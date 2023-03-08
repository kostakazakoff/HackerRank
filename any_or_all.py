number_of_integers = int(input())
integers = [x for x in input().split()]

positive = all(map(lambda x: int(x) > 0, integers))
palindrome = any(map(lambda x: x == x[::-1], integers))

print(all((positive, palindrome)))