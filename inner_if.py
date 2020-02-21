# marks = int(input("Enter your GPA number : "))
num1 = float(input("Enter your number : "))
num2 = float(input("Enter your number : "))
num3 = float(input("Enter your number : "))

"""
if marks > 80:
    if marks > 70:
        if marks > 60:
            print("Inner statement success")
"""
"""
if num1 > num2:
    if num1 > num3:
        print("Number num1 ",num1)
    else:
        print("Inner second statement not success")
else:
    print("Inner first statement not success")

"""

if num1 > num2:
    if num1 > num3:
        print("Number num1 ", num1)
    else:
        print("Number num3 ", num3)

# if num2 > num1:#or
else:
    if num2 > num3:
        print("Number num2 ", num2)
    else:
        print("Number num3 ", num3)
