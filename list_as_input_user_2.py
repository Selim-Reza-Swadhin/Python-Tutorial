numOfWords = 0
numOfLetters = 0
numOfDigits = 0

text = input("Enter a statements have text, number and space : ")  # My name is 123

for x in text:
    x = x.lower()
    # if x >= 'a' and x <= 'z':
    if 'a' <= x <= 'z':  # chained
        numOfLetters += 1
    # elif x >= '0' and x <= '9':
    elif '0' <= x <= '9':  # chained
        numOfDigits += 1
    elif x >= ' ':
        numOfWords += 1
print("The letters is : ", numOfLetters)
print("The digits is : ", numOfDigits)
print("The words is : ", numOfWords + 1)
