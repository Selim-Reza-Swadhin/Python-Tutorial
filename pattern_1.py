n = int(input("Enter n number : "))


for x in range(n):
    print(x * "*")

for x in range(n + 1):
    print(x * "*")

for x in range(n + 1):
    print((2 * x - 1) * "*")
