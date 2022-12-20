from copy import deepcopy
from itertools import permutations

N = 8
edges = [
  [1, 3],
  [2, 4, 5],
  [3, 7],
  [],
  [],
  [6],
  [],
  [],
]

dp = [0] * N
cands = [0] * N
numtrack = 0

def rec(cur, tracked, track):
  global dp, numtrack, cands
  if tracked == N:
    print(track)
    numtrack += 1

  for next in edges[cur]:
    if dp[next] == 0:
      cands[next] = 1
  
  for i in range(N):
    if cands[i] == 1:
      dp[i] = 1
      cands[i] = 0
      rec(i, tracked+1, track+str(i))
      dp[i] = 0
      cands[i] = 1

  for next in edges[cur]:
    if dp[next] == 0:
      cands[next] = 0

dp[0] = 1
for next in edges[0]:
  cands[next] = 1
rec(0, 1, "0")
print(numtrack)