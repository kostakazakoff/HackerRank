def merge_the_tools(string, k):
    substr_count = len(string) // k
    result = [''] * substr_count

    for n in range(k):
        idx = 0
        for i in range(n, len(string), k):
            if string[i] not in result[idx]:
                result[idx] += string[i]
            idx += 1
    [print(x) for x in result]

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)