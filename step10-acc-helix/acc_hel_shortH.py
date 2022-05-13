#!/usr/bin/env python3

import os
import os.path
import pathlib
import glob
import sys
import re
import fnmatch


dssp_path = os.getcwd()+"/../step8-helix-length/shortH_output_pdb_files_ed"


#read all filenames in the dirs

dssp_files = os.listdir(dssp_path)



#collecting the total number of dssp files in the directory.

num_files = len(glob.glob1(dssp_path,"*.dssp"))

print('There are',num_files, 'dssp files in the input directory\n\n')

def sum_of_list(l):
    total = 0
    for val in l:
        total = total + val
        return total

for dssp_helix in dssp_files:
    print("Processing: ", dssp_helix)
    
    if fnmatch.fnmatch(dssp_helix, '*.dssp'):
        #open file to read from
        with open(os.path.join(dssp_path, dssp_helix), "r") as src_file:
            with open("acc_hel_shortH.txt", 'a') as acc_file:

                print(dssp_helix, ':', file=acc_file)
                
                i = 0
                acc = []
                
                for line in src_file:
                        
                        linearray = line.split()
                        #print(linearray)
                        

                        try:
                            i = i + 1
                            if i==1:
                                continue
                            
                            acc.append(linearray[9])
                            


                            #print (sum(int(j) for j in acc))
                            
                            
                            #print (acc, '\n', file=acc_file)
                            
                            
                        except:
                            continue
                
                sum_acc = str(sum(int(x) for x in acc))
                len_acc = len(acc)

                tot_acc = float(sum_acc)/len_acc
                print(round(tot_acc, 3), '\n', file=acc_file)
                

                