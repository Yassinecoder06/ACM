from math import ceil

n = int(input())
m = int(input())
names = [input() for _ in range(m)]

def main():
    if m > n:
        return names[n-1]
    
    count = 0
    step = 1

    while True:
        round_size = step * m
        if count + round_size >= n:
            position = n - count
            index = (position - 1) // step
            return names[index]
        count += round_size
        step = step * 2

print(main())
