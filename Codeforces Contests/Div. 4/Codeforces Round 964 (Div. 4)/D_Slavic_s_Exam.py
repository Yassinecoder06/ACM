from collections import Counter
def find_first_unsorted(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

t = int(input())

for _ in range(t):
    s = list(input())
    x = list(input())

    co = Counter(x)
    
    question_indexes = []
    for j in range(len(s)):
        if s[j] == '?':
            question_indexes.append(j)

    can = True
    new_s = []
    for i in range(len(s)):
        if co.get(s[i], False) or s[i] == '?':
            new_s.append(s[i])

    if len(new_s) < len(x):
        print('NO')
    else:
        k = 0
        q_index = 0
        for i in range(len(new_s)):
            if k >= len(x):
                if new_s[i] == '?':
                    s[question_indexes[q_index]] = 'a' 
                    q_index += 1
                continue

            if x[k] == new_s[i]:
                k+=1

            elif new_s[i] == '?':
                s[question_indexes[q_index]] = x[k]
                q_index +=1
                k+=1
                
        if k >= len(x):
            print('YES')
            print(''.join(s))
        else:
            print('NO')