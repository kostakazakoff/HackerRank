from itertools import combinations

length = int(input())
the_list = input().split()
idx_count = int(input())

all_comb = [x for x in combinations(the_list, idx_count)]
comb_with_a = [x for x in all_comb if 'a' in x]
result = len(comb_with_a) / len(all_comb)

print(f'{result:.3f}')
