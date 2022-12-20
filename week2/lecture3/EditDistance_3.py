import math

def edit_distance(target, pattern):
  I = len(pattern)
  J = len(target)

  last = [ [ I-i + J-j for j in range(J+1)] for i in range(I+1) ]
  dp = [ [0] * (J+1) for _ in range(I+1) ]
  dir = [ [0] * (J+1) for _ in range(I+1) ]

  for i in range(1, I+1):
    dp[i][0] = dp[i-1][0] + 1
    dir[i][0] = 0
  
  for j in range(1, J+1):
    dp[0][j] = dp[0][j-1] + 1
    dir[0][j] = 0

  for i in range(1, I+1):
    for j in range(1, J+1):
      jump = i+j
      diag = math.inf
      left = dp[i][j-1] + 1
      down = dp[i-1][j] + 1
      if pattern[i-1] == target[j-1]:
        diag = dp[i-1][j-1]
      else:
        diag = dp[i-1][j-1] + 1
      
      arr = [jump, left, down, diag]

      mValue = min(arr)
      mIndex = arr.index(mValue)

      dp[i][j] = mValue
      dir[i][j] = mIndex

  print(*dp, sep="\n")
  print('dp')
  print(*dir, sep="\n")
  print('dir')

  print(*last, sep="\n")
  print('last')

  mValue = math.inf
  for i in range(I+1):
    for j in range(J+1):
      dp[i][j] += last[i][j]
      if mValue > dp[i][j]:
        mValue = dp[i][j]

  print(*dp, sep="\n")

  return mValue

fn = "dataset_248_3 (2).txt"
f = open(f"./data/{fn}", "r")
target = f.readline().strip()
pattern = f.readline().strip()
res = edit_distance(target, pattern)
print(res)