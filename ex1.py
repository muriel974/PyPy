x,y = 1,2
def f ():
	x,y = 3,4
	print 'f (): x=%d, y=%d' % (x,y)
	z = 5

def g ():
	x = 6
	f()
	print 'g (): x=%d , y=%d' % (x,y)

y = 7
f()
print '__main__ : x=%d, y=%d' % (x,y)
x = 8
g()
print 'g()x=%d, y=%d' % (x,y)
