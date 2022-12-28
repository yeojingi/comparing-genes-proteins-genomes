def two_break_distance(P, Q, maxSynteny):
  path_p = [0] * (maxSynteny * 2 + 1)
  path_q = [0] * (maxSynteny * 2 + 1)

  for cycle in P:
    for i in range(len(cycle)):
      if cycle[i] > 0:
        e = cycle[i]*2 - 1
      else:
        e = -cycle[i]*2
      
      if cycle[i-1] > 0:
        s = cycle[i-1] * 2
      else:
        s = -cycle[i-1] * 2 - 1
      
      path_p[s] = e
      path_p[e] = s
  
  for cycle in Q:
    for i in range(len(cycle)):
      if cycle[i] > 0:
        e = cycle[i]*2 - 1
      else:
        e = -cycle[i]*2
      
      if cycle[i-1] > 0:
        s = cycle[i-1] * 2
      else:
        s = -cycle[i-1] * 2 - 1
      
      path_q[s] = e
      path_q[e] = s

  dp = [0] * (maxSynteny * 2 + 1)
  nCycle = 0
  for i in range(1, len(path_p)):
    cur = i
    p = True
    if dp[cur] == 0:
      nCycle += 1

    while dp[cur] == 0:
      if p:
        dp[cur] = 1
        cur = path_p[cur]
        p = False
      else:
        dp[cur] = 1
        cur = path_q[cur]
        p = True
  
  return maxSynteny - nCycle

fn = "test_result.txt"
f = open(f"./data/{fn}", "r")
reads = f.readline().strip().lstrip('(').rstrip(')').split(')(')
P = [ list(map(int, read.split())) for read in reads ]
reads = f.readline().strip().lstrip('(').rstrip(')').split(')(')
Q = [ list(map(int, read.split())) for read in reads ]
res = two_break_distance(P, Q, max( [max([abs(n) for n in cycle]) for cycle in P] ))
print(res)