#-----------------------------list--comprehensions--------------

numbers = [1,2,3,4,5]

evenNumbers = [x for x in numbers if x % 2 is 0]

oddNumbers = [y for y in numbers if y not in evenNumbers]

print(evenNumbers)
print(oddNumbers)