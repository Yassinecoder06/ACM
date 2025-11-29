n, limit = map(int, input().split())
fights = list(map(int, input().split()))


def can_fight(initial_bounty):
    b = initial_bounty
    for i in range(n):
        if b > fights[i]:
            b += 100
    return (b <= limit)

low, high = 0, limit

while low < high:
    mid = (low + high + 1) // 2
    if can_fight(mid):
        low = mid
    else:
        high = mid - 1

print(low)
