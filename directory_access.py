import os.path
import os
import re
import fnmatch


# source file path for excel and google sheet.
master_path = 'C:\\Users\\usenadu\\Documents\\dumidu-pearson\\google api\\2\\excel_files\\'

f = open ("master_file.csv", "r")                 # open source excel file and gogole sheet id list.
f1 = f.readlines()


for line in f1:
    line = line.rstrip()                    # rstrip - remove the new line.
    a = line.split(",")                     # split the line from "comma".
    folder,gsheetid = a[0],a[1]

    #print (folder)
    folder_path = os.path.join(master_path, folder)
    #print (folder_path)


    files = os.listdir(folder_path)
    print (files)

    if len(files) == 0:
        print('Folder is Empty')
    else:
        #print('Folder is Not Empty')           # folder*.xlsx

        excel_files = [os.path.join(dirpath, f)
            for dirpath, dirnames, files in os.walk(folder_path)
            for f in fnmatch.filter(files, '%s*.xlsx' % folder)]
  
        print (excel_files)


   
        def extract_number(f):
            s = re.findall("\d+$",f)
            return (int(s[0]) if s else -1,f)
    
        latest_excel_file = max(excel_files,key=extract_number)
        print (latest_excel_file)
    
        #excel_file_path = os.path.join(master_path, folder_path, latest_excel_file)
        #print (excel_file_path)
