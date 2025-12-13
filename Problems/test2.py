from itertools import accumulate
import operator
arr = [1,2,3,4,5,6]

print(list(accumulate(arr, operator.mul)))