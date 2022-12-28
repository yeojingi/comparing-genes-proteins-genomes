from lib.ColoredEdges import colored_edges
from lib.TwoBreakOnGenome import two_break_on_genome

def two_break_distance(P, Q):
  edges_Q = colored_edges(Q)
  ress = []

  for edge_Q in edges_Q:
    print('res', P)
    print('edge_Q', edge_Q)
    ress.append(P)
    edges_P = colored_edges(P)
    [s, e] = edge_Q

    for edge_P in edges_P:
      if s in edge_P:
        # [i1, i2] = [s, edge_P[edge_P.index(s)-1]]
        [i1, i2] = edge_P
      if e in edge_P:
        # [i3, i4] = [e, edge_P[edge_P.index(e)-1]]
        [i3, i4] = edge_P
        # [i2, i4] = edge_P
    
    if [i1, i2] == [i3, i4] or [i1, i2] == [i4, i3]:
      break

    P = two_break_on_genome(P, i1, i2, i3, i4)
    print()
    # input()
    
  # ress.append(P)
  return ress

fn = "test.txt"
f = open(f"./data/{fn}", "r")
reads = f.readline().strip().lstrip('(').rstrip(')').split(')(')
P = [ list(map(int, read.split())) for read in reads ]
reads = f.readline().strip().lstrip('(').rstrip(')').split(')(')
Q = [ list(map(int, read.split())) for read in reads ]
ress = two_break_distance(P, Q)

output = ""
for r in ress:
  for res in r:
    output += "("
    tmp = []
    for e in res:
      if e > 0:
        tmp.append(f"+{e}")
      else:
        tmp.append(f"{e}")
    output += " ".join(tmp) + ")"
  print(output)
  output = ""