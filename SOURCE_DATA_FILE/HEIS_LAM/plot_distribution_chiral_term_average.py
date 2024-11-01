import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.colors


matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


#
#def exponential(x,A,q):
#    return A*np.exp(-q*x)
#
#temp_index=input("Enter temperature index (0, 10, 20, 30, 40)=")
#input_name="chiral_10_10_10_"+temp_index+"_theta0_sim_num_0.bin"
#File=np.loadtxt(input_name)

T=np.loadtxt("average_thermodynamic_data_L10.txt")[:,0]

#print(len(File[:,0]))
N_space=100
#config_number=len(File[:,0])//N_space
config_number=2501//N_space

size_labels=18
N_bins=200
    

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


    
fig=plt.figure(figsize=(8,4))
plt.subplots_adjust(left=0.15, bottom=0.165, right=0.95, top=0.95)

#for t_index in temp_index:
for i in range(len(temp_index)):
    t_index=temp_index[i]
    input_name="chiral_10_10_10_"+t_index+"_theta0_sim_num_0.bin"
    File=np.loadtxt(input_name)
    
    projection=[]
    for j in range(config_number):
        config=j*N_space
        projection.extend(File[config,:])
        
#    counts, bins, bars=plt.hist(projection,bins=100,alpha=0.8,label=r"$ T=%.3f $" %(T[int(temp_index)]))
   
    plt.hist(projection,alpha=0.6,bins=N_bins,color=colors[i],label=r"$ T=%.3f J_\chi $" %(T[int(t_index)]))

#        counts, bins, bars=plt.hist(projection,bins=100,alpha=0.8,label=r"$ T=%.3f/\lambda $" %(T[int(temp_index)]))
    
    
plt.axvline(-0.7698,color="k")
plt.xlim(-1,1)
plt.legend(prop={'size': size_labels})
plt.tick_params(labelsize=size_labels)
plt.xlabel(r"$ \chi_{ijk} $", size=size_labels)
plt.legend()
plt.show()
    
        

