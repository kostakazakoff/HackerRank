def minion_game(string):
    vowels = 'AEIOU'
    s_points = 0
    k_points = 0
    winner = None
    repeatings = len(string)

    for i in range(repeatings):
        points = repeatings - i
        if string[i] in vowels:
            k_points += points
        else:
            s_points += points
    repeatings -= 1
    
    if s_points > k_points:
        winner = 'Stuart'
    elif k_points > s_points:
        winner = 'Kevin'
    if winner:
        print(f'{winner} {max(s_points, k_points)}')
    else:
        print('Draw')

    
if __name__ == '__main__':
    s = input()
    minion_game(s)