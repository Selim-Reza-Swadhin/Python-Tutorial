n = int(input("Enter your n number : "))

sum = 1
# range(start,end,difference)
for x in range(1, n + 1, 1):
    sum *= x
print("1X2X3X4X.......Xn = ", sum)


for x in range(2, n + 1, 2):
    sum *= x
print("2X4X6X.......Xn = ", sum)


for x in range(1, n + 1, 2):
    sum *= x
print("1X3X5X.......Xn = ", sum)
