from collections import Counter


def is_sublist_with_duplicates(small, large):
    # Count frequencies of items in both lists
    count_small = Counter(small)
    count_large = Counter(large)

    # Check if large has at least enough of each item in small
    return all(count_large[item] >= count for item, count in count_small.items())


# Example Usage:
small = [1, 2, 2]
large = [2, 3, 1, 2, 4]

print(is_sublist_with_duplicates(small, large))  # Output: True
