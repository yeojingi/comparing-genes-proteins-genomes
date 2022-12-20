def global_alignment(match, mismatch, indel, target, pattern):
  I = len(pattern)
  J = len(target)

  dp = [ [0] * (J+1) for _ in range(I+1)]

  track = [ [0] * (J+1) for _ in range(I+1) ]

  for i in range(1, I+1):
    dp[i][0] = dp[i-1][0] - indel
    track[i][0] = 2

  for j in range(1, J+1):
    dp[0][j] = dp[0][j-1] - indel
    track[i][0] = 0

  for i in range(1, I+1):
    for j in range(1, J+1):
      down = dp[i-1][j] - indel
      right = dp[i][j-1] - indel
      diag = dp[i-1][j-1] + match if pattern[i-1] == target[j-1] else dp[i-1][j-1] - mismatch

      dp[i][j] = max(down, right, diag)
      if down >= right and down >= diag:
        track[i][j] = 2
      elif right >= down and right >= diag:
        track[i][j] = 0
      elif diag >= down and diag >= right:
        track[i][j] = 1
      else:
        print("error")
        exit()
    
  i = I
  j = J
  res_pattern = []
  res_target = []

  while True:
    if i == 0 and j == 0:
      break

    if track[i][j] == 2:
      i -= 1
      res_target.append('-')
      res_pattern.append(pattern[i])
    elif track[i][j] == 0:
      j -= 1
      res_pattern.append('-')
      res_target.append(target[j])
    else:
      i -= 1
      j -= 1
      res_pattern.append(pattern[i])
      res_target.append(target[j])

  res_pattern.reverse()
  res_target.reverse()

  return [dp[I][J], "".join(res_target), "".join(res_pattern)]
  

fn = "dataset_247_3.txt"
f = open(f"./data/{fn}", 'r')
match, mismatch, indel = map(int, f.readline().strip().split())
target = f.readline().strip()
pattern = f.readline().strip()
[score, res1, res2] = global_alignment(match, mismatch, indel, target, pattern)
print(score)
print(res1)
print(res2)

#GAGA
#GAT
# A-