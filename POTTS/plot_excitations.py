import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pathlib import Path
from functions import *

'''
Input variables
'''
resp_iterative=0

Lx=int(input("Enter L of simulation="))
Ly=Lx
Lz=Lx

Lxyz=int(input("Enter L(max value L of simulation)="))
angle="0"#input("Enter angle=")
Lmu=4

T_index=input("Enter T index (0,10,20,30,40)=")

input_name="Data_structure_factor_"+str(Lx)+"_"+str(Lx)+"_"+str(Lx)+"_"+T_index+".bin";

if(resp_iterative):
    input_name="Data_structure_factor_"+str(Lx)+"_"+str(Lx)+"_"+str(Lx)+".bin";

File=np.loadtxt(input_name)

condition=0
resp_tet=int(input("Plot the solid tetrahedra: no (0) or yes(1):"))

if(resp_iterative==0):
  
    T_input_name="Energy_"+str(Lx)+"_"+str(Lx)+"_"+str(Lx)+".txt"
    my_file = Path(T_input_name)

    if my_file.is_file():
        T=np.loadtxt(T_input_name)[:,0]
        E=np.loadtxt(T_input_name)[:,1]
        
    else:
        print("File_name="+T_input_name)
        print("No file found for the potts model with Lx="+str(Lx)+" size")
        exit()
    
    
    print(T)
    
fig=plt.figure(figsize=(9,6))
ax=fig.gca(projection='3d')

repeated_up=[]
repeated_down=[]
chiral_breaking_up=[]
chiral_breaking_down=[]
excitation_found=0

chiral_configurations=[[0,1,2,3],[0,2,3,1],
                                  [0,3,1,2],
                                  [1,0,3,2],
                                  [1,2,0,3],
                                  [1,3,2,0],
                                  [2,0,1,3],
                                  [2,1,3,0],
                                  [2,3,0,1],
                                  [3,0,2,1],
                                  [3,1,0,2],
                                  [3,2,1,0]]
                                    
for i in range(0,1):
    config=i*0#400
    configuration=File[config,:]
  
    x_lat_pyro=[]
    y_lat_pyro=[]
    z_lat_pyro=[]
    
    x_lat_fcc=[]
    y_lat_fcc=[]
    z_lat_fcc=[]
    

    x_lat_color=[]
  
    dot_product=[]
    
    for i_1 in range(Lxyz):
        for j_1 in range(Lxyz):
            for k_1 in range(Lxyz):
            
                sublattice_sites_up=[]
                sublattice_sites_down=[]
                
                
                for mu_1 in range(Lmu):

                    pos=Lmu*Lxyz*Lxyz*i_1+Lmu*Lxyz*j_1+Lmu*k_1+mu_1
                    
                    color_ijkmu=configuration[i_1*Lx*Ly*Lmu+j_1*Ly*Lmu+k_1*Lmu+mu_1]
                    sublattice_sites_up.append(color_ijkmu)
                   
                    rx=(i_1+j_1 )/2.
                    ry=(i_1+k_1 )/2.
                    rz=(j_1+k_1 )/2.

                    x_lat_fcc.append(rx)
                    y_lat_fcc.append(ry)
                    z_lat_fcc.append(rz)
                    
                    rx+=((mu_1==1)+(mu_1==2))/4.
                    ry+=((mu_1==1)+(mu_1==3))/4.
                    rz+=((mu_1==2)+(mu_1==3))/4.
                    
                    rx*=4;
                    ry*=4;
                    rz*=4;
                    
                    if(resp_tet):
                        plot_solid_tetrahedra(ax,[2*(i_1+j_1 ),2*(i_1+k_1 ),2*(j_1+k_1 )])
                    
                    x_lat_pyro.append(rx)
                    y_lat_pyro.append(ry)
                    z_lat_pyro.append(rz)
                    
