import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.colors


matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'



def exponential(x,A,q):
    return A*np.exp(-q*x)

temp_index=input("Enter temperature index (0, 10, 20, 30, 40)=")
input_name="chiral_10_10_10_"+temp_index+"_theta0_sim_num_0.bin"

File=np.loadtxt(input_name)
#print(File)

T=np.loadtxt("average_thermodynamic_data_L10.txt")[:,0]
#print(T)

print(len(File[:,0]))
N_space=100
config_number=len(File[:,0])//N_space
#exit()

projection=[]#np.array([])
for i in range(config_number):
    config=i*N_space
    projection.extend(File[config,:])


plt.subplot(111)
counts, bins, bars=plt.hist(projection,bins=100)
plt.title(r"Configuration=%i, T=%.3f, $\bar{P}_z$=%.3f" %(config,T[int(temp_index)],np.mean(projection)))

plt.show()
    
#exit()
    
    
if(int(input("Plot multiple temperatures: no (0) or yes (1): "))):

    plt.subplot(111)
    for temp_index in ["0","10","20","30","40"]:
        input_name="chiral_10_10_10_"+temp_index+"_theta0_sim_num_0.bin"
        File=np.loadtxt(input_name)
        
        projection=[]
        for i in range(config_number):
            config=i*N_space
            projection.extend(File[config,:])
            
        counts, bins, bars=plt.hist(projection,bins=100,alpha=0.8,label=r"$ T=%.3f $" %(T[int(temp_index)]))
        
#        counts, bins, bars=plt.hist(projection,bins=100,alpha=0.8,label=r"$ T=%.3f/\lambda $" %(T[int(temp_index)]))
        
        
    plt.axvline(-0.7698,linestyle="--",color="k")
    plt.legend()
    plt.show()
    
        

