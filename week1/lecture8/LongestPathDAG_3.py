import sys

sys.setrecursionlimit(10**6)

def longest_path_DAG(matrix):
  N = len(matrix)
  dp = [[0] * N for _ in range(N) ]
  path = []

  for j in range(N):
    dp[0][j] = matrix[0][j]

  for i in range(1, N):
    for j in range(N):
      dp[i][j] = dp[i-1][j]
      if matrix[i][j] > 0:
        dp[i][j] = max(dp[i-1][i] + matrix[i][j], dp[i-1][j])

  maxValue = 0
  maxI = 0
  maxJ = 0
  for i in range(N):
    for j in range(N):
      if dp[i][j] > maxValue:
        maxValue = dp[i][j]
        maxI = i
        maxJ = j
  
  # print(*dp, sep="\n")

  i = maxI
  j = maxI
  path.append(maxJ)

  while True:
    if i == 0:
      path.append(j)
      path.append(i)
      break

    if dp[i-1][j] != dp[i][j]:
      path.append(j)
      j = i
    else:
      i -= 1
  
  path.reverse()

  return [maxValue,path]

#####################################################################


# filename = "dataset_245_7.txt"
filename = "dataset_245_7 (2).txt"
# filename = "dataset_245_7 (1).txt"
f = open(f"./data/{filename}", "r")
s, e = map(int, f.readline().strip().split())
N = e - s + 1

matrix = [ [0] * N for _ in range(N) ]

while True:
  line = f.readline().strip()
  if not line:
    break
  n, m, d = map(int, line.split())
  # matrix[n][m] = d
  matrix[n][m] = d

[d, res] = longest_path_DAG(matrix)
print(d)
# res.reverse()
print(" ".join(list(map(str, res))))