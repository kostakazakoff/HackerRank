matrix1 = [[698, 750], [818, 870], [938, 1888]]
matrix2 = [[570, 660], [720, 930]]
result = []

for m1_row in matrix1:
    for m2_row in matrix2:
        start_period = max(m1_row[0], m2_row[0])
        end_period = min(m1_row[1], m2_row[1])
        intersection = start_period - end_period
        if intersection >= 30:
            result.append([start_period, end_period])

print(result)