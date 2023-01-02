from .ColoredEdges import colored_edges
from .GraphToGenome import graph_to_genome
from .TwoBreakOnGenomeGraph import two_break_on_genome_graph

def two_break_on_genome(P, i1, i2, i3, i4):
  edges = colored_edges(P)
  print('edges', edges, i1, i2, i3, i4)
  new_edges = two_break_on_genome_graph(edges, i1, i2, i3, i4)
  print('new_edges', new_edges)
  new_genome = graph_to_genome(new_edges)
  print('new_genome', new_genome)
  return new_genome

# fn = "dataset_8224_3 (2).txt"
# f = open(f"./data/{fn}", "r")
# reads = f.readline().strip().lstrip("(").rstrip(")").split(")(")
# P = [ list(map(int, read.split())) for read in reads ]
# [i1, i2, i3, i4] = list(map(int, f.readline().strip().split(', ')))
# ress = two_break_on_genome(P, i1, i2, i3, i4)
# output = ""
# for res in ress:
#   output += "("
#   tmp = []
#   for e in res:
#     if e > 0:
#       tmp.append(f"+{e}")
#     else:
#       tmp.append(f"{e}")
#   output += " ".join(tmp) + ")"
# print(output)
