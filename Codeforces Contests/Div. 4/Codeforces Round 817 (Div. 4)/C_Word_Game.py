from collections import Counter, defaultdict

t = int(input())

for _ in range(t):
    n = int(input())

    words = []
    occ = defaultdict(int)

    for _ in range(3):
        word = list(input().split())
        words.append(word)
        for i in range(n):
            occ[word[i]] += 1

    results = [0,0,0]
    
    for i in range(3):
        word = words[i]

        for j in range(n):
            if occ[word[j]] == 1:
                results[i] += 3
            else:
                results[i] += 3-occ[word[j]]

    results=map(str, results)
    print(' '.join(results))
    