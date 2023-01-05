import re


string = input()
substring = input()

ptrn = re.compile(substring)
match = ptrn.search(string)

if not match:
    print('(-1, -1)')

while match:
    print(f'({match.start()}, {match.end() - 1})')
    match = ptrn.search(string, match.start() + 1)
