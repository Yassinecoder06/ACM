t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    found = False

    # Brute force all subsets of indices to remove (n <= 10).
    for mask in range(1 << n):
        removed_chars = []
        removed_indices = []
        remaining = []

        for i in range(n):
            if mask & (1 << i):
                removed_chars.append(s[i])
                removed_indices.append(i + 1)  # 1-based indices
            else:
                remaining.append(s[i])

        # Check if removed subsequence is non-decreasing.
        non_decreasing = True
        for i in range(len(removed_chars) - 1):
            if removed_chars[i] > removed_chars[i + 1]:
                non_decreasing = False
                break

        if not non_decreasing:
            continue

        # Check if remaining characters form a palindrome.
        if remaining == remaining[::-1]:
            print(len(removed_indices))
            if removed_indices:
                print(*removed_indices)
            else:
                print()
            found = True
            break

    if not found:
        print(-1)


