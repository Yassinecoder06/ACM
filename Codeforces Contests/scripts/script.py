import re

text = """
Editorial for Contest 2148
This is a sample text representing an editorial.
Length: 1000 characters.

Problem A: Simple Task
Solution for A involves a basic loop.

Problem B: Complex Math
Solution for B is a dynamic programming approach.

Problem C: Graph Problem
Solution for C uses Dijkstra's algorithm.

First 40 lines of simulated text...
"""

print(f'Tutorial Link: https://codeforces.com/blog/entry/mock_2148')
print(f'Editorial Length: {len(text)}')
print('First 40 lines (non-empty):')
lines = [l.strip() for l in text.splitlines() if l.strip()]
for line in lines[:40]:
    print(line)

found_a = bool(re.search(r'\bA\b', text))
found_b = bool(re.search(r'\bB\b', text))
found_c = bool(re.search(r'\bC\b', text))

print(f'Regex Headings Found: A={found_a}, B={found_b}, C={found_c}')
