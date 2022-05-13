#!/usr/bin/env python3

import os
import os.path
import pathlib
import sys
import glob


dssp_path = os.getcwd()+"/../original-data/dssp_files_for_step_1"
dssp_files = os.listdir(dssp_path)

for dssp in dssp_files:

    print("Processing: ", dssp)

    with open(os.path.join(dssp_path, dssp), "r") as dssp_file:
        with open("sse_prot.txt", 'a') as sse_file:

            print('\n\n', dssp, ':', file=sse_file)

            # Following code is adapted from 
            dssp_lines = [line.rstrip() for line in dssp_file]

            resamount = len(dssp_lines)-28
            dssp_structures = ['H', 'B', 'E', 'G', 'I', 'T', 'S']
            sses=list()


            for line in range(28, len(dssp_lines)):
                if dssp_lines[line][16] in dssp_structures:
                    sses.append(dssp_lines[line][16])

            H = sses.count('H')/resamount*100
            B = sses.count('B')/resamount*100
            E = sses.count('E')/resamount*100
            G = sses.count('G')/resamount*100
            I = sses.count('I')/resamount*100
            T = sses.count('T')/resamount*100
            S = sses.count('S')/resamount*100
            O = (resamount - len(sses))/resamount*100

            print('====Calculating the number of residues forming the secondary structures for', dssp, '====')

            print('\n',
                    f'Percentage of Helix: {round(H, 2)}% \n',
                    f'Percentage of Beta bridge: {round(B, 2)}% \n',
                    f'Percentage of Strand: {round(E, 2)}%, \n',
                    f'Percentage of Helix-3: {round(G, 2)}% \n',
                    f'Percentage of Helix-5: {round(I, 2)}% \n',
                    f'Percentage of Turn: {round(T, 2)}% \n',
                    f'Percentage of Bend: {round(S, 2)}% \n',
                    f'Percentage of other residues: {round(O, 2)}%', file=sse_file)

            print('\n', f'The total percentage: {H + B + E + G + I + T + S + O} %', file=sse_file)

            

          
           
