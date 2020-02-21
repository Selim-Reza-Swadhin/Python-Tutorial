import re

pattern = r"colour"

text1 = "colour My favourite colour is Red. I love blue colour as well."

if re.match(pattern, text1):
    print("Matched")
else:
    print("Not Matched")

print("Search function")
pattern = r"colour"

text1 = "My favourite colour is Red. I love blue colour as well."

if re.search(pattern, text1):
    print("Matched")
else:
    print("Not Matched")

print("FindAll function")
pattern = r"colour"

text1 = "My favourite colour is Red. I love blue colour as well."

if re.findall(pattern, text1):
    print("Matched")
else:
    print("Not Matched")

print(re.findall(pattern, text1))
