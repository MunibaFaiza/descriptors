#!/usr/bin/env python3

import os
import os.path
import pathlib
import glob
import itertools
import collections
import pprint
import sys
import re



input_path = os.getcwd()+"/../original-data/dssp_files_for_step_1/"


#read all filenames in the dir

file_list = os.listdir(input_path)

output_path = os.getcwd()+"/output"


#collecting the total number of log files in the directory.

num_files = len(glob.glob1(input_path,"*.dssp"))
print('There are',num_files, 'dssp files in the input directory\n\n')



matches = ["H  >", "H  <", "H  3>", "H  3<", "H  4", "H  X", "H >", "H 3", "H <", "H X", "H 4"]
short_matches = ["G 3", "G 4", "G X","G >", "G <", "G  3", "G  X","G  >", "G  <", "G  4"]


# read all files in file list and for every file do this:
for file_name in file_list:


	os.makedirs(os.path.join(output_path, file_name))

	import fnmatch

	if fnmatch.fnmatch(file_name, '*.dssp'):
		
		with open(os.path.join(input_path, file_name), "r") as src_file:


			line_was_helix = 0
			filecounter = 0
			line_is_helix = 0

			last_line_matched = 0

			for line in src_file:
					
					set_line_header = ''
					if '#' in line:
						line_header = line
						set_line_header = line_header
					last_line_matched = line_is_helix
					line_is_helix = 0
					#---------------------------------------------
					for helix in matches:						
						if helix in line:
							line_is_helix = 1
							match_type = 1

					for helix in short_matches:						
						if helix in line:
							line_is_helix = 1
							match_type = 2

					if line_is_helix ==1:
					
						if not last_line_matched:
							filecounter +=1
							set_line_header = line_header

							
						os.chdir(os.path.join(output_path, file_name))
						if match_type == 1:
							prefix = "_H_"
						else:
							prefix = "_G_"
						with open(file_name+prefix+str(filecounter)+".dssp", "a") as h:
							print(set_line_header+"\n"+line+"\n",file=h)
							h.close()							
						
	else:
		continue
print("The output is provided in longH_output directory.")
