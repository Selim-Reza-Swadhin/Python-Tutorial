num = [10, 20, 30, 40, 50]
print(num)

index = 0
"""
while index < 5:
    print(num[index])
    index += 1

"""

n = len(num)
while index < n:
    print(num[index])
    index += 1

print("For loop")
for x in num:
    print(x)

print("For loop sum")
sum = 0
for x in num:
    sum += x
print(sum)
