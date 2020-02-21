n = int(input("Enter your n number : "))

sum = 0
# range(start,end,difference)
for x in range(1, n + 1, 1):
    sum += x
print("1+2+3+4+.......+n = ", sum)

# range(start,end,difference)
for x in range(1, n + 1, 2):
    sum += x
print("1+3+5+7+.......+n = ", sum)

# range(start,end,difference)
for x in range(2, n + 1, 3):
    sum += x
print("2+5+8+11+.......+n = ", sum)

# range(start,end,difference)
for x in range(1, n + 1, 1):
    sum += x * x
print("1^2+2^2+3^2+4^2+.......+n^2 = ", sum)

# range(start,end,difference)
for x in range(2, n + 1, 2):
    sum += x * x
print("2^2+4^2+6^2+8^2+.......+n^2 = ", sum)
