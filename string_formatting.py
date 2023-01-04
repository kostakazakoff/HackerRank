def print_formatted(number):
    width = number.bit_length()
    for i in range(1, number + 1):   
        print(f'{i:{width}} {i:{width}o} {i:{width}X} {i:{width}b}')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
