pizzas = ['neapolitan pizza', 'chicago pizza', 'california pizza']
print(pizzas)
friend_pizzas = pizzas[:]
friend_pizzas.append('pepperoni pizza')
print(friend_pizzas)

for pizza in pizzas:
    print("My favorite pizza are: " + pizza)

for f_pizza in friend_pizzas:
    print("My friend's favorite pizzas are: " + f_pizza)

