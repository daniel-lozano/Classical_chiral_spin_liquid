import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
## These lines are needed to set the right font for the plots
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


#
'''
-------------------- Parameters used in the program --------------------
'''



size_labels=18
N_bins=200
'''
Input variables
'''

Lx=int(input("Enter L of simulation="))
Ly=Lx
Lz=Lx
angle="0"#input("Enter angle=")


T_input_name="Energy_"+str(Lx)+"_"+str(Lx)+"_"+str(Lx)+"_theta"+angle+"_sim_num_0.txt";
T=np.loadtxt(T_input_name)[:,0]

temp_index=["20","30","40"]
colors=["r","g","b"]

if(int(input("Extended temperature histograms yes (1) or no (0): "))):
#    temp_index=["40","30","20","10","0"]#["0","10","20","30","40"]
    temp_index=["49","39","29","19","9"]
    colors=["r","orange","g","b","purple"]
    
    if(int(input("Cool down (1) or Warm up (0):"))):
#        colors=colors[::-1]
#        temp_index=temp_index[::-1]
        temp_index=["0","10","20","30","40"]

label_name=int(input("Lambda (0) or Heisenberg (1): "))
fig=plt.figure(figsize=(8,4))
plt.subplots_adjust(left=0.15, bottom=0.165, right=0.95, top=0.95)

for i in range(len(temp_index)):
    
    temp=temp_index[i]
    
    dot_product=np.loadtxt("histogram_"+str(Lx)+"_T"+temp+".dat")
    label=r"$ T=%.3f J_\chi $" %(T[int(temp)])
    
    if(label_name):
        label=r"$ T=%.3f J $" %(T[int(temp)])
        
    
    plt.hist(dot_product,alpha=0.6,bins=N_bins,color=colors[i],label=label)


plt.axvline(-1/3.,color="k")
plt.xlim(-1,1)
plt.legend(prop={'size': size_labels})
plt.tick_params(labelsize=size_labels)
plt.xlabel(r"$ \mathbf{S}_i \cdot \mathbf{S}_j $", size=size_labels)
plt.show()


