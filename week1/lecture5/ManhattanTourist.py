def manhattan_tourist(N, M, Down, Right):
  S = [ [0] * M for _ in range(N)]
  for i in range(1, N):
    S[i][0] = S[i-1][0] + Down[i-1][0]
  
  for j in range(1, M):
    S[0][j] = S[0][j-1] + Right[0][j-1]
  
  for i in range(1, N):
    for j in range(1, M):
      S[i][j] = max(S[i-1][j] + Down[i-1][j], S[i][j-1] + Right[i][j-1])
  
  return S[N-1][M-1]

filename = "dataset_261_10.txt"
f = open(f"./data/{filename}", "r")

N, M = map(int, f.readline().strip().split())
Down = [ list(map(int, f.readline().strip().split())) for _ in range(N) ]
f.readline()
Right = [ list(map(int, f.readline().strip().split())) for _ in range(N+1)]

res = manhattan_tourist(N+1, M+1, Down, Right)
print(res)