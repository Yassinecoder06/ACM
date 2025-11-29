t = int(input())
for _ in range(t):
    n = int(input())
    if n % 4 == 0:
        count_animals = n // 4
    else:
        count_animals = n // 4 + 1
    print(count_animals)
