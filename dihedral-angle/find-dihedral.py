#!/usr/bin/env python3

import __main__
__main__.pymol_argv = [ 'pymol', '-qc'] # Quiet and no GUI


import os
import os.path
import pathlib
import sys
import glob
import sys, time, os
import pymol
from pymol import cmd, stored, CmdException
from chempy import cpv
import math
import io
from contextlib import redirect_stdout


pdb_path = os.getcwd()+"/../step2-convert-dssp-to-pdb/output"

pdb_folder_list = os.listdir(pdb_path)


output = open("result.tsv", "a")

output.write( "Helix 1\tHelix 2\tHelix 3\tCh1\t Ch2\t Ch3\th1_res_st\t h1_res_end\t h1_start\t h1_end\th2_res_st\t h2_res_end\t h2_start\t h2_end\t h3_res_st\t h3_res_end\t h3_start\t h3_end\tangle\r")
            
for dssp_folder in pdb_folder_list:
    prot_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder)
    print("-----------------------------\n\n\r")
    helix_list = os.listdir(prot_path)
  
    
    for helix in helix_list:
        

        helix1_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder+"/"+helix)
       
        print("helix_1 Path: ---", helix1_path)
        i = 0

        with open(helix1_path, "r") as src_file:
            for line in src_file:
                i = i +1
                line_array =  line.split()
                if i == 1:
                    helix1_start = line_array[5]
                    helix1_residue_start = line_array[3]
                helix1_end = line_array[5]
                helix1_residue_end = line_array[3]
                Ch1 = line_array[4]
                res1 = line_array[3]
        

        file_number = 0


        for next_helix in helix_list:
            
            try:
                helix2_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder+"/"+next_helix)

                j = 0
                with open(helix2_path, "r") as src_file2:
                    for line2 in src_file2:
                        j = j + 1
                        line_array2 =  line2.split()
                        if j == 1:
                            helix2_start = line_array2[5]
                            helix2_residue_start = line_array2[3]
                        helix2_end = line_array2[5]
                        helix2_residue_end = line_array2[3]
                        Ch2 = line_array2[4]
                        res2 = line_array2[3]

                
                for third_helix in helix_list:
                    helix3_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder+"/"+third_helix)
                
                    k = 0
                    with open(helix3_path, "r") as src_file3:
                        for line3 in src_file3:
                            k = k +1
                            line_array3 =  line3.split()
                            if k == 1:
                                helix3_start = line_array3[5]
                                helix3_residue_start = line_array3[3]
                            helix3_end = line_array3[5]
                            helix3_residue_end = line_array3[3]
                            Ch3 = line_array3[4]
                            res13 = line_array3[3]

                
                    pymol.cmd.reinitialize('everything')            
                    pymol.cmd.load(helix1_path, "C1")
                    pymol.cmd.load(helix2_path, "C2")
                    pymol.cmd.load(helix3_path, "C3")

                    f = io.StringIO()
                    with redirect_stdout(f):
                        
                        pymol.cmd.do("get_dihedral /C1//"+Ch1+"/"+helix1_residue_start+"`"+helix1_start+"/CA, /C1//"+Ch1+"/"+helix1_residue_end+"`"+helix1_end+"/CA, /C2//"+Ch2+"/"+helix2_residue_start+"`"+helix2_start+"/CA, /C2//"+Ch2+"/"+helix2_residue_end+"`"+helix2_end+"/CA",0,0)

                        command1 = "get_dihedral /C1//"+Ch1+"/"+helix1_residue_start+"`"+helix1_start+"/CA, /C1//"+Ch1+"/"+helix1_residue_end+"`"+helix1_end+"/CA, /C2//"+Ch2+"/"+helix2_residue_start+"`"+helix2_start+"/CA, /C2//"+Ch2+"/"+helix2_residue_end+"`"+helix2_end+"/CA"
                    out_1 = f.getvalue()

                    g = io.StringIO()
                    with redirect_stdout(g):
                        
                        pymol.cmd.do("get_dihedral /C1//"+Ch1+"/"+helix1_residue_end+"`"+helix1_end+"/CA, /C2//"+Ch2+"/"+helix2_residue_start+"`"+helix2_start+"/CA, /C2//"+Ch2+"/"+helix2_residue_end+"`"+helix2_end+"/CA, /C3//"+Ch3+"/"+helix3_residue_start+"`"+helix3_start+"/CA",0,0)

                        command2  = "get_dihedral /C1//"+Ch1+"/"+helix1_residue_end+"`"+helix1_end+"/CA, /C2//"+Ch2+"/"+helix2_residue_start+"`"+helix2_start+"/CA, /C2//"+Ch2+"/"+helix2_residue_end+"`"+helix2_end+"/CA, /C3//"+Ch3+"/"+helix3_residue_start+"`"+helix3_start+"/CA"
                    out_2 = g.getvalue()

                    output.write(
                        helix.replace(".dssp_","").replace("OUTPUT.pdb","")+"\t"
                        +next_helix.replace(".dssp_","").replace("OUTPUT.pdb","")+"\t"
                        +third_helix.replace(".dssp_","").replace("OUTPUT.pdb","")+"\t"
                        +Ch1                    +"\t"
                        +Ch2                    +"\t"
                        +Ch3                    +"\t"
                        +helix1_residue_start+"\t"
                        +helix1_residue_end  +"\t"
                        +helix1_start+"\t"
                        +helix1_end                    +"\t"
                        +helix2_residue_start                    +"\t"
                        +helix2_residue_end                    +"\t"
                        +helix2_start                    +"\t"
                        +helix2_end                    +"\t"
                        +"\t"
                        +"\t"
                        +"\t"
                        +"\t"
                        +out_1.replace("cmd.get_dihedral:","").replace(" degrees.","").strip(' \n\t')

                        +"\r"
                        )

                    output.write(
                        helix.replace(".dssp_","").replace("OUTPUT.pdb","")+"\t"
                        +next_helix.replace(".dssp_","").replace("OUTPUT.pdb","")+"\t"
                        +third_helix.replace(".dssp_","").replace("OUTPUT.pdb","")+"\t"
                        +Ch1                    +"\t"
                        +Ch2                    +"\t"
                        +Ch3                    +"\t"
                        +helix1_residue_start+"\t"
                        +helix1_residue_end  +"\t"
                        +helix1_start+"\t"
                        +helix1_end                    +"\t"
                        +helix2_residue_start                    +"\t"
                        +helix2_residue_end                    +"\t"
                        +helix2_start                    +"\t"
                        +helix2_end                    +"\t"
                        +helix3_residue_start                    +"\t"
                        +helix3_residue_end                    +"\t"
                        +helix3_start                    +"\t"
                        +helix3_end                    +"\t"
                        +out_2.replace("cmd.get_dihedral:","").replace(" degrees.","").strip(' \n\t')
                    
                        +"\r")

                file_number = file_number + 1

                
            except:
               
                continue
        
      
        print("helix_2 Path: ---", helix2_path)

        print("\n\n\n\n\n\n\n\n")

           
          



