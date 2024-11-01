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



label_size=18
Shrink=0.8
sizex="10"
Theta="0"
CMAP=matplotlib.colors.LinearSegmentedColormap.from_list("", ["midnightblue","royalblue","orange","red","darkred"])
#CMAP="terrain"#matplotlib.colors.LinearSegmentedColormap.from_list("", ["darkgreen","royalblue","yellow","red"])


'''
-------------------- Plotting program --------------------
'''


Temp_array_cool_down=np.loadtxt("average_thermodynamic_data_L10_cool_down.txt")[:,0]
E_cool_down=np.loadtxt("average_thermodynamic_data_L10_cool_down.txt")[:,1]
Cv_cool_down=np.loadtxt("average_thermodynamic_data_L10_cool_down.txt")[:,2]

Temp_array_warm_up=np.loadtxt("average_thermodynamic_data_L10_warm_up.txt")[:,0]
E_warm_up=np.loadtxt("average_thermodynamic_data_L10_warm_up.txt")[:,1]
Cv_warm_up=np.loadtxt("average_thermodynamic_data_L10_warm_up.txt")[:,2]


Temp_array_warm_up_kagome=np.loadtxt("average_thermodynamic_data_L10_warm_up_kagome.txt")[:,0]
E_warm_up_kagome=np.loadtxt("average_thermodynamic_data_L10_warm_up_kagome.txt")[:,1]
Cv_warm_up_kagome=np.loadtxt("average_thermodynamic_data_L10_warm_up_kagome.txt")[:,2]


fig=plt.figure(figsize=(6,4))
plt.subplots_adjust(left=0.15, bottom=0.15, right=0.95, top=0.95, wspace=0.25, hspace=0.25)
size_labels=15

plt.semilogx(Temp_array_warm_up,E_warm_up,"rs-",label="warm-up")
#plt.semilogx(Temp_array_warm_up_kagome,E_warm_up_kagome,"g.-",label=r"$\mathrm{warm\ up}\ \mathrm{Kagome}$")
plt.semilogx(Temp_array_cool_down,E_cool_down,"b^-",label=r"cool-down")
plt.grid()
plt.axhline(-1.5396,linestyle="--",color="k")
plt.xlim(min(Temp_array_warm_up),0.5)
plt.ylim(-1.55,-1)
plt.xlabel(r"$T/J_\chi $",size=size_labels)
plt.ylabel(r"$E/J_\chi $",size=size_labels)
plt.legend(prop={'size': size_labels})
plt.tick_params(labelsize=size_labels)
plt.show()

fig=plt.figure(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.95, wspace=0.25, hspace=0.35)
size_labels=15


plt.subplot(211)
plt.semilogx(Temp_array_warm_up,E_warm_up,"r^-",label=r"warm-up $\mathbf{k}=0$")
plt.semilogx(Temp_array_warm_up_kagome,E_warm_up_kagome,"g.-",label=r"warm-up $\mathrm{Kagome}$")
plt.semilogx(Temp_array_cool_down,E_cool_down,"bs-",label=r"cool-down")

plt.grid()
plt.axhline(-1.5396,linestyle="--",color="k")
plt.xlim(min(Temp_array_warm_up),min([max(Temp_array_warm_up),max(Temp_array_cool_down)]))#plt.ylim(-1.55,-1)
plt.xlabel(r"$T/J_\chi $",size=size_labels)
plt.ylabel(r"$E/J_\chi $",size=size_labels)
plt.legend(prop={'size': size_labels})
plt.tick_params(labelsize=size_labels)

plt.subplot(212)

plt.semilogx(Temp_array_warm_up,Cv_warm_up,"r^-",label=r"warm-up $\mathbf{k}=0$")
plt.semilogx(Temp_array_warm_up_kagome,Cv_warm_up_kagome,"g.-",label=r"warm-up $\mathrm{Kagome}$")
plt.semilogx(Temp_array_cool_down,Cv_cool_down,"bs-",label=r"cool-down")

plt.grid()
#plt.axhline(-1.5396,linestyle="--",color="k")
plt.xlim(min(Temp_array_warm_up),min([max(Temp_array_warm_up),max(Temp_array_cool_down)]))
#plt.ylim(-1.55,-1)
plt.xlabel(r"$T/J_\chi $",size=size_labels)
plt.ylabel(r"$C/k_{\mathrm{B}} $",size=size_labels)
plt.legend(prop={'size': size_labels})
plt.tick_params(labelsize=size_labels)
plt.show()

opacity=0.6

fig=plt.figure(figsize=(6,6))
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.95, wspace=0.25, hspace=0.35)
size_labels=15
plt.subplot(211)
#plt.semilogx(Temp_array_cool_down,E_cool_down,"bs-",label=r"$\mathrm{cool\ down}$")

