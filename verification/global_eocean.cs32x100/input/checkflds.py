# simple python script to check input data
#
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

import mds

import sys

nx, ny, nr, nt = 32, 32, 100, 6

# ------------------------------------------------------

def readfield(fname,fmt):
    print 'read from file: '+fname
    data = np.fromfile(fname,fmt)
    return data

def plotxy(phixy):

    cmax=np.max(phixy[:])
    cmin=np.min(phixy[:])

    plt.subplot(3,4, 3)
    plt.pcolormesh(phixy[:,4,:],vmax=cmax,vmin=cmin)
    plt.axis('equal')
    plt.axis('tight')
    plt.axis('off')

    plt.subplot(3,4, 4)
    plt.pcolormesh(phixy[:,5,:],vmax=cmax,vmin=cmin)
    plt.axis('equal')
    plt.axis('tight')
    plt.axis('off')

    plt.subplot(3,4, 6)
    plt.pcolormesh(phixy[:,2,:],vmax=cmax,vmin=cmin)
    plt.axis('equal')
    plt.axis('tight')
    plt.axis('off')

    plt.subplot(3,4, 7)
    plt.pcolormesh(phixy[:,3,:],vmax=cmax,vmin=cmin)
    plt.axis('equal')
    plt.axis('tight')
    plt.axis('off')

    plt.subplot(3,4, 9)
    plt.pcolormesh(phixy[:,0,:],vmax=cmax,vmin=cmin)
    plt.axis('equal')
    plt.axis('tight')
    plt.axis('off')

    plt.subplot(3,4,10)
    plt.pcolormesh(phixy[:,1,:],vmax=cmax,vmin=cmin)
    plt.axis('equal')
    plt.axis('tight')
    plt.axis('off')

    plt.subplot(3,4,12)
    plt.axis('equal')
    plt.axis('tight')
    plt.axis('off')
    plt.colorbar()

    plt.subplots_adjust(wspace=0, hspace=0)

# Generate geothemal heat flux file

# phi=readfield('bathy_Hmin50.bin','>f8')

# phi=readfield('geoq.bin','>f8')

# phi=readfield('../run/T.0000000001.data','>f4')

# print(stats.describe(phi))

# phixy=np.reshape(phi,(nx,nt,ny))

# phixyz=np.reshape(phi,(nx,nt,ny,nr))
# phixy=phixyz[:,:,:,0]

suff="0000117000"
klev=50
fldCode='T'

if len(sys.argv) > 1:
 suff="%10.10d"%(int(sys.argv[1]))
if len(sys.argv) > 2:
 klev=(int(sys.argv[2]))
if len(sys.argv) > 3:
 fldCode=sys.argv[3]

T=mds.rdmds("%s%s%s%s"%('../run/',fldCode,'.',suff))
A=mds.rdmds('../run/RAZ')

Txy=np.reshape(T[klev,:,:],(ny,nt,nx))
# Txy=np.reshape(A,(ny,nt,nx))
plt.figure(1); plt.clf()
plotxy(Txy)

phiBuf=np.zeros((ny,nx*nt))
phiXYave=np.zeros((nr))
Asum=np.sum(A)
for k in range(nr):
 phiBuf=T[k,:,:]*A
 phiSum=np.sum(phiBuf)
 phiXYave[k]=phiSum/Asum
 

plt.figure(2); plt.clf()
plt.plot(phiXYave,-1000*(np.arange(nr)))

plt.show()
