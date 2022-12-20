def cycle_to_chromosome(cycle):
  arr = list(map(int, cycle.lstrip('(').rstrip(')').split()))
  res_arr = []

  for i in range(0, len(arr), 2):
    if arr[i] > arr[i+1]:
      res_arr.append(f"{-arr[i] // 2}")
    else:
      res_arr.append(f"+{arr[i+1] // 2}")
  
  res = "(" + " ".join(res_arr) + ")"
  return res

fn = "dataset_8222_5.txt"
f = open(f"./data/{fn}", "r")
cycle = f.readline().strip()
res = cycle_to_chromosome(cycle)
print(res)