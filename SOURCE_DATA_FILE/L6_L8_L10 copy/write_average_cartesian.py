import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

#matplotlib.rcParams['text.usetex'] = True
#matplotlib.rcParams['text.latex.preamble'] = [
#    r'\usepackage{amsmath}',r'\usepackage{amssymb}',r'\usepackage{bm}']
#


'''
Parameters of the averaged runs
'''

sizex=input("Enter size of x=")#input("Enter the size of the lattice=")
sizey=sizex
sizez=sizex
label_size=18
Theta=input("Enter the value of theta with sign=")
N=50#int(input("Number of temperature points="))

'''
Arrays for the average thermodynamic quantities
'''
T=np.zeros(N)
E=np.zeros(N)
C_v=np.zeros(N)
M=np.zeros(N)
M2=np.zeros(N)
M_A2=np.zeros(N)

#M_E=np.zeros(N)
#M_E6=np.zeros(N)
#
#
#M_T1_planar=np.zeros(N)#15
#M_tot=np.zeros(N)
#
#M_ICE=np.zeros(N)
#M_T1_xy=np.zeros(N)
#
#M_T2=np.zeros(N)#18
#
#M_local_zz=np.zeros(N)#18





label=["-0.001","-0.01","-0.02","-0.05","-0.1"]
col=["k","r","g","b","violet"]

file_name_out_put="average_thermodynamic_data_L"+sizex+".txt"

'''
-------------------------------- Reading file --------------------------------
'''

my_file = Path(file_name_out_put)

if my_file.is_file():

    FILE=np.loadtxt(file_name_out_put)
    T=FILE[:,0]
    E=FILE[:,1]
    C_v=FILE[:,2]
    M=FILE[:,3]
    M2=FILE[:,4]
#    M_A2=FILE[:,5]
#    M_E=FILE[:,6]
#    M_E6=FILE[:,7]
#    M_tot=FILE[:,8]
#    M_T1_planar=FILE[:,9]
#    M_ICE=FILE[:,10]
#    M_T1_xy=FILE[:,11]
#    M_T2=FILE[:,12]
#    M_local_zz=FILE[:,13]
#    
    
    plt.figure(figsize=(12,5))

    plt.subplot(221)
    plt.semilogx(T,E,"^-")
    plt.xlabel("$ T/J $",size=15)
    plt.ylabel("Energy",size=15)
    plt.title("Energy per spin, "+sizex+"x"+sizey+"x"+sizez)
    for i in range(5):
        plt.axvline(T[i*10],color="red",linestyle="--")
    plt.grid()
    plt.subplot(222)
    plt.semilogx(T,C_v,"^-")
    plt.xlabel("$ T/J $",size=15)
    plt.ylabel("$ C_v $",size=15)
    plt.title("MC Specific heat, "+sizex+"x"+sizey+"x"+sizez)
    plt.grid()
    for i in range(5):
        plt.axvline(T[i*10],color="red",linestyle="--")
    plt.subplot(223)
    plt.semilogx(T,M,"^-")
    plt.xlabel("$ T/J $",size=15)
    plt.ylabel("$ m_s^2 $",size=15)
    plt.title(" Mean sublattice magnetization, "+sizex+"x"+sizey+"x"+sizez)
    plt.grid()
    plt.subplot(224)
    plt.loglog(T,(M2-M**2)/T,"^-")
    plt.xlabel("$ T/J $",size=15)
    plt.ylabel("$ \\chi/N $",size=15)
    plt.title(" Susceptibility, "+sizex+"x"+sizey+"x"+sizez)
    plt.grid()
    plt.show()

    plt.figure(figsize=(6,5))

    plt.subplot(211)
    plt.semilogx(T,E,"^-")
    plt.xlabel("$ T/J $",size=15)
    plt.ylabel("Energy",size=15)
    plt.title("Energy per spin, "+sizex+"x"+sizey+"x"+sizez)
    for i in range(5):
        plt.axvline(T[i*10],color="red",linestyle="--")
    plt.grid()
    plt.subplot(212)
    plt.loglog(T,C_v,"^-")
    plt.xlabel("$ T/J $",size=15)
    plt.ylabel("$ C_v $",size=15)
    plt.title("MC Specific heat, "+sizex+"x"+sizey+"x"+sizez)
    for i in range(5):
        plt.axvline(T[i*10],color="red",linestyle="--")
    plt.grid()

    plt.show()


    plt.figure(figsize=(6,5))

    plt.subplot(211)
    plt.semilogx(T,E,"b^-")
    plt.xlabel("$T/J_\chi$",size=label_size)
    plt.ylabel("$E/J_\chi$",size=label_size)
    plt.xlim(min(T),max(T))
    plt.grid()
    plt.tick_params(labelsize=label_size)
    plt.subplot(212)
    plt.semilogx(T,C_v,"b^-")
    plt.xlabel("$ T/J_\chi $",size=label_size)
    plt.ylabel("$ C/k_{\mathrm{B}} $",size=label_size)
    plt.xlim(min(T),max(T))
    plt.grid()
    plt.tick_params(labelsize=label_size)
    plt.show()


