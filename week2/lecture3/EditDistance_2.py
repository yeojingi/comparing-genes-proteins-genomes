import math

def edit_distance(target, pattern):
  I = len(pattern)
  J = len(target)

  dp = [ [0] * (J+1) for _ in range(I+1) ]

  for i in range(1, I+1):
    dp[i][0] = dp[i-1][0] + 1
  
  for j in range(1, J+1):
    dp[0][j] = dp[0][j-1] + 1

  for i in range(1, I+1):
    for j in range(1, J+1):
      diag = math.inf
      if pattern[i-1] == target[j-1]:
        diag = dp[i-1][j-1]
      else:
        diag = dp[i-1][j-1] + 1
      

      mValue = diag

      dp[i][j] = mValue

  print(*dp, sep="\n")
  print()

  mValue = math.inf
  for i in range(I+1):
    for j in range(J+1):
      dp[i][j] +=  (I-i) + (J-j)
      if dp[i][j] < mValue:
        mValue = dp[i][j]

  print(*dp, sep="\n")

  return mValue

fn = "1.txt"
f = open(f"./data/{fn}", "r")
target = f.readline().strip()
pattern = f.readline().strip()
res = edit_distance(target, pattern)
print(res)