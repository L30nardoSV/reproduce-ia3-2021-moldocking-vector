import sys
import os
import csv
import pandas as pd

def retrieve_runtime(filename):
    """Retrieve runtime (s) from dlg"""

    with open(filename, "rt") as myfile:   # open file for reading text
        lines = myfile.readlines()

        found_keyword = False
        found_keyword_2 = False

        for line in lines:
            if line.startswith('Docking run time'):
                found_keyword = True
           
            if found_keyword:
                docking_runtime = float(line[17:23])
                found_keyword = False
                #print(docking_runtime)

            if line.startswith('Program run time'):
                found_keyword_2 = True

            if found_keyword_2:
                program_runtime = float(line[17:23])
                found_keyword_2 = False
                #print(program_runtime)
        
    return docking_runtime, program_runtime

def parse_dirname(dirname):
    name_list = dirname.split('_')
    device = name_list[1]
    return device

def parse_filename(filename):
    head, tail = os.path.split(filename)
    #print("Filename head: %s" %(head))
    #print("Filename tail: %s" %(tail))
    name_list = tail.replace('.', '_')
    name_list = tail.replace('-', '_')
    name_list = name_list.split('_')
    #print(name_list)

    pdb = name_list[0]
    popsize = name_list[1]
    lsmet = name_list[2]

    return pdb, popsize, lsmet

