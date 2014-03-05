'''
-----
Samantha Miller
March 4, 2014
Assignment Name
'''


'''
name = raw_input('Enter your name: ')
print name + ', very nice to meet you!'
'''

#single lined comment

#Expressions
'''
first = 'Samantha'
yearBorn = 1994
currentYear = 2014
age = currentYear - yearBorn
print age
'''

#Conditionals
'''
budget = 300
if budget > 200:
    #stuff we wanna do it true
    print 'You can buy a pair of Jordans'
elif budget > 30:
    print 'You can buy a pair of shoes from payless'
else:
    print 'No shoes for you'
'''

#Functions
'''
def calcArea(h,w):
    perimeter = 2*h + 2*w
    a = h*w
    return a

height = 40
width = 30
area = calcArea(height,width)
print 'Your area is ' + str(area)
'''

#Arrays
'''
students = ['Jairo', 'Austin', 'Samantha', 'Bryan', 'Lyte', 'Aurturo', 'Anthony','Mike','Ross']

#Dictionary - associative arrays
villains = dict()
villains = {'Star Wars':'Darth Vader', 'Lion King':'Scar', 'Hannah Montana': 'Miley Cyrus'}
print villains['Hannah Montana']
'''

#Loops