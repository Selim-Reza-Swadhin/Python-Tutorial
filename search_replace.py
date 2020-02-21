import re

# re->regular expression
pattern = r"colour"  # r -> row line

text1 = "My favourite colour is Red. I love blue colour as well."

# sub(pattern, replace, string,count=n)

# text2 = re.sub(pattern, "color", text1)
text2 = re.sub(pattern, "color", text1, count=2)
print(text2)