def reorder_metafile(metafile):

    # --------------------------------------------------------------------
    # Sublists
    list_1u4d, list_1xoz, list_1yv3, list_1owe, list_1oyt, list_1ywr, list_1t46, list_2bm2, list_1mzc, list_1r55 = [['0', '0', '0', '0', '0'] for i in range(10)]
    list_5wlo, list_1kzk, list_3s8o, list_5kao, list_1hfs, list_1jyq, list_2d1o, list_3drf, list_4er4, list_3er5 = [['0', '0', '0', '0', '0'] for i in range(10)]

    for idx in metafile:
        if idx[0] == '1u4d':
            if   idx[1] == '128':  list_1u4d[0] = idx
            elif idx[1] == '256':  list_1u4d[1] = idx
            elif idx[1] == '512':  list_1u4d[2] = idx
            elif idx[1] == '1024': list_1u4d[3] = idx
            elif idx[1] == '2048': list_1u4d[4] = idx
            else: print('error')
        elif idx[0] == '1xoz':
            if   idx[1] == '128':  list_1xoz[0] = idx
            elif idx[1] == '256':  list_1xoz[1] = idx
            elif idx[1] == '512':  list_1xoz[2] = idx
            elif idx[1] == '1024': list_1xoz[3] = idx
            elif idx[1] == '2048': list_1xoz[4] = idx
            else: print('error')
        elif idx[0] == '1yv3':
            if   idx[1] == '128':  list_1yv3[0] = idx
            elif idx[1] == '256':  list_1yv3[1] = idx
            elif idx[1] == '512':  list_1yv3[2] = idx
            elif idx[1] == '1024': list_1yv3[3] = idx
            elif idx[1] == '2048': list_1yv3[4] = idx
            else: print('error')
        elif idx[0] == '1owe':
            if   idx[1] == '128':  list_1owe[0] = idx
            elif idx[1] == '256':  list_1owe[1] = idx
            elif idx[1] == '512':  list_1owe[2] = idx
            elif idx[1] == '1024': list_1owe[3] = idx
            elif idx[1] == '2048': list_1owe[4] = idx
            else: print('error')
        elif idx[0] == '1oyt':
            if   idx[1] == '128':  list_1oyt[0] = idx
            elif idx[1] == '256':  list_1oyt[1] = idx
            elif idx[1] == '512':  list_1oyt[2] = idx
            elif idx[1] == '1024': list_1oyt[3] = idx
            elif idx[1] == '2048': list_1oyt[4] = idx
            else: print('error')       
        elif idx[0] == '1ywr':
            if   idx[1] == '128':  list_1ywr[0] = idx
            elif idx[1] == '256':  list_1ywr[1] = idx
            elif idx[1] == '512':  list_1ywr[2] = idx
            elif idx[1] == '1024': list_1ywr[3] = idx
            elif idx[1] == '2048': list_1ywr[4] = idx
            else: print('error')
        elif idx[0] == '1t46':
            if   idx[1] == '128':  list_1t46[0] = idx
            elif idx[1] == '256':  list_1t46[1] = idx
            elif idx[1] == '512':  list_1t46[2] = idx
            elif idx[1] == '1024': list_1t46[3] = idx
            elif idx[1] == '2048': list_1t46[4] = idx
            else: print('error')
        elif idx[0] == '2bm2':
            if   idx[1] == '128':  list_2bm2[0] = idx
            elif idx[1] == '256':  list_2bm2[1] = idx
            elif idx[1] == '512':  list_2bm2[2] = idx
            elif idx[1] == '1024': list_2bm2[3] = idx
            elif idx[1] == '2048': list_2bm2[4] = idx
            else: print('error')
        elif idx[0] == '1mzc':
            if   idx[1] == '128':  list_1mzc[0] = idx
            elif idx[1] == '256':  list_1mzc[1] = idx
            elif idx[1] == '512':  list_1mzc[2] = idx
            elif idx[1] == '1024': list_1mzc[3] = idx
            elif idx[1] == '2048': list_1mzc[4] = idx
        elif idx[0] == '1r55':
            if   idx[1] == '128':  list_1r55[0] = idx
            elif idx[1] == '256':  list_1r55[1] = idx
            elif idx[1] == '512':  list_1r55[2] = idx
            elif idx[1] == '1024': list_1r55[3] = idx
            elif idx[1] == '2048': list_1r55[4] = idx
            else: print('error')
        elif idx[0] == '5wlo':
            if   idx[1] == '128':  list_5wlo[0] = idx
            elif idx[1] == '256':  list_5wlo[1] = idx
            elif idx[1] == '512':  list_5wlo[2] = idx
            elif idx[1] == '1024': list_5wlo[3] = idx
            elif idx[1] == '2048': list_5wlo[4] = idx
            else: print('error')
        elif idx[0] == '1kzk':
            if   idx[1] == '128':  list_1kzk[0] = idx
            elif idx[1] == '256':  list_1kzk[1] = idx
            elif idx[1] == '512':  list_1kzk[2] = idx
            elif idx[1] == '1024': list_1kzk[3] = idx
            elif idx[1] == '2048': list_1kzk[4] = idx
            else: print('error')
        elif idx[0] == '3s8o':
            if   idx[1] == '128':  list_3s8o[0] = idx
            elif idx[1] == '256':  list_3s8o[1] = idx
            elif idx[1] == '512':  list_3s8o[2] = idx
            elif idx[1] == '1024': list_3s8o[3] = idx
            elif idx[1] == '2048': list_3s8o[4] = idx
            else: print('error')
        elif idx[0] == '5kao':
            if   idx[1] == '128':  list_5kao[0] = idx
            elif idx[1] == '256':  list_5kao[1] = idx
            elif idx[1] == '512':  list_5kao[2] = idx
            elif idx[1] == '1024': list_5kao[3] = idx
            elif idx[1] == '2048': list_5kao[4] = idx
            else: print('error')
        elif idx[0] == '1hfs':
            if   idx[1] == '128':  list_1hfs[0] = idx
            elif idx[1] == '256':  list_1hfs[1] = idx
            elif idx[1] == '512':  list_1hfs[2] = idx
            elif idx[1] == '1024': list_1hfs[3] = idx
            elif idx[1] == '2048': list_1hfs[4] = idx
            else: print('error')
        elif idx[0] == '1jyq':
            if   idx[1] == '128':  list_1jyq[0] = idx
            elif idx[1] == '256':  list_1jyq[1] = idx
            elif idx[1] == '512':  list_1jyq[2] = idx
            elif idx[1] == '1024': list_1jyq[3] = idx
            elif idx[1] == '2048': list_1jyq[4] = idx
            else: print('error')
        elif idx[0] == '2d1o':
            if   idx[1] == '128':  list_2d1o[0] = idx
            elif idx[1] == '256':  list_2d1o[1] = idx
            elif idx[1] == '512':  list_2d1o[2] = idx
            elif idx[1] == '1024': list_2d1o[3] = idx
            elif idx[1] == '2048': list_2d1o[4] = idx
            else: print('error')
        elif idx[0] == '3drf':
            if   idx[1] == '128':  list_3drf[0] = idx
            elif idx[1] == '256':  list_3drf[1] = idx
            elif idx[1] == '512':  list_3drf[2] = idx
            elif idx[1] == '1024': list_3drf[3] = idx
            elif idx[1] == '2048': list_3drf[4] = idx
            else: print('error')            
        elif idx[0] == '4er4':
            if   idx[1] == '128':  list_4er4[0] = idx
            elif idx[1] == '256':  list_4er4[1] = idx
            elif idx[1] == '512':  list_4er4[2] = idx
            elif idx[1] == '1024': list_4er4[3] = idx
            elif idx[1] == '2048': list_4er4[4] = idx
            else: print('error')
        elif idx[0] == '3er5':
            if   idx[1] == '128':  list_3er5[0] = idx
            elif idx[1] == '256':  list_3er5[1] = idx
            elif idx[1] == '512':  list_3er5[2] = idx
            elif idx[1] == '1024': list_3er5[3] = idx
            elif idx[1] == '2048': list_3er5[4] = idx
            else: print('error')                                                                                                    
        else:
            print('error!, \t%s, \t%s, \t%s' %(idx[0], idx[1], idx[2]))

    print(list_1u4d); print(list_1xoz); print(list_1yv3); print(list_1owe); print(list_1oyt)
 #   print(list_1ywr); print(list_1t46); print(list_2bm2); print(list_1mzc); print(list_1r55)
 #   print(list_5wlo); print(list_1kzk); print(list_3s8o); print(list_5kao); print(list_1hfs)
 #   print(list_1jyq); print(list_2d1o); print(list_3drf); print(list_4er4); print(list_3er5)

    reordered_metafile = []

    reordered_metafile = list_1u4d + list_1xoz + list_1yv3 + list_1owe + list_1oyt + \
                         list_1ywr + list_1t46 + list_2bm2 + list_1mzc + list_1r55 + \
                         list_5wlo + list_1kzk + list_3s8o + list_5kao + list_1hfs + \
                         list_1jyq + list_2d1o + list_3drf + list_4er4 + list_3er5

    # --------------------------------------------------------------------
    # Sublists: pdb vs runtimes

    R_1u4d, R_1xoz, R_1yv3, R_1owe, R_1oyt, R_1ywr, R_1t46, R_2bm2, R_1mzc, R_1r55 = [['0', '0', '0', '0', '0', '0'] for i in range(10)]
    R_5wlo, R_1kzk, R_3s8o, R_5kao, R_1hfs, R_1jyq, R_2d1o, R_3drf, R_4er4, R_3er5 = [['0', '0', '0', '0', '0', '0'] for i in range(10)]

    R_1u4d[0] = '1u4d'; R_1xoz[0] = '1xoz'; R_1yv3[0] = '1yv3'; R_1owe[0] = '1owe'; R_1oyt[0] = '1oyt'
    R_1ywr[0] = '1ywr'; R_1t46[0] = '1t46'; R_2bm2[0] = '2bm2'; R_1mzc[0] = '1mzc'; R_1r55[0] = '1r55'
    R_5wlo[0] = '5wlo'; R_1kzk[0] = '1kzk'; R_3s8o[0] = '3s8o'; R_5kao[0] = '5kao'; R_1hfs[0] = '1hfs'
    R_1jyq[0] = '1jyq'; R_2d1o[0] = '2d1o'; R_3drf[0] = '3drf'; R_4er4[0] = '4er4'; R_3er5[0] = '3er5'

    # CAUTION
    # Might need to replaced range(4) with range(1),
    # as some folders contain results only for one case (numwi=32)
    # instead of five ones (popsize={128, 256, 512, 1024, 2048})
    for i in range(5):
        R_1u4d[i+1] = list_1u4d[i][2]; R_1xoz[i+1] = list_1xoz[i][2]; R_1yv3[i+1] = list_1yv3[i][2]; R_1owe[i+1] = list_1owe[i][2]; R_1oyt[i+1] = list_1oyt[i][2]
        R_1ywr[i+1] = list_1ywr[i][2]; R_1t46[i+1] = list_1t46[i][2]; R_2bm2[i+1] = list_2bm2[i][2]; R_1mzc[i+1] = list_1mzc[i][2]; R_1r55[i+1] = list_1r55[i][2]
        R_5wlo[i+1] = list_5wlo[i][2]; R_1kzk[i+1] = list_1kzk[i][2]; R_3s8o[i+1] = list_3s8o[i][2]; R_5kao[i+1] = list_5kao[i][2]; R_1hfs[i+1] = list_1hfs[i][2]
        R_1jyq[i+1] = list_1jyq[i][2]; R_2d1o[i+1] = list_2d1o[i][2]; R_3drf[i+1] = list_3drf[i][2]; R_4er4[i+1] = list_4er4[i][2]; R_3er5[i+1] = list_3er5[i][2]

 #   print(R_1u4d); print(R_1xoz); print(R_1yv3); print(R_1owe); print(R_1oyt)
 #   print(R_1ywr); print(R_1t46); print(R_2bm2); print(R_1mzc); print(R_1r55)
 #   print(R_5wlo); print(R_1kzk); print(R_3s8o); print(R_5kao); print(R_1hfs)
 #   print(R_1jyq); print(R_2d1o); print(R_3drf); print(R_4er4); print(R_3er5)

    reordered_runtimes_metafile = []
    reordered_runtimes_metafile = [R_1u4d] + [R_1xoz] + [R_1yv3] + [R_1owe] + [R_1oyt] + \
                                  [R_1ywr] + [R_1t46] + [R_2bm2] + [R_1mzc] + [R_1r55] + \
                                  [R_5wlo] + [R_1kzk] + [R_3s8o] + [R_5kao] + [R_1hfs] + \
                                  [R_1jyq] + [R_2d1o] + [R_3drf] + [R_4er4] + [R_3er5]

    return reordered_runtimes_metafile

