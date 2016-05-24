# Conditional Spiral Vizualizations
# By Jackson Henry
from numpy import zeros,sin

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


def apply_condition(array,condition):
    r = array[0]
    n = len(r)
    for i in range(n):
	for j in range(n):
	        array[(i,j)] = condition(array[(i,j)])
    return(array)

def gen_spiral_data(dim,condition):
	spiral       = numeric_spiral(dim)
	ulam_spiral  = apply_condition(spiral,condition)
	return(ulam_spiral)




def show_spiral(data):
    from matplotlib.pyplot import imshow,show,figure,Axes,set_cmap
    
    #this is to remove plat axes
    fig = figure()
    fig.set_size_inches(6, 6)
    ax = Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    set_cmap('binary')
    #display plot
    ax.imshow(data, interpolation='nearest')
    show()
    
def largest_smallest_divisor(x):
    for i in range(2,x):
        if x%i ==0:
            return(i)
    return(1)
    
def s(x):
    return(5*sin(x/10))

def happy(n):
    visited = set()
    while 1:
        if n == 1:
            return(1)
            break
        n = sum(int(c) ** 2 for c in str(n))
        if n in visited:
            return(0)
            break
        visited.add(n)

data = gen_spiral_data(50,happy)
show_spiral(data)