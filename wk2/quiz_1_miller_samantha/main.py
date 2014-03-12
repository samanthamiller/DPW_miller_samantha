def calcArea(h,w):
	area = int(h)*int(w)
	shape = ''
	return area
	return shape
	if h==w:
		shape = 'square'
	else:
		shape = 'rectangle'
		
height = raw_input('Enter the height of the object: ')
width = raw_input('Enter the width of the object: ')		
area = calcArea(int(height),int(width))	
print 'The area of your  is ' +str(area)+ ' square feet.'

for i in range(100,1, -1):
	print str(i)+ ' Bottles of Beer on the Wall, ' +str(i)+ ' Bottles of Beer.. take one down and pass it around. Now you have ' +str(i)+ ' bottles of beer on the wall!'