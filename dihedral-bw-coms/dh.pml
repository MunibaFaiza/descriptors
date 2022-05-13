# run the script which calculate COM (define the command com)
run /home/muniba/Desktop/vdr_descriptors/center_of_mass.py

fetch 5yt2
hide all
sh cartoon


# pasted from "get_view" command to orient your structure in 3D space
set_view (\
     0.209348783,    0.402222723,   -0.891285002,\
    -0.783612072,   -0.476212919,   -0.398965567,\
    -0.584914505,    0.781944692,    0.215491712,\
     0.000000000,    0.000000000, -164.951812744,\
    13.140365601,   20.581226349,   41.893451691,\
   130.049270630,  199.854354858,  -20.000000000 )

# defined secondary structures
select H6, resi 256-274
select H7, resi 297-301
select Hx, resi 410-413
select H12, resi 416-422

# calculation of center of mass for the selected helices
com H6
com H7
com Hx
com H12



#write the results into .txt file
import csv

f=open('dihedral-coms.txt','a')

dh1=cmd.get_dihedral('tmp, /H6_COM/PSDO/P/PSD`1/PS1','/H7_COM/PSDO/P/PSD`1/PS1','/Hx_COM/PSDO/P/PSD`1/PS1','/H12_COM/PSDO/P/PSD`1/PS1')
dh2=cmd.get_dihedral('tmp, /H7_COM/PSDO/P/PSD`1/PS1','/Hx_COM/PSDO/P/PSD`1/PS1','/H12_COM/PSDO/P/PSD`1/PS1','/H6_COM/PSDO/P/PSD`1/PS1')
dh3=cmd.get_dihedral('tmp, /Hx_COM/PSDO/P/PSD`1/PS1','/H12_COM/PSDO/P/PSD`1/PS1','/H6_COM/PSDO/P/PSD`1/PS1','/H7_COM/PSDO/P/PSD`1/PS1')
dh4=cmd.get_dihedral('tmp, /H12_COM/PSDO/P/PSD`1/PS1','/H6_COM/PSDO/P/PSD`1/PS1','/H7_COM/PSDO/P/PSD`1/PS1','/Hx_COM/PSDO/P/PSD`1/PS1')



    writer = csv.writer(f)
    writer.writerow( ('5yt2',"%10f\a"%dh1,"%10f\a"%dh2,"%10f\a"%dh3,"%10f\a"%dh4) )
  
f.close()


#reinitialize
cmd.reinitialize('everything')