string = list(input())

lowercase = sorted([x for x in string if x.islower()])
uperrcase = sorted([x for x in string if x.isupper()])
odds = sorted([x for x in string if x.isdigit() and int(x) % 2 != 0])
evens = sorted([x for x in string if x.isdigit() and int(x) % 2 == 0])

print(''.join((*lowercase, *uperrcase, *odds, *evens)))