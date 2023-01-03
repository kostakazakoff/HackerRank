s = input()
s_dict = {}

for el in s:
    if el not in s_dict:
        s_dict[el] = 0
    s_dict[el] += 1

chars = sorted(s_dict.items(), key=lambda x: [-x[1], x[0]])[:3]
[print(*x) for x in chars]