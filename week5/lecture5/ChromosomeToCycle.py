def chromosome_to_cycle(chromosome):
  arr = list(map(int, chromosome.lstrip('(').rstrip(')').split()))
  res_arr = []

  for ele in arr:
    if ele > 0:
      res_arr.append(2*ele-1)
      res_arr.append(2*ele)
    else:
      res_arr.append(-2*ele)
      res_arr.append(-2*ele-1)

  res = " ".join(list(map(str, res_arr)))
  res = "(" + res + ")"
  return res

fn = "dataset_8222_4.txt"
f = open(f"./data/{fn}", "r")
chromosome = f.readline().strip()
res = chromosome_to_cycle(chromosome)
print(res)