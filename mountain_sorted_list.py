def check_mountain_sort(the_list):

    if len(the_list) < 3:
        return False

    max_num = max(the_list)
    slice_index = the_list.index(max_num)

    if(slice_index == 0 or slice_index == len(the_list)-1):
        return False

    left = the_list[:slice_index]
    right = the_list[slice_index:]

    left_is_ok = left == sorted(left) and len(left) == len(set(left))
    right_is_ok = right == sorted(right, reverse=True) and len(right) == len(set(right))

    if (not all([left_is_ok, right_is_ok])):
        return False

    return True


print(check_mountain_sort([1, 3, 4, 2]))