#                    x_lat_color.append(color_ijkmu)
                    if(color_ijkmu==0):
                        x_lat_color.append("r")
                    elif(color_ijkmu==1):
                        x_lat_color.append("b")
                    elif(color_ijkmu==2):
                        x_lat_color.append("g")
                    elif(color_ijkmu==3):
                        x_lat_color.append("orange")
                    
                sublattice_sites_down.append(configuration[  i_1*Lx*Ly*Lmu+j_1*Ly*Lmu+k_1*Lmu+0 ] )
                sublattice_sites_down.append(configuration[ ((i_1-1+Lx)%Lx)*Lx*Ly*Lmu+j_1*Ly*Lmu+k_1*Lmu+1 ]  )
                sublattice_sites_down.append(configuration[i_1*Lx*Ly*Lmu+((j_1-1+Ly)%Ly)*Ly*Lmu+k_1*Lmu+2])
                sublattice_sites_down.append(configuration[i_1*Lx*Ly*Lmu+j_1*Ly*Lmu+((k_1-1+Lz)%Lz)*Lmu+3])
                
                if(len(set(sublattice_sites_up))!=4):
                    repeated_up.append([2*(i_1+j_1 ),2*(i_1+k_1 ),2*(j_1+k_1 )])
                    excitation_found=1
                    
                if(len(set(sublattice_sites_down))!=4):
                    repeated_down.append([2*(i_1+j_1 ),2*(i_1+k_1 ),2*(j_1+k_1 )])
                    excitation_found=1
               
                is_chiral_up=0
                is_chiral_down=0
                for i in range(12):

                    if((np.array(sublattice_sites_up)==np.array(chiral_configurations[i])).all()):
                        is_chiral_up=1
                       
                    if((np.array(sublattice_sites_down)==np.array(chiral_configurations[i])).all()):
                        is_chiral_down=1
                        
                        
                if(is_chiral_up==0):
                    chiral_breaking_up.append([2*(i_1+j_1 ),2*(i_1+k_1 ),2*(j_1+k_1 )])
                    excitation_found=1
                if(is_chiral_down==0):
                    chiral_breaking_down.append([2*(i_1+j_1 ),2*(i_1+k_1 ),2*(j_1+k_1 )])
                    excitation_found=1

                
        
    ax.scatter(x_lat_pyro,y_lat_pyro,z_lat_pyro,color=x_lat_color,s=30)
    
#    plt.legend()

    if(resp_iterative==0 and 0 ):
        plt.title(r"T=%.3f, E=%.3f" %(T[int(T_index)],E[int(T_index)]))
        
#    plt.show()
    
    ### Tetrahedra positions ###


#print(repeated_up)

x=np.array([0,1,0,0,1,1,1,0,1])
y=np.array([0,1,1,0,0,1,0,1,0])
z=np.array([0,0,1,0,1,0,1,1,1])

x_i=np.array([2,2,1,2,1,2,1,1,1])
y_i=np.array([-1,0,-1,-1,0,0,0,-1,-1])
z_i=np.array([1,2,2,1,1,2,1,2,2])

translation_x=np.ones(len(x))
translation_y=np.ones(len(y))
translation_z=np.ones(len(z))

###########################################################################
############################### Lattice ##############################
###########################################################################

x_direction=np.array([1,1,-1,-1])
y_direction=np.array([1,1,1,1])
z_direction=np.array([1,-1,-1,1])

x_pos=np.array([0,1,1,0])
y_pos=np.array([0,1,0,1])
z_pos=np.array([0,0,1,1])
move=np.ones(len(x_pos))


#fig=plt.figure(figsize=(9,9))
#ax=fig.gca(projection='3d')
Ni=Lxyz
Nj=Lxyz
Nk=Lxyz

points=10
x_line=np.linspace(0,Ni*2,points)
zeros=np.zeros(len(x_line))
ones=np.ones(len(x_line))
y_line=np.linspace(0,Nj*2,points)
z_line=np.linspace(0,Nk*2,points)

N_i=2*0
N_j=2*0
N_k=2*0
#N_i=2
#N_j=2
#N_k=2
#
X_cube=[0,2*N_i,2*N_i,0,0,0,2*N_i,2*N_i,0,0,2*N_i,2*N_i,2*N_i,2*N_i,0,0]#,0]
Y_cube=[0,0,2*N_j,2*N_j,0,0,0,2*N_j,2*N_j,0,0,0,2*N_j,2*N_j,2*N_j,2*N_j]#2*Nj]
Z_cube=[0,0,0,0,0,2*N_k,2*N_k,2*N_k,2*N_k,2*N_k,2*N_k,0,0,2*N_k,2*N_k,0]#,2*Nk]
#ax.plot(X_cube,Y_cube,Z_cube,linewidth=0.5,color="k")

