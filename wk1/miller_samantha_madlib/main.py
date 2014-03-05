'''
Samantha Miller
March 4, 2014
Madlib
'''

first_friend = raw_input('Please enter the first friends name: ')
second_friend = raw_input('Please enter the second friends name: ')
third_friend = raw_input('Please enter the third friends name: ')

first_money = input('Amount of money first friend has: ')
second_money = input('Amount of money second friend has: ')
third_money = input('Amount of money third friend has: ')

def group_amount(a1, a2, a3):
	group_total = a1 + a2 + a3
	return group_total
group_amount(first_money, second_money, third_money)


menu_dict = dict()
menu_dict = {'large cheese pizza': 10.50, 'large cheese stuffed crust pizza': 13.50, 'large meat lovers stuffed crust pizza': 15.50}
print menu_dict


group_dict = dict()
group_dict = {first_friend:first_money, second_friend:second_money, third_friend:third_money}


