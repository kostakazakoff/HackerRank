numbers = list(sorted(map(lambda x: int(x), input().split())))

min_sum = sum(numbers[:4])
max_sum = sum(numbers[-4:])

print(f'{min_sum} {max_sum}')