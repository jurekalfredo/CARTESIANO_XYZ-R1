

import numpy as np
from numpy import pi


def CD_robot(vq):

    q4n=-vq[3];


    d1n=vq[0]+212.66 ;
    d2n=vq[1]+167.510 +29.6;
    d3n=vq[2]+ 86.00;
    d4n=0;
    a0n=0;
    a1n=-145.41;
    a2n=0;
    a3n=0;
    T4r0=np.eye(4)
    T4r0[0,:]=[ np.sin(q4n),   np.cos(q4n), 0,  (a2n + a2n + d1n)*-1];
    T4r0[1,:]=[       0,        0,     -1,       (-d4n - d2n)*-1];
    T4r0[2,:]=[- np.cos(q4n),  np.sin(q4n), 0,  (a0n + a1n + d3n)*-1];
    T4r0[3,:]=[       0,        0,     0,               1];


    
    return T4r0        
