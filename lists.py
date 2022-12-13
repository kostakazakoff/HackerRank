def execute(l: list, expression: str):
    a = None
    command, *arguments = expression.split()
    a = (int(x) for x in arguments) if arguments else ''
    if command == 'print':
        print(l)
        return
    commands = {
        'insert': l.insert,
        'print': print,
        'remove': l.remove,
        'append': l.append,
        'sort': l.sort,
        'pop': l.pop,
        'reverse': l.reverse
        }   
    commands[command](*a)


N = int(input())
the_list = []
for _ in range(N):
    execute(the_list, input())

