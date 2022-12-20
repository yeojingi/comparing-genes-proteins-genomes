import sys

sys.setrecursionlimit(10**6)

def longest_path_DAG(matrix, n):
  N = len(matrix)

  maxValue = 0
  maxIndex = 0
  for j in range(N):
    if matrix[n][j] > maxValue:
      maxValue = matrix[n][j]
      maxIndex = j

  if maxValue == 0:
    return [0, [n]]
  else:
    [d, res] = longest_path_DAG(matrix, maxIndex)
    res.append(n)
    return [d + maxValue, res]

filename = "dataset_245_7.txt"
filename = "2.txt"
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
  matrix[m][n] = d

[d, res] = longest_path_DAG(matrix, e)
print(d)
# res.reverse()
print(" ".join(list(map(str, res))))