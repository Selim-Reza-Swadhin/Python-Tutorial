# Lifo -> last in first out

books = []
books.append("C")
books.append("C++")
books.append("C#")

print(books)
print(books.pop())

print(books)
print(books[-1])

# print(books.pop())
# print(books.pop())

if not books:
    print("No books left")
