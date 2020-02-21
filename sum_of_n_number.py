n = int(input("Enter int number : "))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Result = ", sum)

print("2+4+6+.....+n")
i = 2
while i <= n:
    sum += i
    i += 2
print("Result = ", sum)
