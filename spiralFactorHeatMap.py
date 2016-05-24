from  __future__ import division
import math 

#a function that returns true if number is prime
def prime(number):

    # checks if number is 2
    if number ==2:
        return(True)

    #starting at 2
    i = 2

    while i< (math.sqrt(number)+1) :

        #if the remainder of number divided by i is 0 then i goes evenly in to number 
        if number%i == 0:
            return(False)
        i+=1
    #if number is not divisable by any i then it is prime
    return(True)

#this finds a pair of factors of number
def factor_pair(number):
    factor_pair = None

    i = 2

    # checks for factors of number
    while i< (math.sqrt(number)+1):

       #if number is evenly divisable by i then i is a factor
       if number%i == 0:
           
            # a factor pair of number
            factor_pair = ([i,int(number/i)])
            return(factor_pair)
        
       i +=1

    #if there are no factors of number
    if factor_pair == None:
        return(str(number)+' is prime!')
    
  
    return(factor_pair)
    

#finds the prime factors of number
def Prime_factors(number):

    #gets a factor pair of number
    factor =  factor_pair(number)

    #a is one of the factor pair and b is the other
    a = factor[0]
    b = factor[1]

    #an array to be populated with the prime factors of a number
    prime_factors = []

    #checks to see if number is prime itself
    if prime(number) and prime_factors == []:
        return([number])

    k = 0
    
    while k != number:
       

        # if a is prime append it to prime factors
        if prime(a):
            prime_factors.append(a)

        #if b is prime append it to prime factors
        if prime(b):
            prime_factors.append(b)

        #if both a and b are prime break out of the loop
        if (prime(a) and prime(b)):
            break

        #if a isnt prime find a factor pair of it 
        if not prime(a):
            factors = factor_pair(a)
            a = factors[0]
            b = factors[1]

        # if b isn't prime find a factor pair for b
        if not prime(b):
            factors = factor_pair(b)
            a = factors[0]
            b = factors[1]

        # check to see if all the prime factors multiplied together are number if they are loop ends
        k = 1
        for p in range(len(prime_factors)):
            k = k*prime_factors[p]
            
    return(prime_factors)



## Ulam Spiral
## By Jackson and Kallan
from numpy import zeros

#the size of one edge of the array. I.E. the square root of the largest number in the spiral.
dimension =10

def numeric_spiral(n):
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
	        #array[(i,j)] = len(Prime_factors(array[(i,j)]))
	        fork = 'ninja'
    return(array)

def gen_Ulam_data(dim):
	spiral       = numeric_spiral(dim)
	ulam_spiral  = erradicate_non_primes(spiral)
	return(ulam_spiral)




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
    set_cmap('jet')
    ax.imshow(Ulam_data, interpolation='nearest')
    show()
    #s("C:/Users/Jackson/Documents/GitHub/ulamSpiral/ulam.svg",dpi = 500)
    
ulam_data = gen_Ulam_data(100)
show_Ulam_spiral(ulam_data)