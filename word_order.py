n = int(input())
words = {}
for _ in range(n):
    word = input()
    if word not in words:
        words[word] = 0
    words[word] += 1

print(len(words))
print(*words.values())