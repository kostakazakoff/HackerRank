string_length = int(input())
chars_list = list(input())
number_of_queries = int(input())

def char_replacement(l_idx, r_idx, chr):
    for i in range(l_idx - 1, r_idx):
        chars_list[i] = chr

def swap_fragments(l1, r1, l2, r2):
    global chars_list
    first = chars_list[l1-1:r1]
    second = chars_list[l2-1:r2]
    chars_list = chars_list[:l1- 1] + second + chars_list[r1:l2-1] + first + chars_list[r2:]

def reverse_fragment(l_idx, r_idx):
    reversed_fragment = list(reversed(chars_list[l_idx-1:r_idx]))
    chars_list[l_idx-1:r_idx] = reversed_fragment

def write_fragment(l_idx, r_idx):
    print(''.join(chars_list[l_idx-1:r_idx]))

def hamming_distance(l1, l2, fragment_length):
    h_distance = 0
    first_fragment = chars_list[l1 - 1:l1 + fragment_length - 1]
    second_fragment = chars_list[l2 - 1:l2 + fragment_length - 1]

    r = min(len(first_fragment), len(second_fragment))
    chr_n = {'a': 1, 'b': 0}
    for i in range(r):
        h_distance += chr_n[first_fragment[i]]^chr_n[second_fragment[i]]
        # h_distance += len({first_fragment[i], second_fragment[i]}) - 1

    print(h_distance)

execute = {
    'C': char_replacement,
    'S': swap_fragments,
    'R': reverse_fragment,
    'W': write_fragment,
    'H': hamming_distance
}

for _ in range(number_of_queries):
    cmnd, *arguments = [int(x) if x.isdigit() else x for x in input().split()]
    execute[cmnd](*arguments)
