rows = int(input())
matrix = [input().split(',') for i in range(rows)]

rdiag = [matrix[i][i] for i in range(rows)]
ldiag = [matrix[i][-i-1] for i in range(rows)]

print(rdiag, ldiag)