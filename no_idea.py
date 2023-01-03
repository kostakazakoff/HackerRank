n, m = [int(x) for x in input().split()]
target_elements = list(map(int, input().split()))
elements_dict = {}
happiness = 0

for el in target_elements:
    if el not in elements_dict:
        elements_dict[el] = 0
    elements_dict[el] += 1

A = map(int, input().split())
B = map(int, input().split())

for el in A:
    if el in elements_dict:
        happiness += elements_dict[el]
for el in B:
    if el in elements_dict:
        happiness -= elements_dict[el]

print(happiness)
