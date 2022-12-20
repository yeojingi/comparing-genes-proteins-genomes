import math

def affine_gap_penalty(match, mismatch, opening, extension, target, pattern):
  I = len(pattern)
  J = len(target)

  dp = [ [ [0] * 3 for _ in range(J+1) ] for _ in range(I+1) ]
  dir = [ [ [0] * 3 for _ in range(J+1) ] for _ in range(I+1) ]
  # dir = [ [0] * (J+1) for _ in range(I+1) ]

  #로  업 미
  #| - \
  for i in range(1, I+1):
    # dp[i][0][0] = dp[i-1][0][0] - extension
    dp[i][0][0] = -math.inf
    dp[i][0][1] = -math.inf
    dp[i][0][2] = -math.inf
    dir[i][0][0] = 0
  
  for j in range(1, J+1):
    dp[0][j][0] = -math.inf
    dp[0][j][1] = -math.inf
    dp[0][j][2] = -math.inf
    # dp[0][j][2] = dp[0][j-1][2] - extension
    dir[0][j][1] = 2

  for i in range(1, I+1):
    for j in range(1, J+1):
      # dir 1
      for k in [0, 2, 1]:
        lower, middle, upper = -math.inf, -math.inf, -math.inf
        if k == 0:
          lower = dp[i-1][j][0] - extension
          middle = dp[i-1][j][1] - opening
        elif k == 2:
          upper = dp[i][j-1][2] - extension
          middle = dp[i][j-1][1] - opening
        elif k == 1:
          match_or_mismatch = 0
          if target[j-1] == pattern[i-1]:
            match_or_mismatch = match
          else:
            match_or_mismatch = -mismatch

          lower = dp[i-1][j-1][0] + match_or_mismatch
          upper = dp[i-1][j-1][2] + match_or_mismatch
          middle = dp[i-1][j-1][1] + match_or_mismatch

        arr = [lower, middle, upper]

        mValue = max(arr)
        mIndex = arr.index(mValue)

        dp[i][j][k] = mValue
        dir[i][j][k] = mIndex

        # if i == 3 and j == 1 and k == 2:
        #   print(arr, max(arr), k)
          # for k in range(3):
          #   print()
          #   for i in range(I+1):
          #     for j in range(J+1):
          #       print(dir[i][j][k], end=" ")
          #     print(" | ", end="")
          #     for j in range(J+1):
          #       print(dp[i][j][k], end=" ")
          #     print()
        
        # if i == 4 and j == 2 and k == 1:
        #   print(arr, max(arr), k)
        #   for k in range(3):
        #     print(k)
        #     for i in range(I+1):
        #       for j in range(J+1):
        #         print(dir[i][j][k], end=" ")
        #       print(" | ", end="")
        #       for j in range(J+1):
        #         print(dp[i][j][k], end=" ")
        #       print()
      
  mi = 0
  mj = 0
  mk = 0

  rt = []
  rp = []
  # for i in range(1, I+1):
  #   for j in range(1, J+1):
  #     for k in range(3):
  #       if dp[i][j][k] > mValue:
  #         mi, mj, mk = i, j, k
  #         mValue = dp[i][j][k]
  
  # mValue = max(dp[I][J])
  # mi = I
  # mj = J
  # mk = dp[I][J].index(mValue)

  mValue = dp[I][J][1]
  mi = I
  mj = J
  mk = 1

  ci, cj, ck = mi, mj, mk
  v = mk
  while ci > 0 and cj > 0:
    v = dir[ci][cj][ck]
    t = '-'
    p = '-'
    if ck == 0:
      ci -= 1
      p = pattern[ci]
    elif ck == 1:
      ci -= 1
      cj -= 1
      p = pattern[ci]
      t = target[cj]
    elif ck == 2:
      cj -= 1
      t = target[cj]
    rt.append(t)
    rp.append(p)
    ck = v
      
  rt.reverse()
  rp.reverse()

  # print(mi, mj, mk)
  # for k in range(3):
  #   print(k)
  #   for i in range(I+1):
  #     for j in range(J+1):
  #       print(dir[i][j][k], end=" ")
  #     print(" | ", end="")
  #     for j in range(J+1):
  #       print(dp[i][j][k], end=" ")
  #     print()

  return [mValue, "".join(rt), "".join(rp)]

fn = "test.txt"
f = open(f"./data/{fn}", "r")
[match, mismatch, opening, extension] = list(map(int, f.readline().strip().split()))
target = f.readline().strip()
pattern = f.readline().strip()
ress = affine_gap_penalty(match, mismatch, opening, extension, target, pattern)
print(*ress, sep="\n")