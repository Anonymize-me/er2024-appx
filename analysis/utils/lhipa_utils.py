# LHIPA: to check
# Implementation of Duchowski2018 LHIPA  by Amine Abbad-Andaloussi


import math , pywt , numpy as np

from warnings import warn


# LHIPA is expected to decrease with increased cognitive load
def lhipa(dx, dt, min_sample_size = 100, sym = 'sym5'):
    """
    LHIPA as of Duchowski.

    :param dx: input signal (as compatible with list)
    :param dt: imput signal timestamps  (as compatible with list)
    :param min_sample_size: minimum size of the input signal (sample).
        Default = 100
    :param sym: wavelet type. Default: 'sym5'
    :return: LHIPA index computed on the input signal
    """ 
    
    # find max decomposition level 
    d = list(dx)

    if len(d) > min_sample_size:
        d.insert(0, 0)
        sym = 'sym5'  # modified sym5
        w = pywt.Wavelet(sym)
        maxlevel = pywt.dwt_max_level(len(d), filter_len=w.dec_len)
        hif, lof = 1, int(maxlevel / 2)

        # get detail coefficients of pupil diameter signal d
        cD_H = pywt.downcoef('d', d, sym, 'per', level=hif)
        cD_L = pywt.downcoef('d', d, sym, 'per', level=lof)

        # normalize by 1/ 2j􀀀
        cD_H = [x / math.sqrt(2 ** hif) for x in cD_H]
        cD_L = [x / math.sqrt(2 ** lof) for x in cD_L]

        # obtain the LH:HF ratio
        cD_LH = cD_L

        for i in range(len(cD_L)):
            cD_LH[i] = cD_L[i] / cD_H[int((2 ** lof) / (2 ** hif) * i)]

        # detect modulus maxima , see Duchowski et al. [15]
        cD_LHm = modmax(cD_LH)

        # threshold using universal threshold luniv􀀀= sˆ􀀀 (2logn)
        # where sˆ􀀀 is the standard deviation of the noise
        luniv = np.std(cD_LHm) * math.sqrt(2.0 * np.log2(len(cD_LHm)))
        cD_LHt = pywt.threshold(cD_LHm, luniv, mode="less")

        # get signal duration (in seconds)
        d2 = list(dt)
        tt = (d2[-1] - d2[0]) / 1000

        # compute LHIPA
        ctr = 0
        for i in range(len(cD_LHt)):
            if math.fabs(cD_LHt[i]) > 0:
                ctr += 1
        LHIPA = float(ctr) / tt
        return LHIPA
    
    warn(f'Input signal size (={len(d)}) lower than the minimum (={min_sample_size}). Returned NaN.')
    return np.nan

def modmax(d):
    # compute signal
    m = [math.fabs(di) for di in d]

    # if value is larger than both neighbours, and strictly # larger than either, then it is a local maximum
    t = [0.0] * len(d)
    for i in range(len(d)):
        ll = m[i - 1] if i >= 1 else m[i]
        oo = m[i]
        rr = m[i + 1] if i < len(d) - 1 else m[i]  # change len(d)-2 to len(d)-1
        if (ll <= oo and oo >= rr) and (ll < oo or oo > rr):
            # compute magnitude
            t[i] = math.sqrt(d[i] ** 2)
        else:
            t[i] = 0.0
    return t


def sliding_window_lhipa(dx, dt, w, w_pace):
    l = len(dt)


    # Compute LHIPA
    if w_pace == 'progressive':
        dxe = np.concatenate((dx, dx[-1 - (w-1):0]))
        iDt = dt[-1] - dt[-2]
        dte = np.concatenate((dt, dt[-1]+np.array(1+range(w-1))*iDt))
        dte = dte - dte[0]
        w = -w
    else: # w_pace == 'retrograde'
        dxe = np.concatenate((dx[w-1:0:-1], dx))
        iDt = dt[1] - dt[0]
        dte = np.concatenate((dt[0]-np.array(range(w-1,0,-1))*iDt, dt))
        dte = dte - dte[0]


    lhipa_res_all = np.empty(l)
    for i in range(l):
        lhipa_res_all[i] = lhipa(dxe[i:i+(w-1)], dte[i:i+(w-1)])

    return lhipa_res_all

def batch_sliding_window_lhipa(dx, dt, 
    timeWindows = [10], timeSteps = [-1], w_pace = 'Retrograde'):

    res_all = []
    wFilters = []

    l = len(dt)
    freq = 1000*l/(dt[-1] - dt[0])

    for tStep in timeSteps:
        if tStep > 0:
            wStep = math.floor(freq * tStep)
            if wStep == 0:
                Warning.warn('w_step cannot be lower than 1')
                wStep = 1
            wPos = list(range(0, l, wStep))
        else: wPos = list(range(0, l))
        wFilters.append(wPos)

    for tWindow in timeWindows:
        w = math.floor(freq * tWindow)
        res_all.append(sliding_window_lhipa(dx, dt, w, w_pace))

    return res_all, wFilters


def main_exec():
    print("--> Running main_exec function.\n")
    


def import_exec():
    print("--> Importing lhipa_utils module file.\n")
 

###############################################################################
# End of file
#
if __name__ == "__main__": main_exec()
else: import_exec()