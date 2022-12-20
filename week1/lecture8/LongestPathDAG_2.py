import sys

sys.setrecursionlimit(10**6)

def longest_path_DAG(matrix, s, e):
  N = len(matrix)
  dp_s = [-1] * N
  dp_track = [ [] for _ in range(N) ]

  def rec(n):
    print('rec', n)
    if n == s:
      # dp_s[s] = 0
      return [s]
    maxIndex = s
    maxDistance = 0
    maxTrack = []

    for i in range(N):
      if matrix[i][n] > 0:
        if dp_s[i] < 0:
          track = rec(i)
        else:
          track = dp_track[i]
        
        if dp_s[i] == 0:
          continue
        
        if dp_s[i] + matrix[i][n] > maxDistance:
          maxDistance = dp_s[i] + matrix[i][n]
          maxIndex = i
          maxTrack = track
    
    dp_s[n] = maxDistance
    dp_track[n] = maxTrack
    return maxTrack + [n]

  res = rec(e)
  d = dp_s[e]

  print(dp_s)  
  print(*matrix, sep="\n")
  return [d, res]

#####################################################################


filename = "dataset_245_7.txt"
filename = "2.txt"
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

[d, res] = longest_path_DAG(matrix, s, e)
print(d)
# res.reverse()
print(" ".join(list(map(str, res))))