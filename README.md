# descriptors
Descriptors for protein structures

This package allows to parse DSSP files to fetch all helices in individual files. These helices files can then be used to extract atomic coordinates from the original PDB files.

Further, several operations including finding angles, dihedrals, distances, and calculating center of masses can be performed on these files.

All the Python scripts are provided inside the folders along with their outputs.

A few descriptors are calculated using Pymol (.pml) scripts.

## Requirements

You need to install Biopython. Use the following command:

``` pip install biopython```

## Usage

```python3 <script_name.py>```