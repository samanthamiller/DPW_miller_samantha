def calcArea(h,w):
	area = int(h)*int(w)
	return area
	if h==w:
		shape = 'square'
		return shape
	else:
		shape = 'rectangle'
		return shape
		
height = raw_input('Enter the height of the object: ')
width = raw_input('Enter the width of the object: ')		
area = calcArea(int(height),int(width))	
print 'The area of your  is ' +str(area)+ ' square feet.'

for i in range(1,100,1):