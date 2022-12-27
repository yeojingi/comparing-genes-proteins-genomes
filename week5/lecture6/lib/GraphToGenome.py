def graph_to_genome(GenomeGraph):
  P = []

  N = max([max(edge) for edge in GenomeGraph])

  path = [0] * (N+1)

  for edge in GenomeGraph:
    path[edge[0]] = edge[1]
    path[edge[1]] = edge[1]-1 if edge[1] % 2 == 0 else edge[1]+1
  
  dp = [0] * (N+1)

  for edge in GenomeGraph:
    i = edge[0]
    if dp[i] == 1:
      continue
    
    start = i
    dp[i] = 1
    cur = path[i]
    cycle = []
    while dp[cur] == 0:
      cycle.append(cur)

      dp[cur] = 1
      cur = path[cur]
    cycle.append(start)
    cycle = [cycle[-2], cycle[-1]] + cycle[:-2]

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