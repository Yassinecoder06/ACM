n, m = map(int, input().split())  # Reading n and m
a = list(map(int, input().split()))  # Reading the list of integers a
queries = []

# Collecting the queries
for _ in range(m):
    queries.append(int(input()))

distinct_count = [0] * n  # This will store the count of distinct elements from each index
seen = set()  # A set to track distinct elements as we iterate

# Fill the distinct_count array by iterating from the last element to the first
for i in range(n - 1, -1, -1):
    seen.add(a[i])
    distinct_count[i] = len(seen)

# Process each query and output the result
for l in queries:
    print(distinct_count[l - 1])  # Print the result for each query


