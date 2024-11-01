# Classical_chiral_spin_liquid
Data for the publication "A Classical Chiral Spin Liquid from Chiral Interactions on the Pyrochlore Lattice"

The data provided in this repository can be visualized by simply running the python scripts included in the files. For some of the figures the python script must be run in the folder where the data file is located.

The data files included in this repository can be broadly classify in the following categories:
    
    1) average_thermodybamic_data_<additional_information>.txt :
        These files contain thermodynamic quantities that have been measured using a classical Monte-Carlo (cMC) algorithm and averaged between multiple independent cMC simulations. In general, the first three colums of these files correspond to the temperature, energy, and specific heat, respectively.
        
    2) Structure_factor_<additional_information>.bin    :
        These files contain the spin-spin and neutron structure factors in the HHL and HK0 reciprocal planes. Additional information of these can be found in the python files.
        
    3)  Energy_<additional_information>.txt :
        These files contain thermodynamic quantities that have been measured using a classical Monte Carlo algorithm for a single cMC simulation. In general, the first three colums of these files correspond to the temperature, energy, and specific heat, respectively.
        
    4) chiral_<additional_information>.bin :
        These files contain the numerically calculated chirality for every single triangle in a pyrochlore lattice at a certain temperature. 
        
    5) histrogram__<additional_information>.dat :
        These files contain the numerically calculated nearest-neighbor dot-product for every single triangle in a pyrochlore lattice at a certain temperature. 
