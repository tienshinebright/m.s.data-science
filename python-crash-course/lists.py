bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#Accessing element in a list
print(bicycles[0])

#Modifying Elements in a list
motorcycles = ['kawasaki', 'yamaha', 'honda']
motorcycles[2] = 'ducati'
print(motorcycles)

#Adding Elements to a list
motorcycles.append('suzuki')
print(motorcycles)

#Insert Elements into a list
motorcycles.insert(1, 'harley davidson')
print(motorcycles)

#Removing an item using the del
del motorcycles[2]
print(motorcycles)

#Removing an itme using the pop()
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print("This is a pop: ", popped_motorcycles)

#Popping Item from any position in a list
first_owned = motorcycles.pop(0)
print('This first motorcycle I owned was a ' + first_owned.title() + '.')

#Removing an item by value
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

#Organiing a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse = True)
print(cars)

#Sorting a list temporarilt with sorted() function
print('Here is the original list:')
print(sorted(cars))

#Reverse Order
cars.reverse()
print(cars)

#Finding the length of a list
print(len(cars))
















