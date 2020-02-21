marks = int(input("Enter your Number : "))

if marks >= 80 and marks <= 100:
    print("A+")
elif marks >= 70 and marks <= 79:
    print("A")

# chained
if 80 <= marks <= 100:
    print("A+")
elif 10 <= marks <= 32:
    print("Fail")
