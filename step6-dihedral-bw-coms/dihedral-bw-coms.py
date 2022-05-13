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
from pymol import cmd, stored, CmdException, fitting, creating
from chempy import cpv
import math
import io
from contextlib import redirect_stdout

pymol.finish_launching()


pdb_path = os.getcwd()+"/../step2-convert-dssp-to-pdb/output"

pdb_folder_list = os.listdir(pdb_path)

# pymol.cmd.run("anglebetweenhelices.py")


file1 = open("result.tsv", "a")  # append mode
file1.write("H1\tH2\tH3\tH4\tAngle\r\n")
        
for dssp_folder in pdb_folder_list:
    
    prot_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder)
    
    print("-----------------------------\n\n\r")
    
    helix_list = os.listdir(prot_path)
  
    i = 0
    for helix in helix_list:
        

        helix1_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder+"/"+helix)

        j = 0
        for next_helix in helix_list:
            # # print("File number is ", file_number)

            try:
                helix2_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder+"/"+helix_list[j])
                helix3_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder+"/"+helix_list[j+1])
                helix4_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder+"/"+helix_list[j+2])
                
                j = j + 1

                pymol.cmd.run("center_of_mass.py")
                pymol.cmd.load(helix1_path, "H1")
                pymol.cmd.load(helix2_path, "H2")
                pymol.cmd.load(helix3_path, "H3")
                pymol.cmd.load(helix4_path, "H4")

                pymol.cmd.disable("all")

                f = io.StringIO()
                with redirect_stdout(f):
                    pymol.cmd.do("centerofmass H1",0,0)
                out = f.getvalue()
                out1 = out.replace("Center of Mass:","")
                # print(out1)

                g = io.StringIO()
                with redirect_stdout(g):
                    pymol.cmd.do("centerofmass H2",0,0)
                output = g.getvalue()
                out2 = output.replace("Center of Mass:","")
                # print(out2)

                h = io.StringIO()
                with redirect_stdout(h):
                    pymol.cmd.do("centerofmass H3",0,0)
                out_put = h.getvalue()
                out3 = out_put.replace("Center of Mass:","")
                # print(out3)

                m = io.StringIO()
                with redirect_stdout(m):
                    pymol.cmd.do("centerofmass H4",0,0)
                out_put = m.getvalue()
                out4 = out_put.replace("Center of Mass:","")
                # print(out4)

                pymol.cmd.do("pseudoatom c1, pos="+out1+"")
                pymol.cmd.do("pseudoatom c2, pos="+out2+"")
                pymol.cmd.do("pseudoatom c3, pos="+out3+"")
                pymol.cmd.do("pseudoatom c4, pos="+out4+"")


                k = io.StringIO()
                with redirect_stdout(k):
                    pymol.cmd.do("get_dihedral c1, c2, c3, c4",0,0)
                out5 = k.getvalue()
                print(out5.replace("cmd.get_angle: ","").replace("degrees.",""))


                file1.write(
                    helix.replace(".dssp_","").replace("OUTPUT.pdb","")
                    +"\t"
                    +helix_list[j].replace(".dssp_","").replace("OUTPUT.pdb","")
                    +"\t"
                    +helix_list[j+1].replace(".dssp_","").replace("OUTPUT.pdb","")
                    +"\t"
                    +helix_list[j+2].replace(".dssp_","").replace("OUTPUT.pdb","")
                    +"\t"
                    +out5.replace("cmd.get_dihedral:","").replace(" degrees.","").strip(' \n\t')
                    +"\r"
                    )
                pymol.cmd.reinitialize('everything')           
            except:
                continue


        i = i + 1
                

file1.close()
"""
helix_path = os.getcwd()+"selected_helices"
helix_files = os.listdir(helix_path)

for helix in helix_files:

    file_name = os.path.splitext(helix)
    fname = file_name[0]"""