if(N_i<Ni):
    for i in range(Ni-N_i):
        ax.plot(np.array(X_cube)+4*(i+1),np.array(Y_cube)+0,np.array(Z_cube)+0,linewidth=0.5,color="k")
        for j in range(Nj-N_j):
            ax.plot(np.array(X_cube)+4*(i+1),np.array(Y_cube)+4*(j+1),np.array(Z_cube)+0,linewidth=0.5,color="k")
            for k in range(Nk-N_k):
                ax.plot(np.array(X_cube)+4*(i+1),np.array(Y_cube)+0,np.array(Z_cube)+4*(k+1),linewidth=0.5,color="k")
if(N_j<Nj):
    for j in range(Nj-N_j):
        ax.plot(np.array(X_cube)+0,np.array(Y_cube)+4*(j+1),np.array(Z_cube)+0,linewidth=0.5,color="k")
        for i in range(Ni-N_i):
            ax.plot(np.array(X_cube)+4*(i+1),np.array(Y_cube)+4*(j+1),np.array(Z_cube)+0,linewidth=0.5,color="k")
            for k in range(Nk-N_k):
                ax.plot(np.array(X_cube)+0,np.array(Y_cube)+4*(j+1),np.array(Z_cube)+4*(k+1),linewidth=0.5,color="k")
        
if(N_k<Nk):
    for k in range(Nk-N_k):
        ax.plot(np.array(X_cube)+0,np.array(Y_cube)+0,np.array(Z_cube)+4*(k+1),linewidth=0.5,color="k")
        for i in range(Ni-N_i):
            ax.plot(np.array(X_cube)+4*(i+1),np.array(Y_cube)+0,np.array(Z_cube)+4*(k+1),linewidth=0.5,color="k")
            for j in range(Nj-N_j):
                ax.plot(np.array(X_cube)+4*(i+1),np.array(Y_cube)+4*(j+1),np.array(Z_cube)+4*(k+1),linewidth=0.5,color="k")
    
headlength=1
#ax.quiver([0],[0],[0],[2*Ni],[0],[0],color="red",length=0.2)
#ax.quiver([0],[0],[0],[0],[2*Nj],[0],color="blue",length=0.2)
#ax.quiver([0],[0],[0],[0],[0],[2*Nk],color="green",length=0.2)
#

linewidth=3
size_dots=0
upcolor="k"
downcolor="k"
resp_1=1


for i in range(len(repeated_up)):
    plot_solid_tetrahedra_up(ax,repeated_up[i])
    
for i in range(len(repeated_down)):
    plot_solid_tetrahedra_down(ax,repeated_down[i])



repeated_up=np.array(repeated_up)
repeated_down=np.array(repeated_down)

chiral_breaking_up=np.array(chiral_breaking_up)
chiral_breaking_down=np.array(chiral_breaking_down)

print("repeated up")
print(len(repeated_up))
print("repeated down")
print(len(repeated_down))
print("repeated chiral up")
print(len(chiral_breaking_up))
print("repeated chiral down")
print(len(chiral_breaking_down))

if (excitation_found and len(repeated_up)>0):
    ax.scatter(repeated_up[:,0]+.6,repeated_up[:,1]+.6,repeated_up[:,2]+.6,color="k",s=500)
    
if (excitation_found and len(repeated_down)>0 ):
    ax.scatter(repeated_down[:,0]-.6,repeated_down[:,1]-.6,repeated_down[:,2]-.6,color="k",s=500)

if (excitation_found and len(chiral_breaking_up)>0):
    ax.scatter(chiral_breaking_up[:,0]+.4,chiral_breaking_up[:,1]+.4,chiral_breaking_up[:,2]+.4,color="m",s=500)

if (excitation_found and len(chiral_breaking_down)>0):
    ax.scatter(chiral_breaking_down[:,0]-.4,chiral_breaking_down[:,1]-.4,chiral_breaking_down[:,2]-.4,color="m",s=500)



N_max=max(max(Ni,Nj),Nk)

ax.set_xlim(0,3*N_max)
ax.set_ylim(0,3*N_max)
ax.set_zlim(0,3*N_max)
#plt.legend(prop={'size': 15})
ax.set_xlabel("$ x $",size=20)
ax.set_ylabel("$ y $",size=20)
ax.set_zlabel("$ z $",size=20)
ax.set_axis_off()
ax.set_box_aspect((1,1,1))
plt.show()





