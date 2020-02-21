n = int(input("Enter any number : "))


def fact(n):
    if n == 1:  # base or condition
        return 1
    else:
        return n * fact(n - 1)


print("Factorial number is ", fact(n))
