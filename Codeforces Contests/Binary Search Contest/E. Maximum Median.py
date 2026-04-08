n, k = map(int, input().split())
a = sorted(map(int, input().split()))

middle = n//2
left = a[middle]
right = a[middle] + k

def can_achieve(target):
    operations_needed = 0

    for i in range(n//2, n):
        if a[i] < target:
            operations_needed += (target - a[i])
        if operations_needed > k:
            return False
    return operations_needed <= k

while left <= right:
    mid = (left + right) // 2
    if can_achieve(mid):
        left = mid + 1
    else:
        right = mid - 1

print(right) 