def break_points(arr):
  new_arr = [0] + arr + [ len(arr) + 1]
  L = len(new_arr)

  score = 0

  for i in range(L-1):
    if new_arr[i] - new_arr[i+1] != -1:
      score += 1

  return score

fn = "dataset_287_6.txt"
f = open(f"./data/{fn}", "r")
arr = list(map(int, f.readline().strip().split()))
res = break_points(arr)
print(res)