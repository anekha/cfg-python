#temperature = input('What is the temperature?')
#is_freezing = float(temperature) <= 0.0
#print('The temperature is freezing: {}'.format(is_freezing))


#burger_price = input('What is the price of the burger?')
#low_price = float(burger_price) <= 10.0
#print('The burger is within budget: {}'.format(low_price))

price = input('How much is a burger?')
vegetarian = input('Is there a vegetarian option? (y/n)')
within_budget = float(price) <= 10
has_vegetarian = vegetarian == 'y'
is_good_choice = within_budget and has_vegetarian

if is_good_choice:
    print('This is a good choice')
if not is_good_choice:
    print('Probably not a good idea')

meal_price = float(input('How much did the meal cost?'))

discount_choice = input('Do you have a discount? y/n')
discount_applicable = discount_choice == 'y' and meal_price > 20
if discount_applicable:
    meal_price = meal_price* 0.9
    print('Discount Applied')
else:
    print('No discount')

print('Total cost: {}'.format(meal_price))
