import numpy as np
from numba import njit
 
@njit('(i4[::1],)', cache=True)
def f(A):
  N = len(A)
  cnt = 0
  for i in range(N):
    for j in range(i + 1, N):
      for k in range(j + 1, N):
        cnt += (A[k] < A[i] + A[j])
  return cnt
 
N = int(input())
A = np.int32(input().split())
A.sort()
print(f(A))