edges = [
  [0, 3],
  [0, 1],
  [1, 4],
  [1, 2],
  [1, 5],
  [5, 6],
  [2, 7],
  [2, 3]
]

test_edges = [
  [],
  [0],
  [1],
  [0, 2],
  [1],
  [1],
  [5],
  [2],
]

nodes = [0] * 8
nodes[0] = 1
num = 0
se = set()

def rec(usedEdges, nodes, track):
  global num, edges,se

  if len(track) == 8:
    num += 1
    se.add(track)
    return
  
  for i in range(8):
    if usedEdges[i] != 0:
      continue

    [s, e] = edges[i]
    if nodes[s] == 1 and nodes[e] == 0:

      usedEdges[i] = 1
      nodes[e] = 1
      rec(usedEdges, nodes, track+str(e))
      usedEdges[i] = 0
      nodes[e] = 0

rec([0] * len(edges), nodes, "0")
print(num)
print(len(se))

for track in se:

  nodes = [0] * 8
  nodes[0] = 1

  for i in range(1, len(track)):
    s = int(track[i])
    ok = False

    for start in test_edges[s]:
      if str(start) in track:
        ok = True
    if not ok:
      print(track, i, s)
      break