requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    print("Adding " + topping + ".")

    if topping == 'green peppers':
        print("Sorry, we are not green peepers right now.")
    
    print("Finished making your pizza!\n")


empty_toppings = []
if empty_toppings:
    for topping in empty_toppings:
        print("Adding " + topping + ".")
    print("Finished making your pizza!\n")
else:
    print("Are you sure you want a plain pizza?\n")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
selected_toppings = ['mushrooms', 'pineapple', 'extra cheese', 'french fries']
for toppings in selected_toppings:
    if toppings in available_toppings:
        print("Adding " + toppings + ".")
    else:
        print("Sorry, we are not " + toppings + " right now.")
    print("Finished making your pizza!\n")