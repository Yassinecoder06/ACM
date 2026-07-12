prefix_sum = [0]
array = [0]
i = 1
while prefix_sum[-1] < 2**30:
    array.append(i)
    prefix_sum.append(prefix_sum[-1] + i)
    i += 1

print(prefix_sum[-1])
