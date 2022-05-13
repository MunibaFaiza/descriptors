#!/usr/bin/python3


import math 
import sys
import os

dssp_path = os.getcwd()+"/../step2-convert-dssp-to-pdb/output"
dssp_folder_list = os.listdir(dssp_path)



for dssp_folder in dssp_folder_list:
    helix_path = os.path.join(os.getcwd()+"/../step2-convert-dssp-to-pdb/output/"+dssp_folder)
    helix_list = os.listdir(helix_path)

    for helix in helix_list:
        print("Processing: ", helix)

        with open(os.path.join(helix_path, helix), "r") as Structure:
            with open("test.txt", 'a') as rg_file:

                print(helix, ':', file=rg_file)
                coord = list()
                mass = list()

                for line in Structure:
                    try:
                        line = line.split()
                        # Following code is adapted from https://github.com/sarisabban/Rg/
                        # Copyright (c) 2017 Sari Sabban
                        x = float(line[6])
                        y = float(line[7])
                        z = float(line[8])
                        coord.append([x, y, z])
                        if line[-1] == 'C':
                            mass.append(12.0107)
                        elif line[-1] == 'O':
                            mass.append(15.9994)
                        elif line[-1] == 'N':
                            mass.append(14.0067)
                        elif line[-1] == 'S':
                            mass.append(32.065)

                    except:
                        pass
                
                xm = [(m*i, m*j, m*k) for (i, j, k), m in zip(coord, mass)]
                tmass = sum(mass)
                rr = sum(mi*i + mj*j + mk*k for (i, j, k), (mi, mj, mk) in zip(coord, xm))
                mm = sum((sum(i) / tmass)**2 for i in zip(*xm))
                rg = math.sqrt(rr / tmass-mm)
                Rg = round(rg,3)
                # end https://github.com/sarisabban/Rg/
                print (Rg, '\n', file=rg_file)