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

# Asking first friend to input the amount of money they have
first_money = input('Amount of money first friend has: ')
# Asking first friend to input the amount of money they have
second_money = input('Amount of money second friend has: ')
# Asking first friend to input the amount of money they have
third_money = input('Amount of money third friend has: ')

def group_amount(a1, a2, a3):
	group_total = a1 + a2 + a3
	return group_total
group_amount = group_amount(first_money, second_money, third_money)

def tip(group_total):
	tip_conversion = group_total / 3 
	tip_conversion * .20 
	return tip_conversion
tip(group_amount)	

menu_dict = dict()
menu_dict = {'large cheese pizza': 10.50, 'large cheese stuffed crust pizza': 13.50, 'large meat lovers stuffed crust pizza': 15.50}

menu_response = []

if group_amount >= menu_dict['large cheese pizza'] and group_amount >= menu_dict['large cheese stuffed crust pizza'] and group_amount >= menu_dict['large meat lovers stuffed crust pizza']:
	menu_response.append('You have enough money for a large cheese pizza, large cheese stuffed crust pizza or a large meat lovers stuffed crust pizza')
elif group_amount >= menu_dict['large cheese pizza'] and group_amount >= menu_dict['large cheese stuffed crust pizza']:
	menu_respons.append('You have enough money for a large cheese pizza or large cheese stuffed crust pizza.')
elif group_amount >= menu_dict['large cheese pizza']:
	menu_response.append('You have enough money for a large cheese pizza')
else:
	menu_response.append('You do not have enough money for anything at this pizzaria')

				 
	