def write_csvfile(filename_docking_csv, filename_program_csv, csv_ordered_docking_metafile, csv_ordered_program_metafile):
    with open(filename_docking_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["pdb", "psize=128", "psize=256", "psize=512", "psize=1024", "psize=2048"])
        for row in csv_ordered_docking_metafile:
            writer.writerow(row)

    with open(filename_program_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["pdb", "psize=128", "psize=256", "psize=512", "psize=1024", "psize=2048"])
        for row in csv_ordered_program_metafile:
            writer.writerow(row)

    return filename_docking_csv, filename_program_csv

def main():
    dirname = sys.argv[1]   # first argument is the folder containing .dlg files

    device = parse_dirname(dirname)
    #print(device)

    # Reading only dlg files
    list_files = []
    for file in os.listdir(dirname):
        if file.endswith(".dlg"):
            list_files.append(file)
    #print(list_files)

    csv_sw_docking_metafile = []
    csv_sw_program_metafile = []

    csv_ad_docking_metafile = []
    csv_ad_program_metafile = []

    for filename in list_files:
        pdb, popsize, lsmet = parse_filename(dirname + '/' + filename)
        time_docking, time_program = retrieve_runtime(dirname + '/' + filename)
        #print('%s, \t%s, \t%s, \t%6.2f, \t%6.2f' %(pdb, popsize, lsmet, time_docking, time_program))

        csv_row_sw_docking = []
        csv_row_sw_program = []
        csv_row_ad_docking = []
        csv_row_ad_program = []

        if lsmet == 'sw':
            csv_row_sw_docking.extend([pdb, popsize, time_docking])
            csv_row_sw_program.extend([pdb, popsize, time_program])
            #print(csv_row_sw_docking)
            #print(csv_row_sw_program)
            csv_sw_docking_metafile.extend([csv_row_sw_docking])
            csv_sw_program_metafile.extend([csv_row_sw_program])
        elif lsmet == 'ad':
            csv_row_ad_docking.extend([pdb, popsize, time_docking])
            csv_row_ad_program.extend([pdb, popsize, time_program])
            #print(csv_row_ad_docking)
            #print(csv_row_ad_program)
            csv_ad_docking_metafile.extend([csv_row_ad_docking])
            csv_ad_program_metafile.extend([csv_row_ad_program])
 
    #print(csv_sw_docking_metafile)
    #print(csv_sw_program_metafile)
    #print(csv_ad_docking_metafile)
    #print(csv_ad_program_metafile)

    csv_ordered_sw_docking_metafile = []
    csv_ordered_sw_program_metafile = []
    csv_ordered_ad_docking_metafile = []
    csv_ordered_ad_program_metafile = []

    csv_ordered_sw_docking_metafile = reorder_metafile(csv_sw_docking_metafile)
    csv_ordered_sw_program_metafile = reorder_metafile(csv_sw_program_metafile)
    csv_ordered_ad_docking_metafile = reorder_metafile(csv_ad_docking_metafile)
    csv_ordered_ad_program_metafile = reorder_metafile(csv_ad_program_metafile)

    #print(csv_ordered_sw_docking_metafile)
    #print(csv_ordered_ad_docking_metafile)

    # Produce csv files only with runtimes only
    filename_sw_docking = 'myresults_sw_docking_times' + '_' + device
    filename_sw_program = 'myresults_sw_program_times' + '_' + device
    filename_sw_docking_csv  = filename_sw_docking + '.csv'
    filename_sw_program_csv  = filename_sw_program + '.csv'
    filename_sw_docking_txt  = filename_sw_docking + '.txt'
    filename_sw_program_txt  = filename_sw_program + '.txt'
    filename_sw_docking_xlsx = filename_sw_docking + '.xlsx'
    filename_sw_program_xlsx = filename_sw_program + '.xlsx'

    filename_ad_docking = 'myresults_ad_docking_times' + '_' + device
    filename_ad_program = 'myresults_ad_program_times' + '_' + device
    filename_ad_docking_csv  = filename_ad_docking + '.csv'
    filename_ad_program_csv  = filename_ad_program + '.csv'
    filename_ad_docking_txt  = filename_ad_docking + '.txt'
    filename_ad_program_txt  = filename_ad_program + '.txt'
    filename_ad_docking_xlsx = filename_ad_docking + '.xlsx'
    filename_ad_program_xlsx = filename_ad_program + '.xlsx'    

    filename_sw_docking_csv, filename_sw_program_csv = write_csvfile(filename_sw_docking_csv, filename_sw_program_csv, csv_ordered_sw_docking_metafile, csv_ordered_sw_program_metafile)
    filename_ad_docking_csv, filename_ad_program_csv = write_csvfile(filename_ad_docking_csv, filename_ad_program_csv, csv_ordered_ad_docking_metafile, csv_ordered_ad_program_metafile)    

    # Changing file extension: from csv into txt
    os.rename(filename_sw_docking_csv, filename_sw_docking_txt)
    os.rename(filename_sw_program_csv, filename_sw_program_txt)
    os.rename(filename_ad_docking_csv, filename_ad_docking_txt)
    os.rename(filename_ad_program_csv, filename_ad_program_txt)    

    # Transforming files: from txt into excel
    pd.read_csv(filename_sw_docking_txt, delimiter=",").to_excel(filename_sw_docking_xlsx, index=False)
    pd.read_csv(filename_sw_program_txt, delimiter=",").to_excel(filename_sw_program_xlsx, index=False)
    pd.read_csv(filename_ad_docking_txt, delimiter=",").to_excel(filename_ad_docking_xlsx, index=False)
    pd.read_csv(filename_ad_program_txt, delimiter=",").to_excel(filename_ad_program_xlsx, index=False)    

main()

# python3 collect_results_dlg.py <folder_dlgs>
