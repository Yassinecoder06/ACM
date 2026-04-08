from math import ceil

n,k = map(int, input().split())
x = list(map(int, input().split()))

def can_divide(max_sum):
    subarrays = 1
    current_sum = 0
    
    for num in x:
        if current_sum + num > max_sum:
            subarrays += 1
            current_sum = num

            if current_sum > max_sum:
                return False
        else:
            current_sum += num

        if subarrays > k:
            return False

    return True

left = max(x)
right = sum(x)

while left < right:
    mid = (left + right) // 2

    if can_divide(mid):
        right = mid
    else:
        left = mid + 1

print(left)