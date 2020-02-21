file = open("student.txt", "r")  # only read mode
# print(file.readable())

# text = file.read()
# print(text)

# size = len(text)
# print("Total characters = ", size)

# print(file.readline())  # single line
# print(file.readlines())  # list line
# index_line = file.readlines()[1]  # index line
# print(index_line)

for line in file:
    print(line)

# file = open("student.txt", "w")  # only write mode
# print(file.writable())

# file = open("student.txt", "r+")  # read and write mode
# print(file.readable())
# print(file.writable())


file.close()
