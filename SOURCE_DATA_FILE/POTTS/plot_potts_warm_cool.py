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

sizex="10"#input("Enter size of x=")#input("Enter the size of the lattice=")
sizey=sizex
sizez=sizex

fig=plt.figure(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.95, wspace=0.25, hspace=0.35)
size_labels=15

plt.subplot(211)

FILE=np.loadtxt("Energy_"+sizex+"_"+sizey+"_"+sizez+".txt")
T=FILE[:,0]
E=FILE[:,1]
Cv=FILE[:,2]

FILE=np.loadtxt("Energy_"+sizex+"_"+sizey+"_"+sizez+"_warm_up.txt")
Tw=FILE[:,0]
Ew=FILE[:,1]
Cvw=FILE[:,2]

plt.semilogx(Tw,Ew,"rs-",label="warm-up")
plt.semilogx(T,E,"b^-",label="cool-down")
plt.xlabel(r"$T/J_\chi $",size=size_labels)
plt.ylabel(r"$E/J_\chi $",size=size_labels)
plt.grid()
plt.xlim(min(T),max(T))
#plt.legend(prop={'size': size_labels})
plt.yticks([0,0.5,1,1.5])
plt.tick_params(labelsize=size_labels)
plt.legend()
plt.subplot(212)
plt.semilogx(Tw,Cvw,"rs-",label="warm-up")
plt.semilogx(T,Cv,"b^-",label="cool-down")
plt.xlabel(r"$ T/J_\chi $",size=15)
plt.ylabel(r"$ C/k_{B} $",size=15)
plt.xlim(min(T),max(T))
plt.grid()
#plt.yticks([0,0.1,0.2,0.3])
#plt.legend(prop={'size': size_labels})
plt.tick_params(labelsize=size_labels)
plt.legend(loc=2)
plt.show()


