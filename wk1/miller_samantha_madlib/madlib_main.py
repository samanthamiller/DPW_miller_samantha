'''
Samantha Miller
March 4, 2014
Madlib
'''

# Asking first friend to input their name
first_friend = raw_input('Please enter the first friends name: ')
# Asking second friend to input their name
second_friend = raw_input('Please enter the second friends name: ')
# Asking third friend to input their name
third_friend = raw_input('Please enter the third friends name: ')

# friend_array holds the names of the people attending the pizza place together
friend_array = [first_friend, second_friend, third_friend]

# Loops through friend_array and prints which friends are going to the pizza place
for i in friend_array:	
	print i + ' is going to the pizza place.'

# Asking first friend to input the amount of money they have
first_money = input('Amount of money first friend has: ')
# Asking first friend to input the amount of money they have
second_money = input('Amount of money second friend has: ')
# Asking first friend to input the amount of money they have
third_money = input('Amount of money third friend has: ')


# Use a function to return the amount of money the group has collectivly 
def group_amount(a1, a2, a3):
	group_total = a1 + a2 + a3
	return group_total
# Set group_amount equal to the function with the parameters of the friends inputed money	
group_amount = group_amount(first_money, second_money, third_money)

# Use a function to return the amount of money that should be used for a tip based on groups collective money
def tip(group_total):
	tip_conversion = group_total / 3 
	tip_conversion * .20 
	return tip_conversion
# Pass group_amount into tip function to return amount the tips should be	
tip = tip(group_amount)	

# Set menu_dict equal to a dictonary
menu_dict = dict()
# Set menu_dict equal to a dictionary containing menu options and their prices
menu_dict = {'large cheese pizza': 10.50, 'large cheese stuffed crust pizza': 13.50, 'large meat lovers stuffed crust pizza': 15.50}

# Use menu_response as an empty array that the if statment will later push responses
menu_response = []


# Use if, elif and else to determin which types of food the group can order based on the amount of money they collectivly have and the price of the menu items
if group_amount >= menu_dict['large cheese pizza'] and group_amount >= menu_dict['large cheese stuffed crust pizza'] and group_amount >= menu_dict['large meat lovers stuffed crust pizza']:
	menu_response.append('You have enough money for a large cheese pizza, large cheese stuffed crust pizza or a large meat lovers stuffed crust pizza')
elif group_amount >= menu_dict['large cheese pizza'] and group_amount >= menu_dict['large cheese stuffed crust pizza']:
	menu_response.append('You have enough money for a large cheese pizza or large cheese stuffed crust pizza')
elif group_amount >= menu_dict['large cheese pizza']:
	menu_response.append('You have enough money for a large cheese pizza')
else:
	menu_response.append('Sorry you do not have enough money for anything at this pizzaria')

# Add message statment to combind information needed 
message = '''
	{first_friend}, {second_friend} and {third_friend} welcome to Samantha's Pizzaria. Collectively your group has ${group_amount}. {menu_response[0]}. Don't forget to leave a tip! A 20% tip for your groups meal is ${tip}! 
'''				 

# Formating the message 
message = message.format(**locals())
# Printing the message 
print message
