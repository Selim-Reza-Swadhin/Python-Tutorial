import re

# pattern = r"[aeiou]"
# pattern = r"[A-Z]"
# pattern = r"[A-Z][a-z]"
pattern = r"[A-Z][a-z][0-9]"

# if re.match(pattern, "azsdfghj"):
# if re.match(pattern, "Azsdfghj"): # start capital letter
# if re.match(pattern, "Azsdfghj"): # start capital to small letter
if re.match(pattern, "Az0sdfghj"): # start capital, small to numeric letter
    print("Match")
else:
    print("Not match")
