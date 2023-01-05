number_of_marks, subject = [int(x) for x in input().split()]
marks = []

for _ in range(subject):
    marks.append([float(x) for x in input().split()])

marks = zip(*marks)
result = [sum(x)/len(x) for x in marks]

[print(f'{x:.1f}') for x in result]