# simple python script to generate input data
#
import numpy as np

nx, ny, nr, nt = 32, 32, 101, 6

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
gflux=(np.random.rand(nx,ny,nt)-0.5)*1.e-4
writefield('geoq.bin',gflux)
