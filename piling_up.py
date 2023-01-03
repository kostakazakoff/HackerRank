from collections import deque


t = int(input())

for _ in range(t):
    result = 'Yes'
    number_of_qubes = int(input())
    qubes = deque(map(int, input().split()))
    pile_qube = max(qubes[0], qubes[-1])

    while qubes:
        if pile_qube >= qubes[0] > qubes[-1]:
            pile_qube = qubes[0]
            qubes.popleft()
        elif pile_qube >= qubes[-1]:
            pile_qube = qubes[-1]
            qubes.pop()
        else:
            result = 'No'
            break

    print(result)