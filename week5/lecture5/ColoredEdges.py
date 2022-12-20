def colored_edges(cycles):
  ress = []
  for cycle in cycles:
    for i in range(-1, len(cycle)-1):
      if cycle[i] > 0:
        s = 2*cycle[i]
      else:
        s = -2*cycle[i] - 1

      if cycle[i+1] > 0:
        e = 2*cycle[i+1] - 1
      else:
        e = -2*cycle[i+1]
      
      ress.append(f"({s}, {e})")
  
  return ress
      

fn = "dataset_8222_7.txt"
f = open(f"./data/{fn}", "r")
read = f.readline().strip()
raw_cycles = read.split(")")
cycles = [ list(map(int, raw_cycle.lstrip("(").split())) for raw_cycle in raw_cycles ]
ress = colored_edges(cycles)
print(", ".join(ress))
