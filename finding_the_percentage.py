def student_average(name, **students):
    numbers = students[name]
    return f'{sum(numbers) / len(numbers):.2f}'

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    print(student_average(query_name, **student_marks))