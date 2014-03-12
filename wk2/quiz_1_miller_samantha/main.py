def calcArea(h,w):
	area = h*w
	return area
	if h==w:
		shape = 'square'
		return shape
	else:
		shape = 'rectangle'
		return shape
h = raw_input('Enter the height of the object: ')
w = raw_input('Enter the width of the object: ')		
calcArea(h,w)	
print 'The area of your  is ' +area+ ' square feet.'