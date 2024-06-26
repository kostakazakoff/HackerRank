import re


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

decoded = ''

for col in range(m):
    for row in range(n):
        decoded += matrix[row][col]

ptrn = re.compile(r'\b[^\w]+\b')
encoded = ' '.join(ptrn.split(decoded))

print(encoded)
