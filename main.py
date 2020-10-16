import numpy as np

def exercise1(a, offset):
    result = np.zeros((offset*2 + a.shape[0], offset*2 + a.shape[1]))
    result[offset:a.shape[0]+offset, offset:a.shape[1]+offset] = a
    return result

a = np.ones((4,5))
offset = 2

print(a)
print(exercise1(a, offset))
