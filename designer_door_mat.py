n, m = [int(x) for x in input().split()]
welcome = (m - 7)//2 * '-' + 'WELCOME' + (m - 7)//2 * '-'

def half_draw(start, end, step):
    for i in range(start, end, step):
        symbols = '.' + '|..' * i
        empty = (m//2 - len(symbols)) * '-'
        row = f'{empty}{symbols}|{symbols[::-1]}{empty}'
        print(row)

half_draw(0, n//2, 1)
print(welcome)
half_draw(n//2 - 1, -1, -1)
