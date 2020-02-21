num1 = float(input("Enter your number : "))
num2 = float(input("Enter your number : "))

if num1 > num2:
    print("Number num1", num1)
else:
    print("Number num2", num2)

print("Ternary")
max = num1 if num1 > num2 else num2
print("Maximun number",max)
print(num1 if num1 > num2 else num2)
