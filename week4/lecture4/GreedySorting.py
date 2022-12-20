def greedy_sorting(arr):
  t = open('./data/freak.txt', 'r')
  ress = []
  for i in range(1, len(arr)+1):
    for j in range(i-1, len(arr)):
      if arr[j] == i or arr[j] == -i:
        break
    
    # for k in range(i-1, ((j) - (i-1) - 1) // 2 + 1 + i - 1):
    # print(i, j, (j - (i-1)) // 2 + 1)
    if j != i-1:
      for k in range((j - (i-1)) // 2 + 1):
        if j-k == i-1+k:
          arr[j-k] *= -1
        else:
          tmp = arr[j-k]
          arr[j-k] = -arr[i-1+k]
          arr[i-1+k] = -tmp
        # print(f"\t{k} {j+1-k}")
      
      ress.append(print_arr(arr))
      # r = print_arr(arr)
      # tr = t.readline().strip()
      # if not tr == f'({r})':
      #   print(i)
      #   print(r)
      #   print(tr)
      #   break


    if arr[i-1] < 0:
      arr[i-1] *= -1
      ress.append(print_arr(arr))
      # r = print_arr(arr)
      # tr = t.readline().strip()
      # if not tr == f'({r})':
      #   print(r)
      #   break

  return ress

def print_arr(arr):
  seq = []
  for i in range(len(arr)):
    if arr[i] > 0:
      seq.append(f"+{arr[i]}")
    else:
      seq.append(str(arr[i]))
  
  return " ".join(seq)

fn = "1.txt"
fn = "dataset_286_4 (1).txt"
fn = "dataset_286_4 (2).txt"
fn = "quiz.txt"
f = open(f"./data/{fn}", "r")
arr = list(map(int, f.readline().strip().split()))
ress = greedy_sorting(arr)
f.close()
f = open("./data/output.txt", "w")
for res in ress:
  f.write(res)
  f.write("\n")
# print(*ress, sep="\n")