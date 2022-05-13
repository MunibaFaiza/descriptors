#!/usr/bin/python3

'''
	Calculates the Radius of Gyration (Rg) of a protein given its .pdb 
	structure file. Returns the Rg integer value in Angstrom.
'''

import math 
import sys
import os

pdb_path = os.getcwd()+"/../original-data/pdb_files_for_step_2"
pdb_files = os.listdir(pdb_path)

for pdb_file in pdb_files:
    print("Processing: ", pdb_file)

    with open(os.path.join(pdb_path, pdb_file), "r") as Structure:
        with open("rg_proteins.txt", 'a') as rg_file:

            print(pdb_file, ':', file=rg_file)
            coord = list()
            mass = list()

            for line in Structure:
                try:
                    line = line.split()
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
            print (Rg, '\n', file=rg_file)