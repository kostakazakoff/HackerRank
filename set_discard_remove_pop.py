def execute_command(set_of_elements: set, command_params):
    commands = {'remove': set_of_elements.remove, 'discard': set_of_elements.discard}
    command, *element = command_params.split()
    element = int(element[0]) if element else None
    if command == 'pop' and set_of_elements:
        set_of_elements.pop()
    elif element in set_of_elements:
        commands[command](element)


if __name__ == '__main__':
    number_of_elements = int(input())
    elements = set(map(int, input().split()))
    number_of_commands = int(input())

    for _ in range(number_of_commands):
        command = input()
        execute_command(elements, command)
        print(elements)

    print(sum([x for x in elements]))
