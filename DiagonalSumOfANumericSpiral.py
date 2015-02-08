## Ulam Spiral
## By Jackson and Kallan
from numpy import zeros,array
from time import clock

#the size of one edge of the array. I.E. the square root of the largest number in the spiral.
dimension =10

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
	b = clock()
	print(b-a)
	return(array)

def getDIags(a):
	b = []
	n = len(a[0])
	for i in range(n):
		b.append(a[i,i])
		b.append(a[i,n-i-1])
	return(b)

ns = numeric_spiral(1001)
diags = array(getDIags(ns))
print sum(diags)-1