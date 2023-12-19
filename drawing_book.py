
def pageCount(n, p):
    left = int(p / 2)
    right = int(n / 2) - left
    return min(left, right)


if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
