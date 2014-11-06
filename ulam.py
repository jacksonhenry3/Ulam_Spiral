## Ulam Spiral
## By Jackson and Kallan
from numpy import zeros
from time import clock

#the size of one edge of the array. I.E. the square root of the largest number in the spiral.
dimension =500

def numeric_spiral(n):
        a = clock()
	array     = zeros((n,n),dtype=int)
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
	if x==1:
		return True
	if x>=2:
		for i in range(2,x):
			if x!=i:
				if x%i==0:
					return True

def erradicate_non_primes(array):
    """
    replaces all non-primes in a 2d array with zeros
    """
    r = array[0]
    n = len(r)
    for i in range(n):
	for j in range(n):
		if not_prime(array[(i,j)])==True:
			array[(i,j)] = 0
		else:
		    array[(i,j)] = 1

def erradicate_non_primes(array):
    """
    replaces all non-primes in a 2d array with zeros
    """
    r = array[0]
    n = len(r)
    for i in range(n):
		for j in range(n):
				array[(i,j)] = array[(i,j)]%50

def gen_Ulam_data(dim):
	spiral       = numeric_spiral(dim)
	erradicate_non_primes(spiral)
	return(spiral)




def show_Ulam_spiral(Ulam_data):
    """
        Plots the Ulam spiral and saves it. Depends on matplotlib.pyplot
    """
    from matplotlib.pyplot import set_cmap,savefig,figure,Axes,show

    
    fig = figure()
    fig.set_size_inches(6, 6)
    ax = Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    # set_cmap('binary')
    ax.imshow(Ulam_data, interpolation='nearest')
    show()
    # savefig("ulam1.svg",dpi = 500)
    
ulam_data = gen_Ulam_data(dimension)
show_Ulam_spiral(ulam_data)