import math

def middle_edge_linear_space(match, mismatch, indel, target, pattern):
  I = len(pattern)
  J = len(target)

  dp = [ [0] * (J+1) for _ in range(I+1) ]
  rdp = [ [0] * (J+1) for _ in range(I+1) ]
  dir = [ [0] * (J+1) for _ in range(I+1) ]
  rdir = [ [0] * (J+1) for _ in range(I+1) ]
  sdp = [ [0] * (J+1) for _ in range(I+1) ]

  for i in range(1, I+1):
    dp[i][0] = dp[i-1][0] - indel
    dir[i][0] = 0
  
  for j in range(1, J+1):
    dp[0][j] = dp[0][j-1] - indel
    dir[0][j] = 1

  for i in range(1, I+1):
    for j in range(1, J+1):
      down = dp[i-1][j] - indel
      right = dp[i][j-1] - indel
      diag = 0

      if target[j-1] == pattern[i-1]:
        diag = dp[i-1][j-1] + match
      else:
        diag = dp[i-1][j-1] - mismatch

      arr = [down, right, diag]

      mValue = max(arr)
      mIndex = arr.index(mValue)

      dp[i][j] = mValue
      dir[i][j] = mIndex

  for i in range(I-1, -1, -1):
    rdp[i][J] = rdp[i+1][J] - indel
    rdir[i][J] = 0

  for j in range(J-1, -1, -1):
    rdp[I][j] = rdp[I][j+1] - indel
    rdir[I][j] = 1
  
  for i in range(I-1, -1, -1):
    for j in range(J-1, -1, -1):
      up = rdp[i+1][j] - indel
      left = rdp[i][j+1] - indel
      diag = 0

      if target[j] == pattern[i]:
        diag = rdp[i+1][j+1] + match
      else:
        diag = rdp[i+1][j+1] - mismatch

      arr = [up, left, diag]

      mValue = max(arr)
      mIndex = arr.index(mValue)

      rdp[i][j] = mValue
      rdir[i][j] = mIndex

  for i in range(I+1):
    for j in range(J+1):
      sdp[i][j] = dp[i][j] + rdp[i][j]
  
  mj = J // 2
  mi = 0
  mv = -math.inf

  for i in range(I+1):
    if sdp[i][mj] > mv:
      mv = sdp[i][mj]
      mi = i
  
  ress = []
  ress.append([mi, mj])

  for i in range(mi, I+1):
    if sdp[i][mj+1] == mv:
      ress.append([i, mj+1])
      break
  
  return ress

fn = "dataset_250_12.txt"
f = open(f"./data/{fn}", "r")
match, mismatch, indel = map(int, f.readline().strip().split())
target = f.readline().strip()
pattern = f.readline().strip()
ress = middle_edge_linear_space(match, mismatch, indel, target, pattern)
for res in ress:
  print(" ".join(list(map(str, res))))