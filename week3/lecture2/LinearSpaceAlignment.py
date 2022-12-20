import math
import sys

sys.setrecursionlimit(10**6)

score = 0

def solution(match, mismatch, indel, target, pattern):

  out_v = []
  out_w = []

  def linear_space_aligment(v, w, top, bottom, left, right):
    global score

    print(top, bottom, left, right)
    if left == right:
      # output
      for i in range(top, bottom):
        score -= indel
        out_w.append( w[i-1] )
        out_v.append( '-' )
      return

    elif top == bottom:
      # output
      for j in range(left, right):
        score -= indel
        out_w.append( '-' )
        out_v.append( v[j-1] )
      return
        
    middle = (left + right) // 2

    # midEdge = [left, right, dir]
    midEdge = MiddleEdge(v, w, top, bottom, left, right)
    midNode = midEdge[0][0]
    linear_space_aligment(v, w, top, midNode, left, middle)
    
    print('midEdge', midEdge)
    # return midEdge # output
    if midEdge[2] == 0:
      score -= indel
      j = midEdge[0][1]
      out_w.append('-')
      out_v.append( v[j] )
    elif midEdge[2] == 1:
      score -= indel
      i = midEdge[0][0]
      out_w.append( w[i] )
      out_v.append( '-' )
    elif midEdge[2] == 2:
      i = midEdge[0][0]
      j = midEdge[0][1]
      out_w.append( w[i] )
      out_v.append( v[j] )
      if w[i] == v[j]:
        score += match
      else:
        score -= mismatch

    if midEdge[2] == 0 or midEdge[2] == 2:
      middle = middle + 1
    if midEdge[2] == 1 or midEdge[2] == 2:
      midNode = midNode + 1
    
    linear_space_aligment(v, w, midNode, bottom, middle, right)

  def MiddleEdge(v, w, top, bottom, left, right):
    I = bottom - top
    J = right - left

    dp = [ [0] * (J+1) for _ in range(I+1) ]
    rdp = [ [0] * (J+1) for _ in range(I+1) ]
    dir = [ [0] * (J+1) for _ in range(I+1) ]
    rdir = [ [0] * (J+1) for _ in range(I+1) ]
    sdp = [ [0] * (J+1) for _ in range(I+1) ]

    for i in range(1, I+1):
      dp[i][0] = dp[i-1][0] - indel
      dir[i][0] = 0
    
    for j in range(1, J+1):
      dp[0][j] = dp[0][j-1] - indel
      dir[0][j] = 1

    for i in range(1, I+1):
      for j in range(1, J+1):
        down = dp[i-1][j] - indel
        to_right = dp[i][j-1] - indel
        diag = 0

        if v[left + j-1] == w[top + i-1]:
          diag = dp[i-1][j-1] + match
        else:
          diag = dp[i-1][j-1] - mismatch

        arr = [down, to_right, diag]

        mValue = max(arr)
        mIndex = arr.index(mValue)

        dp[i][j] = mValue
        dir[i][j] = mIndex

    for i in range(I-1, -1, -1):
      rdp[i][J] = rdp[i+1][J] - indel
      rdir[i][J] = 0

    for j in range(J-1, -1, -1):
      rdp[I][j] = rdp[I][j+1] - indel
      rdir[I][j] = 1
    
    for i in range(I-1, -1, -1):
      for j in range(J-1, -1, -1):
        up = rdp[i+1][j] - indel
        to_left = rdp[i][j+1] - indel
        diag = 0

        if v[left + j] == w[top + i]:
          diag = rdp[i+1][j+1] + match
        else:
          diag = rdp[i+1][j+1] - mismatch

        arr = [up, to_left, diag]

        mValue = max(arr)
        mIndex = arr.index(mValue)

        rdp[i][j] = mValue
        rdir[i][j] = mIndex

    for i in range(I+1):
      for j in range(J+1):
        sdp[i][j] = dp[i][j] + rdp[i][j]
    
    mj = J // 2
    mi = 0
    mv = -math.inf

    for i in range(I+1):
      if sdp[i][mj] > mv:
        mv = sdp[i][mj]
        mi = i
    
    ress = []
    ress.append([top + mi, left + mj])

    # print()
    # print(*sdp, sep="\n")
    # print()
    for i in range(mi, I+1):
      # print(i, mj, sdp)
      if sdp[i][mj+1] == mv and (i == mi or i == mi + 1):
        ress.append([top+ i, left + mj+1])
        break
    if len(ress) == 1:
      ress.append([top+ mi+1, left + mj])
    
    di = ress[1][0] - ress[0][0]
    dj = ress[1][1] - ress[0][1]

    print("di dj", di, dj, ress)
    if di == 0:
      ress.append(0)
    elif di == 1 and dj == 0:
      ress.append(1)
    elif di == 1 and dj == 1:
      ress.append(2)

    print('ress', ress)

    return ress

  linear_space_aligment(target, pattern, 0, len(pattern), 0, len(target))

  # out_v.reverse()
  # out_w.reverse()

  print(score)
  print("".join(out_v))
  print("".join(out_w))

fn = 'dataset_250_14.txt'
f = open(f'./data/{fn}', 'r')
match, mismatch, indel = map(int, f.readline().strip().split())
target = f.readline().strip()
pattern = f.readline().strip()
solution(match, mismatch, indel, target, pattern)
# print(*ress, sep="\n")