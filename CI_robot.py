import numpy as np
from numpy import pi


def CI_robot(vq):

    
    d1n=vq[0]+212.66 ;
    d2n=vq[1]+167.510 +29.6;
    d3n=vq[2]+ 86.00;
    d4n=0;
    a0n=0;
    a1n=-145.41;
    a2n=0;
    a3n=0;


    
    Px = (vq[0,3]+212.66)/-1
    Py = (vq[1,3]-167.510 -29.6)
    Pz = (vq[2,3]-145.41+86)/-1


    q2i=(np.arctan2(vq[0,0],vq[0,1]))/-1

    print('CINEMATICA INVERSA X: ',Px)
    print('CINEMATICA INVERSA Y: ',Py)
    print('CINEMATICA INVERSA Z: ',Pz)

    print('CINEMATICA INVERSA R1: ',q2i*180/pi)
    
