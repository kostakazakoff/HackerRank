if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    second_grade = sorted(list(set(x[1] for x in students)))[1]
    names = '\n'.join(list(sorted([x[0] for x in students if x[1] == second_grade])))

    print(names)