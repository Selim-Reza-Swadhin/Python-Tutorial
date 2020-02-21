def add(x, y):
    sum = x + y
    print(sum)


def sub(x, y):
    sum = x - y
    print(sum)


def message():
    print("No parameter")


var_fnc = add  # add()
var_fnc(10, 20)  # var_fnc variable function

add(15, 30)
sub(15, 30)
message()
