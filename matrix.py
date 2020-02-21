matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matrix[0][2])

matrix[0][2] = 10
print(matrix[0][2])
print(matrix[1][2])

print("Start for loop")

for row in matrix:
    for col in row:
        print(col)
