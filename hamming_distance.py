string_length = int(input())
string_list = list(input())
number_of_queries = int(input())

def char_replacement(l_idx, r_idx, chr):
    global string_list
    for i in range(l_idx, r_idx + 1):
        string_list[i] = chr

def swap_fragments(l1, r1, l2, r2):
    global string_list
    left = string_list[l1-1:r1]
    right = string_list[l2-1:r2]
    
    string_list[l1-1:r1] = right
    string_list[l2-1:r2] = left

    print(string_list)

def reverse_fragment(l_idx, r_idx):
    global string_list
    print(string_list)

def write_fragment(l_idx, r_idx):
    global string_list
    print(string_list)

def hamming_distance(l1, l2, fragment_length):
    global string_list
    print(string_list)

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
    