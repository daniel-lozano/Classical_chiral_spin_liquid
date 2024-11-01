import numpy as np 
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib
import matplotlib.colors
## These lines are needed to set the right font for the plots
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'

CMAP=matplotlib.colors.LinearSegmentedColormap.from_list("", ["midnightblue","royalblue","orange","red","darkred"])
#CMAP="terrain"#matplotlib.colors.LinearSegmentedColormap.from_list("", ["darkgreen","royalblue","yellow","red"])





def symmetrize_figure(matrix):
    return (matrix+matrix[:,::-1]+matrix[::-1,:]+matrix[::1,::-1]+matrix.T)/5
    
sizex=input("Enter size of x=")#input("Enter the size of the lattice=")
sizey=sizex
sizez=sizex

temp_index_array=["0","10","20","30","40"]
T_structure=np.loadtxt("average_thermodynamic_data_L10.txt")[:,0]
P_z=np.loadtxt("average_thermodynamic_data_L10.txt")[:,-1]
print(T_structure)
#exit()
Theta=input("Enter the value of theta with sign=")
max_sim_num=50
keyword=CMAP
resp_symm=0#int(input("Symmetrize data yes (1) or no (0):"))

for i_temp in range(len(temp_index_array)):
    file_name=file_name="Structure_factor_"+sizex+"_"+sizey+"_"+sizez+"_"+temp_index_array[i_temp]+"_theta"+Theta+".bin"

    my_file = Path(file_name)

    if my_file.is_file():

        FILE=np.loadtxt(file_name)
               
        q1=FILE[:,0]
        q2=FILE[:,1]

        Spin_Structure_factor_hhl=FILE[:,2]
        Spin_Structure_factor_hk0=FILE[:,3]

        Structure_factor_hhl=FILE[:,4]
        Structure_factor_hk0=FILE[:,5]

        Q_size=int(sizex)*4##int(input("Enter size of Q_array="))

        Q1=np.reshape(q1,(Q_size,Q_size))*2
        Q2=np.reshape(q2,(Q_size,Q_size))*2
        q1=FILE[:,0]*2
        q2=FILE[:,1]*2
        extent=(min(q1), max(q1), min(q2), max(q2))

        Spin_Structure_factor_hhl= np.reshape(Spin_Structure_factor_hhl,(Q_size,Q_size))
        Spin_Structure_factor_hk0= np.reshape(Spin_Structure_factor_hk0,(Q_size,Q_size))
        
        '''
        Eliminating the point at 0
        '''
        index_hhl=np.argmax(Structure_factor_hhl)
        index_hk0=np.argmax(Structure_factor_hk0)
#        print(index_hhl,index_hk0)
#        print(Structure_factor_hhl[index_hhl],Structure_factor_hk0[index_hk0])
#
        Structure_factor_hk0[index_hk0]=(Structure_factor_hk0[index_hk0-1]+Structure_factor_hk0[index_hk0+1])/2
        Structure_factor_hhl[index_hhl]=(Structure_factor_hhl[index_hhl-1]+Structure_factor_hhl[index_hhl+1])/2
        ### Setting the value to the new max which corresponds to another Gamma point
        print("Setting the value to the new max which corresponds to another Gamma point")
        Structure_factor_hk0[index_hk0]=np.max(Structure_factor_hk0)
        Structure_factor_hhl[index_hhl]=np.max(Structure_factor_hhl)
        
        Structure_factor_hhl= np.reshape(Structure_factor_hhl,(Q_size,Q_size))
        Structure_factor_hk0= np.reshape(Structure_factor_hk0,(Q_size,Q_size))
        
        
#        exit()
        ##Symmetryzing the matrices
        if(resp_symm):
            Spin_Structure_factor_hhl=symmetrize_figure(Spin_Structure_factor_hhl)
            Spin_Structure_factor_hk0=symmetrize_figure(Spin_Structure_factor_hk0)
            Structure_factor_hhl=symmetrize_figure(Structure_factor_hhl)
            Structure_factor_hk0=symmetrize_figure(Structure_factor_hk0)

        Shrink=0.6
        plt.figure(figsize=(15,5))
        plt.subplot(141)
        im1=plt.pcolormesh(Q1,Q2, Spin_Structure_factor_hhl,cmap=keyword ,shading='auto')
        plt.gca().set_aspect(1/np.sqrt(2))
        cbar=plt.colorbar(im1,orientation="vertical", shrink=Shrink)
        plt.xlabel("$ [hh0] $")
        plt.ylabel("$ [00\\ell] $")
        plt.title("$ |S(q)|^2\ T=%0.5f$" %T_structure[int(temp_index_array[i_temp])])

        plt.subplot(142)
        im1=plt.pcolormesh(Q1,Q2, Spin_Structure_factor_hk0,cmap=keyword,shading='auto')
        plt.gca().set_aspect('equal')
        cbar=plt.colorbar(im1,orientation="vertical",pad=0.1, shrink=Shrink)
        plt.xlabel("$ [h00] $")
        plt.ylabel("$ [0k0] $")
        plt.title("$ |S(q)|^2\ T=%0.5f$" %T_structure[int(temp_index_array[i_temp])])

        plt.subplot(143)
        im1=plt.pcolormesh(Q1,Q2, Structure_factor_hhl,cmap=keyword,shading='auto')
        plt.gca().set_aspect(1/np.sqrt(2))
        cbar=plt.colorbar(im1,orientation="vertical",pad=0.1, shrink=Shrink)
        plt.xlabel("$ [hh0] $")
        plt.ylabel("$ [00\\ell] $")
        plt.title("$ |S_{\\perp}(q)|^2\ T=%0.5f$" %T_structure[int(temp_index_array[i_temp])])
        plt.subplot(144)
        im1=plt.pcolormesh(Q1,Q2, Structure_factor_hk0,cmap=keyword,shading='auto')
        plt.gca().set_aspect('equal')
        cbar=plt.colorbar(im1,orientation="vertical",pad=0.1, shrink=Shrink)
        plt.xlabel("$ [h00] $")
        plt.ylabel("$ [0k0] $")
        plt.title("$ |S_{\\perp}(q)|^2\ T=%0.3f$" %T_structure[int(temp_index_array[i_temp])])
        print("P_zz=%.3f" %P_z[int(temp_index_array[i_temp])])
        plt.show()
