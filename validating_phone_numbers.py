import re

pattern = r'^[789]\d{9}$'
N = int(input())

output = {
    True: 'YES',
    False: 'NO'
}

for _ in range(N):
    result = re.match(pattern, input()) != None
    print(output[result])