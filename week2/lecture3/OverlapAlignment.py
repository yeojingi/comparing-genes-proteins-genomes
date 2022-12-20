import math

def overlap_alignment(match, mismatch, indel, target, pattern):
  I = len(pattern)
  J = len(target)

  dp = [ [0]*(J+1) for _ in range(I+1) ]
  dir = [ [0]*(J+1) for _ in range(I+1) ]

  for i in range(1, I+1):
    dp[i][0] = dp[i-1][0] - indel
    dir[i][0] = 2

  # for j in range(1, J+1):
  #   dp[0][j] = dp[0][j-1] - indel
  #   dir[0][j] = 1

  for i in range(1, I+1):
    if i == I//2:
      print("dp half generated")
    for j in range(1, J+1):
      jump = -math.inf
      right = dp[i][j-1] - indel
      down = dp[i-1][j] - indel
      diag = 0
      if target[j-1] == pattern[i-1]:
        diag = dp[i-1][j-1] + match
      else:
        diag = dp[i-1][j-1] - mismatch
      
      arr = [jump, right, down, diag]

      mValue = max(arr)
      mIndex = arr.index(mValue)

      dp[i][j] = mValue
      dir[i][j] = mIndex
  
  mValue = 0
  mIndex = 0
  for i in range(I+1):
    if dp[i][J] > mValue:
      mValue = dp[i][J]
      mIndex = i

  ci = mIndex
  cj = J

  print('dp generated')
  rep_t = []
  rep_p = []
  while ci > 0 or cj > 0:
    v = dir[ci][cj]
    # print(ci, cj, v, "".join(rep_t), "".join(rep_p))
    if v == 0:
      ci = 0 
      cj = 0
    elif v == 1:
      cj -= 1
      rep_t.append(target[cj])
      rep_p.append('-')
    elif v == 2:
      ci -= 1
      rep_t.append('-')
      rep_p.append(pattern[ci])
    else:
      ci -= 1
      cj -= 1
      rep_t.append(target[cj])
      rep_p.append(pattern[ci])

  rep_t.reverse()
  rep_p.reverse()

  return [mValue, "".join(rep_t), "".join(rep_p)]    

fn = "dataset_248_7.txt"
f = open(f'./data/{fn}', 'r')
match, mismatch, indel = map(int, f.readline().strip().split())
target = f.readline().strip()
pattern = f.readline().strip()
[score, rep_t, rep_p] = overlap_alignment(match, mismatch, indel, target, pattern)
print(f'{score}\n{rep_t}\n{rep_p}')