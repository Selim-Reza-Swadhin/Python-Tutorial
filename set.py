num1 = {1, 2, 3, 4, 5, 5, 4, 8}
print(num1)

num2 = set([1, 2, 3, 4, 5, 5, 4])
num2.add(7)
num2.remove(7)
print(num2)
print(7 in num2)
print(5 in num2)
print(5 not in num2)

# union
print(num1 | num2)

# intersection
num3 = set([4, 5, 6, 7])
print(num1 & num3)

# difference
print(num1 - num2)
