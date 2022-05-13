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

pymol.cmd.run("anglebetweenhelices.py") #This is a Pymol script.


for dssp_folder in pdb_folder_list:
    prot_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder)
    print("pdb,helix1,helix2,helix1_start,helix1_end,helix2_start,helix2_end,angle\r")
    helix_list = os.listdir(prot_path)
    output = open("result.csv", "a")
    output.write("pdb,helix1,helix2,helix1_start,helix1_end,helix2_start,helix2_end,angle\r")
    for helix in helix_list:
        helix1_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder+"/"+helix)
        
        i = 0
        with open(helix1_path, "r") as src_file:
            for line in src_file:
                i = i +1
                line_array =  line.split()
                if i == 1:
                    helix1_start = line_array[5]
                helix1_end = line_array[5]

        for helix_2 in helix_list:
            helix2_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder+"/"+helix_2)
            if helix_2 == helix:
                continue
            
            j = 0
            with open(helix2_path, "r") as helix2_file:
                
                for line_2 in helix2_file:
                    j = j +1
                    line_2_array =  line_2.split()
                    if j == 1:
                        helix2_start = line_2_array[5]
                    helix2_end = line_2_array[5]
            
            pymol.finish_launching()
            pymol.cmd.load(helix1_path)
            pymol.cmd.load(helix2_path)
            pymol.cmd.disable("all")


            f = io.StringIO()
            with redirect_stdout(f):
                pymol.cmd.do("angle_between_helices resi "+helix1_start+"-"+helix1_end+", resi "+helix2_start+"-"+helix2_end,0,0)
            out = f.getvalue()
            out = out.replace("Using method: helix_orientation","").replace("Angle: ","").replace("deg","")
            pymol.cmd.reinitialize('everything')

            print(dssp_folder.replace(".dssp","")+","+helix.replace(dssp_folder,"").replace(" ","").replace(".dssp_OUTPUT.pdb","").replace(".dssp","").replace("_","")+","+helix_2.replace(dssp_folder,"").replace(".dssp_OUTPUT.pdb","").replace(".dssp","").replace("_","")+","+helix1_start+","+helix1_end+","+helix2_start+","+helix2_end+","+out.strip(' \n\t'))

            
            output.write(dssp_folder.replace(".dssp","")+","+helix.replace(dssp_folder,"").replace(" ","").replace(".dssp_OUTPUT.pdb","").replace(".dssp","").replace("_","")+","+helix_2.replace(dssp_folder,"").replace(".dssp_OUTPUT.pdb","").replace(".dssp","").replace("_","")+","+helix1_start+","+helix1_end+","+helix2_start+","+helix2_end+","+out.strip(' \n\t')+"\r")


output.close()
           
          



