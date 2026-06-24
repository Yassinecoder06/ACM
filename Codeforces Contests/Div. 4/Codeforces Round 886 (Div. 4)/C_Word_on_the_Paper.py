t = int(input())

for _ in range(t):
    word = ''
    for _ in range(8):
        a = list(input())
        a.sort()
        if a[-1] != '.':
            word += a[-1]

    print(word)