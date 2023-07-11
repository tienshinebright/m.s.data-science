cubes = list(map(lambda x:x**3, range(1,11)))
print(cubes)
for cube in cubes:
    print(cube)

cubes2 = [value**3 for value in range(1,11)]
print(cubes2)