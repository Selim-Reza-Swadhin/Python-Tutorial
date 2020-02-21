num1 = float(input("Enter your first number : "))
num2 = float(input("Enter your second number : "))
num3 = float(input("Enter your second number : "))

if num1 > num2 and num1 > num3:
    print("Number num1", num1)
elif num2 > num1 and num2 > num3:
    print("Number num2", num2)
else:
    print("Number num3", num3)
