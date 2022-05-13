#!/usr/bin/env python3

from Bio.PDB import *
import numpy as np


import math 
import sys
import os
import os.path

helix_path = os.getcwd()+"/shortH_output_pdb_files_ed"
helix_files = os.listdir(helix_path)

for helix in helix_files:
    print("Processing: ", helix)

    with open(os.path.join(helix_path, helix), "r") as helix_file:
        with open("helix_length_shortH.txt", 'a') as len_file:

            print(helix, ":", file=len_file)

            file_name = os.path.splitext(helix)
            fname = file_name[0]

            pdb_file = os.path.join(helix_path, helix)
            
            p=PDBParser()


            structure=p.get_structure(fname, pdb_file)
            
            for model in structure:
                for chain in model:

                    CA_Coord = []
                    for residue in chain:
                        #CA_coordinates = np.append(CA_coordinates, residue['CA'].get_vector())
                        # print(residue['CA'])
                        CA_Coord.append((residue['CA'].get_vector()))

                    """print(CA_Coord)
                    print("\n-----------------")
                    print(CA_Coord[0])
                    print(CA_Coord[-1])
                    """
                    x1 = CA_Coord[0][0]
                    y1 = CA_Coord[0][1]
                    z1 = CA_Coord[0][2]
                    x2 = CA_Coord[-1][0]
                    y2 = CA_Coord[-1][1]
                    z2 = CA_Coord[-1][2]

                    length_of_helix = ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)**0.5

                    len_of_helix = round(length_of_helix, 3)
                    print(len_of_helix, "\n" , file=len_file)
