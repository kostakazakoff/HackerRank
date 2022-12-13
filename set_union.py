number_of_students1 = int(input())
students1 = set([int(x) for x in input().split()])
number_of_students2 = int(input())
students2 = set([int(x) for x in input().split()])

print(len(students1|students2))

