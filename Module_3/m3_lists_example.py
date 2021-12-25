# Let's take 3 lists. one with multi-assignment

cars_1 = cars_3 = ['Ford', 'Audi', 'BMW']
cars_2 = ['Ford', 'Audi', 'BMW']

# Sort all of them one by one

cars_1.sort()
cars_2.sort()
cars_3.sort()

# Check that all of them are visually equal

print(f"This is 1st: {cars_1}")
print(f"This is 2nd: {cars_2}")
print(f"This is 3rd: {cars_3}")

# Let's compare them in pairs

print(f"1st pair result is {cars_1 == cars_2}")
print(f"2st pair result is {cars_2 == cars_3}")

# OK, what will Identity check show?

print(f"1st pair result is {cars_1 is cars_2}")
print(f"2st pair result is {cars_2 is cars_3}")

# Let's additionally check 1st and 2nd list

print(f"3st pair result is {cars_1 is cars_3}")

# Why? Let's check id's of each list:

print(f"list 1: {hex(id(cars_1))}")
print(f"list 2: {hex(id(cars_2))}")
print(f"list 3: {hex(id(cars_3))}")

# one more trick
# Let's append list 3 and check list 1
cars_3.append('Opel')
print(f"output of list 1 {cars_1}")
print(f"one more check for l1 and l3 and it's {cars_1 is cars_3}")

# We need one more copy of list?
cars_4 = cars_3

# Let's check it with list 1
print(f"Result for car_1 and car_4 lists {cars_1 is cars_4}")

# Separate list

cars_5 = cars_3.copy()
print(f"car_5 vs car_1: {cars_1 is cars_5}")
