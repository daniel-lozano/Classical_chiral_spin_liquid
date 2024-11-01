import numpy as np
import matplotlib.pyplot as plt
#from constants import *
#from large_N_functions import *

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import animatplot as amp
import matplotlib
import matplotlib.colors
## These lines are needed to set the right font for the plots
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'


#
'''
-------------------- Parameters used in the program --------------------
'''



label_size=14
Shrink=0.8
sizex="10"
Theta="0"
CMAP=matplotlib.colors.LinearSegmentedColormap.from_list("", ["midnightblue","royalblue","orange","red","darkred"])
#CMAP="terrain"#matplotlib.colors.LinearSegmentedColormap.from_list("", ["darkgreen","royalblue","yellow","red"])


'''
-------------------- Plotting program --------------------
'''


Temp_array=np.loadtxt("average_thermodynamic_data_L10.txt")[:,0]
index=4

fig=plt.figure(figsize=(6,8))
plt.subplots_adjust(left=0.10, bottom=0.05, right=0.98, top=0.98, wspace=0.28, hspace=0.25)


for t in range(1,3):

    temp_index_array=str(t*10)
    file_name="Structure_factor_"+sizex+"_"+sizex+"_"+sizex+"_"+temp_index_array+"_theta"+Theta+".bin"
    print(file_name)

    FILE=np.loadtxt(file_name)
    q1=FILE[:,0]
    q2=FILE[:,1]
    
    Spin_Structure_factor_hhl=FILE[:,2]
    Spin_Structure_factor_hk0=FILE[:,3]

    Structure_factor_hhl=FILE[:,4]
    Structure_factor_hk0=FILE[:,5]

    Q_size=10*4##int(input("Enter size of Q_array="))

    Q1=np.reshape(q1,(Q_size,Q_size))
    Q2=np.reshape(q2,(Q_size,Q_size))
    q1=FILE[:,0]*2
    q2=FILE[:,1]*2
    
    '''
    Eliminating the point at 0
    '''
    index_hhl=np.argmax(Structure_factor_hhl)
    index_hk0=np.argmax(Structure_factor_hk0)

    Structure_factor_hk0[index_hk0]=(Structure_factor_hk0[index_hk0-1]+Structure_factor_hk0[index_hk0+1])/2
    Structure_factor_hhl[index_hhl]=(Structure_factor_hhl[index_hhl-1]+Structure_factor_hhl[index_hhl+1])/2
    ### Setting the value to the new max which corresponds to another Gamma point
    Structure_factor_hk0[index_hk0]=np.max(Structure_factor_hk0)
    Structure_factor_hhl[index_hhl]=np.max(Structure_factor_hhl)
    
    Structure_factor_hhl= np.reshape(Structure_factor_hhl,(Q_size,Q_size))
    Structure_factor_hk0= np.reshape(Structure_factor_hk0,(Q_size,Q_size))
    
    Q1=Q1[1:,1:]*2
    Q2=Q2[1:,1:]*2
    Structure_factor_hhl= Structure_factor_hhl[1:,1:]
    Structure_factor_hk0= Structure_factor_hk0[1:,1:]
    
    
    Spin_Structure_factor_hhl= np.reshape(Spin_Structure_factor_hhl,(Q_size,Q_size))
    Spin_Structure_factor_hk0= np.reshape(Spin_Structure_factor_hk0,(Q_size,Q_size))
    Spin_Structure_factor_hhl= Spin_Structure_factor_hhl[1:,1:]
    Spin_Structure_factor_hk0= Spin_Structure_factor_hk0[1:,1:]
    

    print(3,2,2*(t-1)+1)
    
    plt.subplot(3,2,2*(t-1)+2)
    input_name="SCGA_hk0_plane_"+str(t)+".txt"
    x_label=r"$[h00]$"
    y_label=r"$[0k0]$"
    plt.gca().set_aspect('equal')
    
    plt.pcolormesh(Q1,Q2,Spin_Structure_factor_hk0,cmap=CMAP,shading='auto')
    plt.ylabel(y_label,size=label_size)
    
    plt.yticks(size=label_size)
    plt.title(r"$T=%.3fJ_\chi$" %Temp_array[t*10],size=label_size)
    cbar=plt.colorbar(orientation="vertical",pad=0.1, shrink=Shrink)
    cbar.ax.tick_params(labelsize=label_size)
#    plt.clim(min(Structure_factor_hk0.flatten()),max(Structure_factor_hk0.flatten()))
    plt.clim(2,7)
    
    plt.xticks([-2,0,2])
    if(t==3):
        plt.xticks([-2,0,2])
