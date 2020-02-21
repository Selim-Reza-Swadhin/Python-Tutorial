num = [1, 2, 3, 4, 5]

print("map function")
# map(fnc, iteral)
list_convert = map(lambda x: x * x, num)
result = list(list_convert)
print(result)

print("list Comprehensions")
# [expression for item in list]
result = [x * x for x in num]
print(result)

print("filter function")
result = list(filter(lambda x: x % 2 == 0, num))
print(result)

print("list Comprehensions")
# [expression for item in list if expression % 2 == 0]
result = [x for x in num if x % 2 == 0]
print(result)
