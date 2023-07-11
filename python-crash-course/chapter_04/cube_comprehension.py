cubes = [value*value*value for value in range(1,11)]
print(cubes)

cubes2 = [value**3 for value in range(1,11)]
print(cubes2)

cubes3 = list(map(lambda value:value**3, range(1,11)))
print(cubes3)
