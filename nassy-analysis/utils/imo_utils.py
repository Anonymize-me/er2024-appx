import csv

def read_imo_file_header(imo_filename):
    imo_header = {}
    lines = 0

    with open(imo_filename, 'r', newline='') as f:
        imo = csv.reader(f)
        
    
        row = next(imo)
        lines = 1

        ### INFO
        while not(row[0] == '#METADATA'):

            ## Respondant ID & respondant info
            if row[0].startswith('#Respondent'):
                respondantInfo = {}
                while row[0].startswith('#Respondent'):
                    if row[0] == '#Respondent Name': respondantInfo['name'] = row[1]
                    if row[0] == '#Respondent Gender': respondantInfo['gender'] = row[1]
                    if row[0] == '#Respondent Age': respondantInfo['age'] = row[1]
                    if row[0] == '#Respondent Group': respondantInfo['group'] = row[1]

                    row = next(imo)
                    lines += 1

                imo_header['respondant_info'] = respondantInfo
 
            ## Sensors & sensor info
            elif row[0] == '#Sensor info':
                sensorInfo ={}
                while row[0] == '#Sensor info':
                    sensorInfo[row[1]] = row[2:]

                    row = next(imo)
                    lines += 1

                imo_header['sensor_names'] = sensorInfo.keys()
                imo_header['sensor_info'] = sensorInfo
            else:
                row = next(imo)
                lines += 1
       
        
        ### METADATA
        while not(row[0] == '#DATA'):
            ## ...
            # print(', '.join(row))
            #

            row = next(imo)
            lines += 1
        
        
        f.close()

    imo_header['data_line'] = lines

    return imo_header
    