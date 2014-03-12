def calcArea(h,w):
	area = int(h)*int(w)
	return area
	if h==w:
		shape = 'square'
		return shape
	else:
		shape = 'rectangle'
		return shape
h = int(raw_input('Enter the height of the object: '))
w = int(raw_input('Enter the width of the object: '))		
area = calcArea(h,w)	
print 'The area of your  is ' +int(area)+ ' square feet.'