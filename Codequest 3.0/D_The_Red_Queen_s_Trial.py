import heapq

n, s, k = map(int, input().split())
p = list(map(int, input().split()))

heap = []  # max-heap using negative values
ans = 0

for x in p:
    if s >= x:
        s -= x
        heapq.heappush(heap, -x)
        ans += 1
    elif k > 0:
        # try to swap with biggest fought guard
        if heap and -heap[0] > x:
            biggest = -heapq.heappop(heap)
            s += biggest          # undo cost
            k -= 1                # crystal used on biggest
            s -= x                # fight current guard
            heapq.heappush(heap, -x)
            ans += 1
        else:
            # use crystal on current guard
            k -= 1
            ans += 1
    else:
        break

print(ans)

