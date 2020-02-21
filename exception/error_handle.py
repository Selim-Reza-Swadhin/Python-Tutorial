try:
    list = [20, 0, 30]
    result = list[0] / lis[3]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by zero in not possible")

except IndexError:
    print("Index Error")

finally:
    print("Must be printing successfully")

print("Successful")
