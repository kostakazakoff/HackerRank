from itertools import product

# x, n = map(int, input().split())

# l = [list(map(lambda y: (int(y)**2)%n, input().split()))[1:] for i in range(x)]
# bestes = [sum(el)%n for el in product(*l)]
# print(max(bestes))


lists_count, M = [int(x) for x in input().split()]
max_nums = []

lst = [[int(x)**2 for x in (input().split())[1:]] for _ in range(lists_count)]

