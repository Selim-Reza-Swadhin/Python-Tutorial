def add(x, y):
    sum = x + y
    return sum


result = add(20, 10)
print("Return value = ", result)


def large(a, b):
    if a > b:
        return a
    else:
        return b


print("Large number = ", large(10, 20))

maximum = large  # large() function
print("Maximum number = ", maximum(2, 7))  # maximum variable function
