import math

def local_alignment(target, pattern):
  I = len(pattern)
  J = len(target)

  matrix = read_pam250()
  dir = [ [0] * (J+1) for _ in range(I+1) ]
  dp = [ [0] * (J+1) for _ in range(I+1) ]
  indel = -5

  for i in range(1, I+1):
    dp[i][0] = dp[i-1][0] + indel
    dir[i][0] = 1
  
  for j in range(1, J+1):
    dp[0][j] = dp[0][j-1] + indel
    dir[0][j] = 2

  for i in range(1, I+1):
    for j in range(1, J+1):
      cands = [0,
        dp[i-1][j] + indel,
        dp[i][j-1] + indel,
        dp[i-1][j-1] + matrix[ pattern[i-1] ][ target[j-1] ] ]

      maxScore = -math.inf
      maxIndex = 0
      for k in range(4):
        if cands[k] > maxScore:
          maxScore = cands[k]
          maxIndex = k
      dp[i][j] = maxScore
      dir[i][j] = maxIndex
  
  maxScore = -math.inf
  maxI = 0
  maxJ = 0

  for i in range(I+1):
    for j in range(J+1):
      if dp[i][j] > maxScore:
        maxI = i
        maxJ = j
        maxScore = dp[i][j]
  
  i = maxI
  j = maxJ
  rt = []
  rp = []
  while i > 0 and j > 0:
    if dir[i][j] == 0:
      i = 0
      j = 0
    elif dir[i][j] == 1:
      rp.append(pattern[i-1])
      rt.append('-')
      i -= 1
    elif dir[i][j] == 2:
      rt.append(target[j-1])
      rp.append('-')
      j -= 1
    else:
      rt.append(target[j-1])
      rp.append(pattern[i-1])
      i -= 1
      j -= 1
  rt.reverse()
  rt = "".join(rt)
  rp.reverse()
  rp = "".join(rp)

  return [maxScore, rt, rp]

def read_pam250():
  f_pam250 = open("./PAM250", 'r')
  AAs = list(f_pam250.readline().strip().split())
  AA_index = {}
  for i in range(20):
    AA_index[AAs[i]] = i

  matrix = {}
  for _ in range(20):
    line_list = f_pam250.readline().strip().split()
    matrix[line_list[0]] = {}
    for i in range(20):
      matrix[line_list[0]][AAs[i]] = int(line_list[i+1])

  f_pam250.close()
  return matrix

fn = "dataset_247_10.txt"
f = open(f"./data/{fn}", "r")
target = f.readline().strip()
pattern = f.readline().strip()
[score, rt, rp] = local_alignment(target, pattern)
print(score)
print(rt)
print(rp)