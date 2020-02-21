try:
    num1 = int(input("Enter First number : "))
    num2 = int(input("Enter Second number : "))
    result = num1 / num2
    print(result)

# except ValueError:
#     print("You have to insert only integer.")
# except ZeroDivisionError:
#     print("You can not divide a number by 0")
except (ValueError, ZeroDivisionError):
    print("You have entered incorrect input.")

finally:
    print("Thanks...")


