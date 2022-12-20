import math

def fitting_alignment(target, pattern, scoring_table):
  indel = -1

  I = len(pattern)
  J = len(target)
  dp = [ [0] * (J+1) for _ in range(I+1) ]
  dir = [ [0] * (J+1) for _ in range(I+1) ]

  for i in range(1, I+1):
    for j in range(1, J+1):
      aa_pattern = pattern[i-1]
      aa_target = target[j-1]

      jump = -math.inf
      right = dp[i][j-1] + indel
      down = dp[i-1][j] + indel
      diag = dp[i-1][j-1] + scoring_table[aa_pattern][aa_target]

      directions = [jump, right, down, diag]
      mValue = max(directions)
      mDir = directions.index(mValue)

      dp[i][j] = mValue
      dir[i][j] = mDir

  cj = 0
  maxValue = 0
  for j in range(1, J+1):
    if dp[I][j] > maxValue:
      maxValue = dp[I][j]
      cj = j
  
  ci = I
  res_t = []
  res_p = []
  while ci > 0 or cj > 0:
    direction = dir[ci][cj]
    if direction == 0:
      ci = 0
      cj = 0
    elif direction == 1:
      cj -= 1
      res_t.append( target[cj] )
      res_p.append( '-' )
    elif direction == 2:
      ci -= 1
      res_t.append( '-' )
      res_p.append( pattern[ci] )
    elif direction == 3:
      ci -= 1
      cj -= 1
      res_t.append( target[cj] )
      res_p.append( pattern[ci] )
  
  res_t.reverse()
  res_p.reverse()

  return [maxValue, "".join(res_t), "".join(res_p) ]

fn = "dataset_248_5.txt"
f = open(f"./data/{fn}", "r")
target = f.readline().strip()
pattern = f.readline().strip()
f.close()

scoring_table = {}
f = open("./BLOSUM62.txt", "r")
header = f.readline().strip().split()
for _ in range(len(header)):
  line = f.readline().strip().split()
  row = {}
  for i in range(len(line[1:])):
    score = int(line[i+1])
    row[header[i]] = score
  
  scoring_table[line[0]] = row

[score, resT, resP] = fitting_alignment(target, pattern, scoring_table)
print(score)
print(resT)
print(resP)
