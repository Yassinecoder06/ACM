import re
text = """
Editorial for Contest 2148
Problem A: Simple Task
Problem B: Complex Math
Problem C: Graph Problem
"""
print(f"Tutorial Link: https://codeforces.com/blog/entry/mock_2148")
print(f"Editorial Length: {len(text)}")
print("First 40 lines (non-empty):")
lines = [l.strip() for l in text.splitlines() if l.strip()]
for line in lines:
    print(line)
print(f"Regex Headings Found: A={bool(re.search(r\"\\bA\\b\", text))}, B={bool(re.search(r\"\\bB\\b\", text))}, C={bool(re.search(r\"\\bC\\b\", text))}")
