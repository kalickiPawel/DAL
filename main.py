import numpy as np

def exercise1(a, offset):
    return np.vstack((
        np.zeros((offset, a.shape[0]+2*offset+1)), 
        np.hstack((
            np.zeros((a.shape[0],offset)),
            a,
            np.zeros((a.shape[0],offset)))),
        np.zeros((offset, a.shape[0]+2*offset+1))
    ))

def exercise1_1(a, offset):
    result = np.zeros((offset*2 + a.shape[0], offset*2 + a.shape[1]))
    result[offset:a.shape[0]+offset, offset:a.shape[1]+offset] = a
    return result

#TODO: policzyc czasy dla dwoch funkcji
a = np.ones((4,5))
offset = 3

print(a)
print(exercise1(a, offset))
print(exercise1_1(a, offset))
