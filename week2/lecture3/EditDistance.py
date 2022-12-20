import math

def edit_distance(target, pattern):
  I = len(pattern)
  J = len(target)

  last = [ [ abs( (I - i) - (J - j)) + abs(i-j) for j in range(J+1)] for i in range(I+1) ]
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
      left = dp[i][j-1] + 1
      down = dp[i-1][j] + 1
      diag = math.inf
      if pattern[i-1] == target[j-1]:
        diag = dp[i-1][j-1]
      
      arr = [jump, left, down, diag]

      mValue = min(arr)
      mIndex = arr.index(mValue)

      dp[i][j] = mValue
      dir[i][j] = mIndex

  print(*dp, sep="\n")
  print()
  print(*dir, sep="\n")
  print()

  print(*last, sep="\n")
  print()
  for i in range(I+1):
    for j in range(J+1):
      dp[i][j] += last[i][j]

  print(*dp, sep="\n")

  # pass

fn = "1.txt"
f = open(f"./data/{fn}", "r")
target = f.readline().strip()
pattern = f.readline().strip()
res = edit_distance(target, pattern)
print(res)