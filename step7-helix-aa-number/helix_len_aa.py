#!/usr/bin/env python3

import os
import os.path
import pathlib
import sys
import re
import glob
import fnmatch
from pprint import pprint

dssp_path = os.getcwd()+"/../step1-break_dssp_files_into_helices-dssp/output"

dssp_folder_list = os.listdir(dssp_path)

num_files = len(glob.glob1(dssp_path,"*.dssp"))

print('There are',num_files, 'dssp files in the input directory\n\n')


for dssp_folder in dssp_folder_list:
    helix_path = os.path.join(os.getcwd()+"/../step1-break_dssp_files_into_helices-dssp/output/"+dssp_folder)
    helix_list = os.listdir(helix_path)
    for helix in helix_list:
        print("Processing: ", helix)

        with open(os.path.join(helix_path, helix), "r") as src_file:
            with open("test", 'a') as len_file:
                
                
                start = 0           
                i = 0
                linesfound = 0
                for line in src_file:
                    i = i +1
                    if i == 1:
                        continue
            
                    linearray = line.split()

                    try:
                        print(linearray[1])
                        linesfound = linesfound + 1
                        
    ######################
                        
                        if linesfound == 1:
                            
                            start = linearray[1]

                        end = linearray[1]

    ######################         
                    except:
                            continue
                    
                    difference =  int(end) - int(start)
                    exact_num = 1
                    helix_len = (difference + exact_num)
                
                    

                print("\nStart: ", start)
                print("End: ", end)
                print("Difference: ", difference)
                print("Helix Length", helix_len)
                print((helix, ':', helix_len,), file=len_file)
            
                
            
                
