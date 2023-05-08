string_length = int(input())
string_list = list(input())
number_of_queries = int(input())


def char_replacement(l_idx, r_idx, chr):
    for i in range(l_idx - 1, r_idx):
        string_list[i] = chr

def swap_fragments(l1, r1, l2, r2):
    global string_list
    first = string_list[l1-1:r1]
    second = string_list[l2-1:r2]
    string_list = string_list[:l1- 1] + second + string_list[r1:l2-1] + first + string_list[r2:]


def reverse_fragment(l_idx, r_idx):
    reversed_fragment = list(reversed(string_list[l_idx-1:r_idx]))
    string_list[l_idx-1:r_idx] = reversed_fragment


def write_fragment(l_idx, r_idx):
    print(''.join(string_list[l_idx-1:r_idx]))


def hamming_distance(l1, l2, fragment_length):
    h_distance = 0
    first_fragment = string_list[l1 - 1:l1 + fragment_length - 1]
    second_fragment = string_list[l2 - 1:l2 + fragment_length - 1]

    r = min(len(first_fragment), len(second_fragment))
    for i in range(r):
        if first_fragment[i] != second_fragment[i]:
            h_distance += 1

    print(h_distance)

extcute = {
    'C': char_replacement,
    'S': swap_fragments,
    'R': reverse_fragment,
    'W': write_fragment,
    'H': hamming_distance
}

for _ in range(number_of_queries):
    cmnd, *arguments = [int(x) if x.isdigit() else x for x in input().split()]
    extcute[cmnd](*arguments)
