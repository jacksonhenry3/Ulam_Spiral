## Ulam Spiral
## By Jackson and Kallan
from numpy import array,zeros
def numeric_spiral(n):
	array     = zeros((n,n))
	direction = 'right'
	index1    = 0
	index2    = 0
	for i in range(n**2,0,-1):
		if direction =='right':
			try:
				if i != n**2:
					index2+=1
				if array[(index1,index2)] != 0:
					raise IndexError
				array[(index1,index2)] = i
			except IndexError:
				direction = 'down'
				index2    -=1


		if direction =='down':
			try:
				index1+=1
				if array[(index1,index2)] != 0:
					raise IndexError
				array[(index1,index2)] = i
				
			except IndexError:
				index1-=1
				direction = 'left'



		if direction =='left':
			try:
				index2-=1
				if array[(index1,index2)] != 0:
					raise IndexError
				array[(index1,index2)] = i
			except IndexError:
				index2+=1
				direction = 'up'



		if direction =='up':
			try:
				index1-=1
				if array[(index1,index2)] != 0:
					raise IndexError
				array[(index1,index2)] = i
			except IndexError:
				index1+=1
				direction = 'right'

				if direction =='right':
					try:
						if i != n**2:
							index2+=1
						if array[(index1,index2)] != 0:
							raise IndexError
						array[(index1,index2)] = i
					except IndexError:
						direction = 'down'
						index2-=1
	return(array)

def not_prime(x):
	x = int(x)
	if x==1:
		return True
	if x>=2:
		for i in range(2,x):
			if x!=i:
				if x%i==0:
					return True

def erradicate_non_primes(array):
	r = array[0]
	n = len(r)
	for i in range(n):
		for j in range(n):
			if not_prime(array[(i,j)])==True:
				array[(i,j)] = 0
	return(array)

def gen_Ulam_data(dim):
	sprial       = numericSpiral(dim)
	ulam_spiral  = erradicate_non_primes(Spiral)
	return(Spiral_prime)


# ----------------- program ends -----------------
	# experimental features
	# print(m)
	# import numpy as np
	# import numpy.random
	# import matplotlib.pyplot as plt

	# # Generate some test data
	# x = np.random.randn(8873)
	# y = np.random.randn(8873)
	# heatmap, xedges, yedges = np.histogram2d(x, y, bins=(dimension,dimension))
	# extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
	# plt.clf()
	# plt.imshow(heatmap, extent=extent)
	# plt.show()