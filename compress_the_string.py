from itertools import groupby

[print(tuple([len(list(v)), int(k)]), end=' ') for k, v in groupby(input())]