def two_break_on_genome_graph(GenomeGraph, i1, i2, i3, i4):
  result_graph = []
  e1i = 0
  e2i = 0

  for i in range(len(GenomeGraph)):
    ele = GenomeGraph[i]

    # if ele in [[i1, i2], [i2, i1]]:
    #   e1i = i
    # elif ele in [[i3, i4], [i3, i2]]:
    #   e2i = i

    if ele == [i1, i2]:
      e1i = i
    elif ele == [i3, i4]:
      e2i = i
  GenomeGraph[e1i][1] = i3
  GenomeGraph[e2i][0] = i2

  return GenomeGraph

# fn = "1.txt"
# fn = "dataset_8224_2.txt"
# f = open(f"./data/{fn}", "r")
# reads = f.readline().strip().lstrip('(').rstrip(')').split('), (')
# GenomeGraph = [ list(map(int, read.split(', '))) for read in reads ]
# [i1, i2, i3, i4] = list(map(int, f.readline().strip().split(', ')))
# res = two_break_on_genome_graph(GenomeGraph, i1, i2, i3, i4)
# print(res)