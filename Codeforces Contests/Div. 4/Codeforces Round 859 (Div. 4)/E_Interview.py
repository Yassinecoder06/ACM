import sys

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    prefix_normal = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_normal[i] = prefix_normal[i-1] + a[i-1]

    low = 1
    high = n

    while low < high:
        mid = (low + high) // 2
        
        count = mid - low + 1
        query_elements = " ".join(str(i) for i in range(low, mid + 1))
        
        print(f"? {count} {query_elements}", flush=True)
        output = int(sys.stdin.readline())

        expected_sum = prefix_normal[mid] - prefix_normal[low-1]

        if output > expected_sum:
            high = mid  
        else:
            low = mid + 1  

    print(f"! {low}", flush=True)
