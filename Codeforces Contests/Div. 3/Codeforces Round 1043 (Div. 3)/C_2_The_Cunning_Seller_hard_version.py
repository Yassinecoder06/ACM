t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    cnt = []
    total_deals = 0

    while n > 0:
        cnt.append(n % 3)
        n //= 3

    cnt.append(0)

    total_deals = sum(cnt)

    if total_deals > k:
        print(-1)
        continue

    k -= total_deals

    i = len(cnt) - 1

    
    while k > 0 and i > 0:
        if cnt[i] == 0:
            i -= 1
            continue

        take = min(cnt[i], k // 2)
        if take == 0:
            break

        cnt[i] -= take
        cnt[i - 1] += take * 3
        k -= take * 2

    ans = 0
    for i, v in enumerate(cnt):
        ans += v * (3**(i+1) + i * 3**(i-1) if i > 0 else 3)

    print(ans)