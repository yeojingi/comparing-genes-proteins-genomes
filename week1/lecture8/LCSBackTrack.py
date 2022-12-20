import sys

sys.setrecursionlimit(10**6) 

def LCS_back_track(v, w):
  direction = {'down': 0, 'right': 1, 'diagonal': 2}

  nV = len(v)
  nW = len(w)

  s = [ [0] * (nW+1) for _ in range(nV+1) ]
  backTrack = [ [0] * (nW+1) for _ in range(nV+1) ]

  for i in range(nV):
    for j in range(nW):
      match = 0
      if v[i] == w[j]:
        match = 1

      s[i+1][j+1] = max(s[i][j+1], s[i+1][j], s[i][j] + match)

      if s[i+1][j+1] == s[i][j+1]:
        backTrack[i+1][j+1] = direction['down']
      elif s[i+1][j+1] == s[i+1][j]:
        backTrack[i+1][j+1] = direction['right']
      elif s[i+1][j+1] == s[i][j] + match:
        backTrack[i+1][j+1] = direction['diagonal']
  
  print("  ", w)
  for i in range(len(s)):
    ss = backTrack[i]
    print(v[i-1] if i != 0 else " ", "".join(list(map(str,ss))))

  return backTrack

def Output_LCS(backTrack, v, i, j):
  direction = {'down': 0, 'right': 1, 'diagonal': 2}

  if i == 0 or j == 0:
    return ""
  
  if backTrack[i][j] == direction['down']:
    return Output_LCS(backTrack, v, i-1, j)
  elif backTrack[i][j] == direction['right']:
    return Output_LCS(backTrack, v, i, j-1)
  else:
    print(i, j, backTrack[i][j])
    return Output_LCS(backTrack, v, i-1, j-1) + v[i-1]

filename = "dataset_245_5.txt"
filename = "dataset_245_5 (1).txt"
f = open(f"./data/{filename}", "r")
v = f.readline().strip()
w = f.readline().strip()
backTrack = LCS_back_track(v, w)
res = Output_LCS(backTrack, v, len(v), len(w))
print(res)