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



size=15
Shrink=0.8
sizex="10"
Theta="0"
CMAP=matplotlib.colors.LinearSegmentedColormap.from_list("", ["midnightblue","royalblue","orange","red","darkred"])
#CMAP="terrain"#matplotlib.colors.LinearSegmentedColormap.from_list("", ["darkgreen","royalblue","yellow","red"])


'''
-------------------- Plotting program --------------------
'''



fig=plt.figure(figsize=(7,4))
plt.subplots_adjust(left=0.15, bottom=0.16, right=0.95, top=0.95, wspace=0.25, hspace=0.25)
size_labels=18

#Interaction=["0","1","2","10","inf"]
Interaction=["6","8","10"]
colors=["b","r","g","purple","gray"]
markers=["^","o",".","s","*"]

for i in range(len(Interaction)):

    interaction=Interaction[i]
    file_name="average_thermodynamic_data_L"+interaction+".txt"
    Temp_array=np.loadtxt(file_name)[:,0]
    E=np.loadtxt(file_name)[:,1]
    C=np.loadtxt(file_name)[:,2]


    label_interaction=r"$L=$"+interaction

    plt.semilogx(Temp_array,C,marker=markers[i],color=colors[i],label=label_interaction)
       
plt.grid()

plt.ylim(0,1.7)
plt.xlabel(r"$T/J_\chi $",size=size_labels)
plt.ylabel(r"$C/k_{\rm B} $",size=size_labels)
plt.legend(prop={'size': size_labels})
plt.tick_params(labelsize=size_labels)
plt.xlim(min(Temp_array),max(Temp_array))
plt.show()


for i in range(len(Interaction)):

    interaction=Interaction[i]
    file_name="average_thermodynamic_data_L"+interaction+".txt"
    Temp_array=np.loadtxt(file_name)[:,0]
    E=np.loadtxt(file_name)[:,1]
    C=np.loadtxt(file_name)[:,2]


    label_interaction=r"$L=$"+interaction
    plt.subplot(121)
    plt.semilogx(Temp_array,E,marker=markers[i],color=colors[i],label=label_interaction)
#    plt.ylim(0,1.7)
    plt.xlabel(r"$T/J_\chi $",size=size_labels)
    plt.ylabel(r"$E $",size=size_labels)
    plt.legend(prop={'size': size_labels})
    plt.tick_params(labelsize=size_labels)
    plt.xlim(min(Temp_array),max(Temp_array))
    plt.subplot(122)
    plt.semilogx(Temp_array,C,marker=markers[i],color=colors[i],label=label_interaction)
       
plt.grid()

plt.ylim(0,1.7)
plt.xlabel(r"$T/J_\chi $",size=size_labels)
plt.ylabel(r"$C/k_{\rm B} $",size=size_labels)
plt.legend(prop={'size': size_labels})
plt.tick_params(labelsize=size_labels)
plt.xlim(min(Temp_array),max(Temp_array))
plt.show()
