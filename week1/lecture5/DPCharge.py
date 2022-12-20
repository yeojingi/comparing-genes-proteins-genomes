import math

def dp_charge(money, coins):
  minCoins = [0]
  for m in range(1, money+1):
    minCoins.append(math.inf)
    for i in range(len(coins)):
      if m >= coins[i]:
        if minCoins[m - coins[i]] + 1 < minCoins[m]:
          minCoins[m] = minCoins[m - coins[i]] + 1
  return minCoins[money]

filename = "dataset_243_10.txt"
f = open(f"./data/{filename}", "r")

money = int(f.readline().strip())
coins = list(map(int, f.readline().strip().split()))

res = dp_charge(money, coins)
print(res)