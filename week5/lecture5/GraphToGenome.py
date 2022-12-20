def graph_to_genome(GenomeGraph):
  P = []
  cycles = []

  for i in range(len(GenomeGraph)):
    cycle = GenomeGraph[i]

    if i >= len(GenomeGraph) - 1:
      cycles.append(cycle[0])
      cycles.insert(0, cycle[1])
      P.append(cycle_to_chromosome(cycles))
      cycles = []
      break

    nextCycle = GenomeGraph[i+1]

    if abs(cycle[1] - nextCycle[0]) == 1:
      cycles.append(cycle[0])
      cycles.append(cycle[1])
    else:
      cycles.append(cycle[0])
      cycles.insert(0, cycle[1])
      P.append(cycle_to_chromosome(cycles))
      cycles = []

  return "".join(P)

def cycle_to_chromosome(cycle):
  chromosome_arr = []

  for i in range(0, len(cycle), 2):
    if cycle[i] > cycle[i+1]:
      chromosome_arr.append(f"-{cycle[i] // 2}")
    else:
      chromosome_arr.append(f"+{cycle[i+1] // 2}")
  
  return "(" + " ".join(chromosome_arr) + ")"

fn = "dataset_8222_8.txt"
f = open(f"./data/{fn}", "r")
reads = f.readline().strip().lstrip('(').rstrip(')').split('), (')
reads = [ list(map(int, read.split(', '))) for read in reads]
res = graph_to_genome(reads)
print(res)