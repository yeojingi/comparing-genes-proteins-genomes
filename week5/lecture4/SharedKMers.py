def shared_kmers(k, target, pattern):
  reversed = reversed_seq(pattern)
  anss = 0
  
  rev_hash = {}
  for j in range(len(pattern) - k + 1):
    n = pattern[j:j+k]

    if rev_hash.get(n):
      rev_hash[n].append(j)
    else:
      rev_hash[n] = [j]
    
    n = reversed_seq(n)
    if rev_hash.get(n):
      rev_hash[n].append(j)
    else:
      rev_hash[n] = [j]
  print("salmonella is done")

  for i in range(len(target) - k + 1):
    cur = target[i:i+k]

    if rev_hash.get(cur):
      for j in rev_hash[cur]:
        anss+=1
  return anss

def reversed_seq(target):
  complements = {"A": "T", "T": "A", "G": "C", "C": "G"}
  reversed = []

  for c in target:
    reversed.append(complements[c])

  reversed.reverse()
  return ''.join(reversed)

# fn = "dataset_289_5 (2).txt"
# f = open(f"./data/{fn}", "r")
k = 30
f = open(f"./data/E_coli.txt", "r")
target = f.readline().strip()
f.close()
f = open(f"./data/Salmonella_enterica.txt", "r")
pattern = f.readline().strip()
f.close()
res = shared_kmers(k, target, pattern)
print(res)