#    label_size=20
#    plt.semilogx(T,(3./2)*M_local_zz-1/2,"^-")
#    plt.axhline(0)
#    plt.axhline(1)
#    plt.xlabel(r"$ T/J $",size=label_size)
#    plt.ylabel(r"$ (3/2)P^z_{\rm local}-1/2 $",size=label_size)
#    plt.tick_params(labelsize=label_size)
#    plt.grid()
#    plt.ylim(0,1)
#    plt.xlim(min(T),max(T))
#    plt.show()
#    
#
#    label_size=20
#    plt.semilogx(T,M_local_zz,"^-")
#    plt.semilogx(T,np.ones(len(T))/3,"r--",label=r"$1/3$")
#    plt.axhline(1)
#    plt.xlabel(r"$ T/J $",size=label_size)
#    plt.ylabel(r"$ P^z_{\rm local} $",size=label_size)
#    plt.tick_params(labelsize=label_size)
#    plt.grid()
#    plt.legend(prop={'size': 12})
#    plt.xlim(min(T),max(T))
#    plt.show()
#
#
#    KB=1 #8.6E-2
#
#    plt.semilogx(T,M_A2,"x-",label=r"AIAO $M_{A_2}$ OP")
#    plt.semilogx(T,M_E,"o-",label=r"$\Gamma_5\ M_E$ OP")
#    plt.semilogx(T,M_tot,"o-",label=r"$ M_{\mathrm{Tot}}$ ")
#    plt.semilogx(T,M_T1_planar,".-",label=r" $M_{T_1}^{\mathrm{Planar}}$ OP")
#    plt.semilogx(T,M_ICE,".-",label=r" $M_{T_1}^{\mathrm{Ice}}$ OP")
#    plt.semilogx(T,M_T1_xy,".-",label=r" $M_{T_1}^{\mathrm{xy}}$ OP")
#    plt.semilogx(T,M_T2,"^-",label=r"$ M_{T_2}$ ")
#    plt.semilogx(T,T*0,"r--")
# 
#    plt.xlabel(" $ T/J $")
#    plt.ylabel(" $ O.P.s $")
#    plt.legend()
#    plt.show()
#    
#    plt.semilogx(T,M_A2,"x-",label=r"$M_{A_2}$ ")
#    plt.semilogx(T,M_E,"o-",label=r"$M_E$ ")
#    plt.semilogx(T,M_ICE,".-",label=r"$M_{T_1}^{\mathrm{Ice}}$")
#    plt.semilogx(T,M_T1_xy,".-",label=r" $M_{T_1}^{\mathrm{xy}}$ ")
#    plt.semilogx(T,M_T2,"^-",label=r"$M_{T_2}$ ")
#    plt.semilogx(T,T*0,"r--")
# 
#    plt.xlabel(" $ T/J $")
#    plt.ylabel(" $ |M_{I}| $")
#    plt.legend()
#    plt.show()
#    
#
#    plt.subplot(211)
#    plt.title(r"$\theta=$"+Theta)
#    plt.semilogx(T,M_E,"o-",label=r"$\Gamma_5\ M_E$ OP")
#    plt.legend()
#    plt.subplot(212)
#    plt.semilogx(T,M_E6,"o-",label=r"$\Gamma_5\ M_{E,6}$ OP")
#    plt.semilogx(T,np.zeros(len(T)),"r--")
#    plt.xlabel(" $ T/J $")
#    plt.legend()
#    plt.show()
#      
    
    '''
    -------------------------------- Printing file --------------------------------
    '''

else:

    max_sim_num=1000#int(input("Enter max number of sim number ="))+1
    print("Max number of simularions = %d" %max_sim_num)
    print("Including factor of \sqrt{3/2} in M_T1_planar ")
    num_average_simulations=0

    for sim_num in range(max_sim_num):

        file_name="Energy_"+sizex+"_"+sizey+"_"+sizez+"_theta"+Theta+"_sim_num_"+str(sim_num)+".txt"
        my_file = Path(file_name)

        if my_file.is_file():
            FILE=np.loadtxt(file_name)
            print("size of the file is ", FILE.shape)
            
            T+=FILE[:,0]
            E+=FILE[:,1]
            C_v+=FILE[:,2]
            M+=FILE[:,3]
            M2+=FILE[:,4]
#            M_A2+=FILE[:,5]
#            M_E+=FILE[:,6]
#            M_E6+=FILE[:,7]
#            M_tot+=FILE[:,8]
#            M_T1_planar+=FILE[:,9]
#            M_ICE+=FILE[:,10]
#            M_T1_xy+=FILE[:,11]
#            M_T2+=FILE[:,12]
#            M_local_zz+=FILE[:,13]
#            
            num_average_simulations+=1

    if(num_average_simulations==0):
        print("number of runs averaged= %d" %num_average_simulations)
        quit()
    
    '''
    Averaging configurations
    '''
    T/=num_average_simulations
    E/=num_average_simulations
    C_v/=num_average_simulations
    M/=num_average_simulations
    M2/=num_average_simulations
#    M_A2/=num_average_simulations
#    M_ICE/=num_average_simulations
#    M_E/=num_average_simulations
#    M_E6/=num_average_simulations
#    M_tot/=num_average_simulations
#
#    M_T1_planar/=num_average_simulations
#    M_T1_xy/=num_average_simulations
#    M_local_zz/=num_average_simulations
#    M_T2/=num_average_simulations

    print("Writing data to "+file_name_out_put)
    print("Number of simulations found=%d" %num_average_simulations)
    FILE=open(file_name_out_put,"w")

    for i in range(len(T)):
        FILE.write(str(T[i])+" "
                    +str(E[i])+" "
                    +str(C_v[i])+" "
                    +str(M[i])+" "
                    +str(M2[i])+" "
#                    +str(M_A2[i])+" "
#                    +str(M_E[i])+" "
#                    +str(M_E6[i])+" "
#                    +str(M_tot[i])+" "
#                    +str(M_T1_planar[i])+" "
#                    +str(M_ICE[i])+" "
#                    +str(M_T1_xy[i])+" "
#                    +str(M_T2[i])+" "
#            +str(M_local_zz[i])+" "
                    +"\n")
                    
    FILE.close()
