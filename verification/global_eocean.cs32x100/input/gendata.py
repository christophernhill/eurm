# simple python script to generate input data
#
import numpy as np

nx, ny, nr, nt = 32, 32, 100, 6

# ------------------------------------------------------

def writefield(fname,data):
    import sys
    print 'write to file: '+fname
    if sys.byteorder == 'little': data.byteswap(True)
    fid = open(fname,"wb")
    data.tofile(fid)
    fid.close()

# Generate geothemal heat flux file
np.random.seed(1)
gflux=(np.random.rand(nx,ny,nt)-0.5)*1.e-6+0.1
writefield('geoq.bin',gflux)

# Generate RBCS to relax to zero at surface
mask=np.zeros((nr,nt,ny,nx))
mask[0,:,:,:]=1.
rvals=np.zeros((nr,nt,ny,nx))
writefield('rbcsthetamask.bin',mask)
writefield('rbcsthetavals.bin',rvals)
