def graph_to_genome(GenomeGraph):
  P = []

  N = max([max(edge) for edge in GenomeGraph])

  path = [0] * (N+1)

  for edge in GenomeGraph:
    path[edge[0]] = edge[1]
    path[edge[1]] = edge[0]
  
  dp = [0] * (N+1)

  for edge in GenomeGraph:
    i = edge[0]
    if dp[i] == 1:
      continue
    
    start = i
    dp[start] = 1
    dp[path[start]] = 1
    cur = path[start]
    cycle = [start, cur]
    cur = cur - 1 if cur % 2 == 0 else cur + 1

    while dp[cur] == 0:
      cycle.append(cur)
      cycle.append(path[cur])
      dp[cur] = 1
      dp[path[cur]] = 1
      if path[cur] == 0:
        print('0 is visited')
        exit()

      cur = path[cur]
      cur = cur - 1 if cur % 2 == 0 else cur + 1

    cycle = [cycle[-1]] + cycle[:-1]

    P.append(cycle_to_chromosome(cycle))

  return P

def cycle_to_chromosome(cycle):
  chromosome_arr = []

  for i in range(0, len(cycle), 2):
    if cycle[i] > cycle[i+1]:
      chromosome_arr.append(-cycle[i] // 2)
    else:
      chromosome_arr.append(cycle[i+1] // 2)
  
  return chromosome_arr

# fn = "4.txt"
# f = open(f"./data/{fn}", "r")
# reads = f.readline().strip().lstrip('(').rstrip(')').split('), (')
# reads = [ list(map(int, read.split(', '))) for read in reads]
# res = graph_to_genome(reads)
# print(res)