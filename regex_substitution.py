import re

lines = []
output_list = []
N = int(input())
[lines.append(input()) for _ in range(N)]

def handle_string(string):
    string = string.group(0)
    if string == '&&':
        return 'and'
    else:
        return 'or'

for l in lines:
    if l.startswith('#'):
        output_list.append(l)
        continue
    output_list.append(re.sub(r'(?<= )&&(?= )|(?<= )\|\|(?= )', handle_string, l))

print(('\n').join(output_list))