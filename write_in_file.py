# file = open("student.txt", "a")  # append mode
# file = open("student.txt", "w")  # create file or overwrite lines mode
file = open("create_file/hello.html", "w")  # create html file or overwrite lines mode

# print(file.write("\nZannat - Lecturer of Physics")) # 29 characters
# file.write("\nZannat - Lecturer of Physics")# warning
# print(file)

# file.write("\nZannat - Lecturer of Physics")
file.write("<h2>Hello Bangladesh</h2>")

file.close()
