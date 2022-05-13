#!/usr/bin/env python3

'''
  this file takes output files from step 1 and creates pdb files in the output directory.
'''

import os
import os.path
import pathlib
import glob
import sys
import re
import fnmatch


dssp_path = os.getcwd()+"/../step1-break_dssp_files_into_helices-dssp/output"
pdb_path = os.getcwd()+"/../original-data/pdb_files_for_step_2"
output_path = os.getcwd()+"/output"

#read all filenames in the dirs

dssp_dir = os.listdir(dssp_path)
pdb_files = os.listdir(pdb_path)


#collecting the total number of dssp files in the directory.

num_files = len(glob.glob1(dssp_path,"*.dssp"))

print('There are',num_files, 'dssp files in the input directory\n\n')

files_read = 0


for dssp_folder in dssp_dir:
    print("Ref PDB Looking into: ", dssp_folder)   
    if fnmatch.fnmatch(dssp_folder, '*.dssp'):
        #open file to read from
        dssp_files = os.listdir(os.path.join(dssp_path, dssp_folder))
        print("there ",os.path.join(dssp_path, dssp_folder))
        for dssp_helix in dssp_files:
            print("Processing: ", dssp_helix)
            pdbfilename_array = dssp_helix.split('.')
            pdbfilename_to_look_in = pdbfilename_array[0]+".pdb"
            with open(os.path.join(os.path.join(dssp_path, dssp_folder), dssp_helix), "r") as src_file:
                try:
                    os.makedirs(os.path.join(output_path, dssp_folder))
                except:
                    print('')
                with open(os.path.join(os.path.join(output_path, dssp_folder),dssp_helix+"_OUTPUT.pdb"), "a") as out_file:
                    #read each line in the file
                    for line in src_file:
                        linearray = line.split()
                        try:
                            atom_to_search = linearray[1]
                            print("atom to search ", atom_to_search)
                            with open(os.path.join(pdb_path, pdbfilename_to_look_in), "r") as pdb_file_handle:
                                for search_line in pdb_file_handle:
                                    search_line_array = search_line.split()
                                    if search_line_array[0] == "ATOM":
                                        if int(search_line_array[5]) == int(atom_to_search):
                                            out_file.write(search_line)

                        except:
                            continue
                                
                        print ("\n\n\n----------------------------------------\n")
                            


