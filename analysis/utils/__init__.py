# -*- coding: utf-8 -*-
__all__ = [
    'read_json', 'make_ticks',
    'read_imo_file_header',
     'modmax','lhipa', 'batch_sliding_window_lhipa'
]

if __name__ == '__main__':
    # Load specific packages/libraries/modules
    pass
else:
    from .imo_utils import read_imo_file_header
    from .lhipa_utils import lhipa, modmax, sliding_window_lhipa, batch_sliding_window_lhipa



import json
import pandas as pd
from numpy import min as npmin,  max as npmax, linspace

def read_json(path):
    with open(path, encoding='utf-8') as inFile:
        return json.load(inFile)
    

def make_ticks(start, stop, step, maxSteps=None):
    n = int((stop-start) // step) + 1
    if maxSteps:
        while n > maxSteps-2:
            step *= 2
            n = int((stop-start) // step) + 1

    bins = linspace(start, n * step, num=n+1)

    return bins


def norm(s):
    return (s - npmin(s))/(npmax(s)-npmin(s))




def execute_main():
    # Test make_ticks
    bins = make_ticks(0, 173.9, 10)
    print(f'Bins <0, 173.9, 10>:[{bins}]')
    return
def execute_onLoad():
    # Nothing do do
    return
if __name__ == '__main__': execute_main()
else: execute_onLoad()