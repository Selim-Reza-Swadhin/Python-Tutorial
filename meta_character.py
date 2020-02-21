import re

# re->regular expression
# pattern = r"colo.r"  # . -> any character but no new line
# pattern = r"^colo.r"  # ^ -> start character
# pattern = r"colo.r$"  # $ -> end character
# pattern = r"^colo.r$"  # ^,$ -> start and end character
# pattern = r"a*"  # * -> 0 or more character
# pattern = r"a+"  # + -> 1 or more character but minimum 1 character
# pattern = r"col-?our"  # ? -> 0 or 1 character but maximum 1 character
pattern = r"a{1,3}$"  # {1,3}$ -> 1 to 3 character but maximum 3 character and not space before 3

# if re.match(pattern, "colour"):
# if re.match(pattern, "col-our"):
if re.match(pattern, "aaa"):
    print("Match")
else:
    print("Not match")
