from struct import *
import numpy as np
# I considered using multiprocessing package, but I find this code version is fine.
# Welcome for your version with multiprocessing to make the reading faster.
# from joblib import Parallel, delayed
import multiprocessing
import time

start_time = time.time()
with open('YOU SHOULD PUT ONE VALID VOLUME BIN FILE HERE','r') as f:
	float_size = 4
	uint_size = 4
	total_count = 0
	cor = f.read(float_size*3)
	cors = unpack('fff', cor)
	print "cors is {}",cors
	cam = f.read(float_size*16)
	cams = unpack('ffffffffffffffff', cam)
	print "cams %16f",cams
	vox = f.read()
	numC = len(vox)/uint_size
	print 'numC is {}'.format(numC)
	checkVoxValIter = unpack('I'*numC, vox)
	checkVoxVal = checkVoxValIter[0::2]
	checkVoxIter = checkVoxValIter[1::2]
	checkVox = [i for (val, repeat) in zip(checkVoxVal,checkVoxIter) for i in np.tile(val, repeat)]
	print 'checkVox shape is {}'.format(len(checkVox))
	checkVox = np.reshape(checkVox, (240,144,240))
f.close()
print "reading voxel file takes {} mins".format((time.time()-start_time)/60)