plt.semilogx(Temp_array_warm_up,E_warm_up,"rs-",label=r"warm-up $ \mathbf{k}=0$",alpha=opacity)
plt.semilogx(Temp_array_warm_up_kagome,E_warm_up_kagome,"g.-",label=r"warm-up $ \mathrm{Kagome}$",alpha=opacity)
plt.semilogx(Temp_array_cool_down,E_cool_down,"b^-",label=r"cool-down",alpha=opacity)

plt.grid()
plt.axhline(-1.5396,linestyle="--",color="k")
plt.xlim(min(Temp_array_warm_up),min([max(Temp_array_warm_up),max(Temp_array_cool_down)]))#plt.ylim(-1.55,-1)
plt.xlabel(r"$T/J_\chi $",size=size_labels)
plt.ylabel(r"$E/J_\chi $",size=size_labels)
plt.legend(prop={'size': size_labels})
plt.tick_params(labelsize=size_labels)

plt.subplot(212)

#plt.loglog(Temp_array_cool_down,Cv_cool_down,"bs-",label=r"$\mathrm{cool\ down}$")
#plt.loglog(Temp_array_warm_up,Cv_warm_up,"r^-",label=r"$\mathrm{warm\ up}$")
#plt.loglog(Temp_array_cool_down,Cv_cool_down,"bs-",label=r"$\mathrm{cool\ down}$")
#plt.semilogx(Temp_array_cool_down_kagome,Cv_cool_down_kagome,"g.-",label=r"$\mathrm{cool\ down}\ \mathrm{Kagome}$")


plt.loglog(Temp_array_warm_up,Cv_warm_up,"rs-",label=r"warm-up $\mathbf{k}=0$",alpha=opacity)
plt.loglog(Temp_array_warm_up,Cv_warm_up_kagome,"g.-",label=r"warm-up $ \mathrm{Kagome}$",alpha=opacity)
plt.loglog(Temp_array_cool_down,Cv_cool_down,"b^-",label=r"cool-down",alpha=opacity)

plt.grid()
#plt.axhline(-1.5396,linestyle="--",color="k")
plt.xlim(min(Temp_array_warm_up),min([max(Temp_array_warm_up),max(Temp_array_cool_down)]))
plt.ylim(10**-1,15)
plt.xlabel(r"$T/J_\chi $",size=size_labels)
plt.ylabel(r"$C/k_{\mathrm{B}} $",size=size_labels)
plt.legend(prop={'size': size_labels})
plt.tick_params(labelsize=size_labels)
plt.show()


M_warm=np.loadtxt("average_thermodynamic_data_L10_warm_up.txt")[:,4]
M_warm_kagome=np.loadtxt("average_thermodynamic_data_L10_warm_up_kagome.txt")[:,4]
M_cool=np.loadtxt("average_thermodynamic_data_L10_cool_down.txt")[:,4]

fig=plt.figure(figsize=(6,3))
plt.subplots_adjust(left=0.15, bottom=0.2, right=0.95, top=0.95, wspace=0.25, hspace=0.25)
size_labels=15
plt.semilogx(Temp_array_warm_up,M_warm,"r^-",label=r"warm-up $\mathbf{k}=0$",alpha=opacity)
plt.semilogx(Temp_array_warm_up_kagome,M_warm_kagome,"g.-",label=r"warm-up $ \mathrm{Kagome}$",alpha=opacity)
plt.semilogx(Temp_array_cool_down,M_cool,"bs-",label=r"cool-down",alpha=opacity)
plt.xlim(min(Temp_array_warm_up),min([max(Temp_array_warm_up),max(Temp_array_cool_down)]))
plt.xlabel(r"$T/J_\chi $",size=size_labels)
plt.ylabel(r"$m_s^2$",size=size_labels)
plt.ylim(-0.1,1.2)
plt.tick_params(labelsize=size_labels)
plt.legend(prop={'size': size_labels})

plt.grid()
plt.show()


M_warm=np.loadtxt("average_thermodynamic_data_L10_warm_up.txt")[:,3]
M_warm_kagome=np.loadtxt("average_thermodynamic_data_L10_warm_up_kagome.txt")[:,3]
M_cool=np.loadtxt("average_thermodynamic_data_L10_cool_down.txt")[:,3]

fig=plt.figure(figsize=(6,2))
plt.subplots_adjust(left=0.15, bottom=0.15, right=0.95, top=0.95, wspace=0.25, hspace=0.25)
size_labels=15
plt.semilogx(Temp_array_warm_up,M_warm,"r^-",label=r"warm-up $ \mathbf{k}=0$")
plt.semilogx(Temp_array_warm_up,M_warm,"r^-",label=r"warm-up $ \mathrm{Kagome}$")

plt.semilogx(Temp_array_cool_down,M_cool,"bs-",label=r"cool-down")
plt.xlim(min(Temp_array_warm_up),min([max(Temp_array_warm_up),max(Temp_array_cool_down)]))
plt.xlabel(r"$T/J_\chi $",size=size_labels)
plt.ylabel(r"$M$",size=size_labels)
plt.tick_params(labelsize=size_labels)
plt.legend(prop={'size': size_labels})

plt.grid()
plt.show()
