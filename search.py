import re

pattern = r"colour"

text1 = "My favourite colour is Red."

match = re.search(pattern, text1)

if match:
    print(match.start())  # index[c]=13 start
    print(match.end())  # index[r]=19 end
    print(match.span())  # index[c]=13 start and index[r]=19 end
