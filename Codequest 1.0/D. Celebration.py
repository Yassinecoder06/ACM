from math import ceil

t = int(input())
for _ in range(t):
    x,y,k = map(int, input().split())
    total_pieces_needed = y + k - 1

    print(ceil(total_pieces_needed/x))