#        plt.xticks(size=label_size)
    plt.xlabel(x_label,size=label_size)
    
    plt.xticks(size=label_size)
    plt.yticks(size=label_size)
    
    
    print(3,2,2*(t))
    plt.subplot(3,2,2*(t-1)+1)
    
    input_name="SCGA_hhl_plane_"+str(t)+".txt"
    x_label=r"$[hh0]$"
    y_label=r"$[00\ell]$"
    plt.gca().set_aspect(1/np.sqrt(2))


    plt.pcolormesh(Q1,Q2,Spin_Structure_factor_hhl,cmap=CMAP,shading='auto')
   
    plt.ylabel(y_label,size=label_size)
    plt.xticks([-2,0,2])
    if(t==3):
        plt.xticks([-2,0,2])
       
    plt.xlabel(x_label,size=label_size)
    plt.xticks(size=label_size)
    plt.yticks(size=label_size)
    plt.title(r"$T=%.3fJ_\chi$" %Temp_array[t*10],size=label_size)
    cbar=plt.colorbar(orientation="vertical",pad=0.1, shrink=Shrink)
    cbar.ax.tick_params(labelsize=label_size)
    plt.clim(2,7)



"""
----------------------------------------------------------------------------------------------------
--------------------------------------------- IM plots ---------------------------------------------
----------------------------------------------------------------------------------------------------
"""

sizex="12"
file_name="Structure_factor_"+sizex+"_"+sizex+"_"+sizex+"_theta"+Theta+".bin"
print(file_name)

FILE=np.loadtxt(file_name)
q1=FILE[:,0]
q2=FILE[:,1]

Spin_Structure_factor_hhl=FILE[:,2]
Spin_Structure_factor_hk0=FILE[:,3]

Structure_factor_hhl=FILE[:,4]
Structure_factor_hk0=FILE[:,5]

Q_size=12*4##int(input("Enter size of Q_array="))

Q1=np.reshape(q1,(Q_size,Q_size))
Q2=np.reshape(q2,(Q_size,Q_size))
q1=FILE[:,0]*2
q2=FILE[:,1]*2

'''
Eliminating the point at 0
'''
index_hhl=np.argmax(Structure_factor_hhl)
index_hk0=np.argmax(Structure_factor_hk0)

Structure_factor_hk0[index_hk0]=(Structure_factor_hk0[index_hk0-1]+Structure_factor_hk0[index_hk0+1])/2
Structure_factor_hhl[index_hhl]=(Structure_factor_hhl[index_hhl-1]+Structure_factor_hhl[index_hhl+1])/2
### Setting the value to the new max which corresponds to another Gamma point
Structure_factor_hk0[index_hk0]=np.max(Structure_factor_hk0)
Structure_factor_hhl[index_hhl]=np.max(Structure_factor_hhl)

Structure_factor_hhl= np.reshape(Structure_factor_hhl,(Q_size,Q_size))
Structure_factor_hk0= np.reshape(Structure_factor_hk0,(Q_size,Q_size))

Q1=Q1[1:,1:]*2
Q2=Q2[1:,1:]*2
Structure_factor_hhl= Structure_factor_hhl[1:,1:]
Structure_factor_hk0= Structure_factor_hk0[1:,1:]


Spin_Structure_factor_hhl= np.reshape(Spin_Structure_factor_hhl,(Q_size,Q_size))
Spin_Structure_factor_hk0= np.reshape(Spin_Structure_factor_hk0,(Q_size,Q_size))
Spin_Structure_factor_hhl= Spin_Structure_factor_hhl[1:,1:]
Spin_Structure_factor_hk0= Spin_Structure_factor_hk0[1:,1:]

t=3

plt.subplot(3,2,2*(t-1)+2)
input_name="SCGA_hk0_plane_"+str(t)+".txt"
x_label=r"$[h00]$"
y_label=r"$[0k0]$"
plt.gca().set_aspect('equal')

plt.pcolormesh(Q1,Q2,Spin_Structure_factor_hk0,cmap=CMAP,shading='auto')
plt.ylabel(y_label,size=label_size)

plt.yticks(size=label_size)
plt.title(r"$T=0^+ J_\chi$")
cbar=plt.colorbar(orientation="vertical",pad=0.1, shrink=Shrink)
cbar.ax.tick_params(labelsize=label_size)
#    plt.clim(min(Structure_factor_hk0.flatten()),max(Structure_factor_hk0.flatten()))
plt.clim(2,7)

plt.xticks([-2,0,2])
if(t==3):
    plt.xticks([-2,0,2])
#        plt.xticks(size=label_size)
plt.xlabel(x_label,size=label_size)

plt.xticks(size=label_size)
plt.yticks(size=label_size)


print(3,2,2*(t))
plt.subplot(3,2,2*(t-1)+1)

input_name="SCGA_hhl_plane_"+str(t)+".txt"
x_label=r"$[hh0]$"
y_label=r"$[00\ell]$"
plt.gca().set_aspect(1/np.sqrt(2))


plt.pcolormesh(Q1,Q2,Spin_Structure_factor_hhl,cmap=CMAP,shading='auto')

plt.ylabel(y_label,size=label_size)
plt.xticks([-2,0,2])
if(t==3):
    plt.xticks([-2,0,2])
   
plt.xlabel(x_label,size=label_size)
plt.xticks(size=label_size)
plt.yticks(size=label_size)
plt.title(r"$T=0^+J_\chi$")
cbar=plt.colorbar(orientation="vertical",pad=0.1, shrink=Shrink)
cbar.ax.tick_params(labelsize=label_size)
plt.clim(2,7)



plt.show()
    


