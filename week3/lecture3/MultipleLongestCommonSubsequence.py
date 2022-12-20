def solution(seqs):
  I, J, K = len(seqs[0]), len(seqs[1]), len(seqs[2])

  dp = [ [ [0] * (K+1) for _ in range(J+1) ] for _ in range(I+1) ]
  dir = [ [ [0] * (K+1) for _ in range(J+1) ] for _ in range(I+1) ]

  for i in range(1, I+1):
    dir[i][0][0] = 0
  for j in range(1, J+1):
    dir[0][j][0] = 1
  for k in range(1, K+1):
    dir[0][0][k] = 2

  for i in range(1, I+1):
    for j in range(1, J+1):
      dir[i][j][0] = 3
  
  for j in range(1, J+1):
    for k in range(1, K+1):
      dir[0][j][k] = 5
  
  for i in range(1, I+1):
    for k in range(1, K+1):
      dir[i][0][k] = 4
  
  for i in range(1, I+1):
    for j in range(1, J+1):
      for k in range(1, K+1):
        arr = [
          dp[i-1][j][k],
          dp[i][j-1][k],
          dp[i][j][k-1],
          dp[i-1][j-1][k],
          dp[i-1][j][k-1],
          dp[i][j-1][k-1],
          dp[i-1][j-1][k-1] + 1 if seqs[0][i-1] == seqs[1][j-1] and seqs[0][i-1] == seqs[2][k-1] \
           else dp[i-1][j-1][k-1]
        ]

        arr.reverse()
        mValue = max(arr)
        mIndex = 6 - arr.index(mValue)
        # mIndex = arr.index(mValue)

        dp[i][j][k] = mValue
        dir[i][j][k] = mIndex

  mValue = dp[I][J][K]
  res = [ [], [], [] ]

  ci = I
  cj = J
  ck = K
  
  while ci > 0 or cj > 0 or ck > 0:
    v = dir[ci][cj][ck]
    
    for i in range(3):
      res[i].append('-')
    
    print(mValue, dp[ci][cj][ck], v, ci, cj, ck, "".join(res[0]), "".join(res[1]), "".join(res[2]))
    if v == 0:
      res[0][-1] = seqs[0][ci-1]
      ci -= 1
    elif v == 1:
      res[1][-1] = seqs[1][cj-1]
      cj -= 1
    elif v == 2:
      res[2][-1] = seqs[2][ck-1]
      ck -= 1
    elif v == 3:
      res[0][-1] = seqs[0][ci-1]
      res[1][-1] = seqs[1][cj-1]
      ci -= 1
      cj -= 1
    elif v == 4:
      res[0][-1] = seqs[0][ci-1]
      res[2][-1] = seqs[2][ck-1]
      ci -= 1
      ck -= 1
    elif v == 5:
      res[1][-1] = seqs[1][cj-1]
      res[2][-1] = seqs[2][ck-1]
      cj -= 1
      ck -= 1
    elif v == 6:
      res[0][-1] = seqs[0][ci-1]
      res[1][-1] = seqs[1][cj-1]
      res[2][-1] = seqs[2][ck-1]
      ci -= 1
      cj -= 1
      ck -= 1
  
  subseqs = []
  for k in range(3):
    res[k].reverse()
    subseqs.append( "".join(res[k]) )
  return [mValue, *subseqs]

fn = "dataset_251_5.txt"
fn = "1.txt"
fn = "dataset_251_5 (1).txt"
fn = "quiz.txt"
f = open(f"./data/{fn}", "r")
seqs = [ f.readline().strip() for _ in range(3) ]
res = solution(seqs)
print(*res, sep = "\n")