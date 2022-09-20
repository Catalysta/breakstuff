import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

prices = [100]
for t in range(1, 1000):
    prices.append(prices[t-1] + np.random.normal(0, 10))

def make_money(prices):
    n = len(prices)
    diffs = [prices[x] - prices[x-1] for x in range(1, n)]

    assert np.sum([x > 0 for x in diffs]) > 0, "Cannot make money!"

    if diffs[0] >= 0:
        potential_buys = [0]
    else:
        potential_buys = []

    potential_sells = []
    for i in range(len(diffs)-1):
        if diffs[i] <= 0 and diffs[i+1] > 0:
            potential_buys.append(i + 1)
        elif diffs[i] >= 0 and diffs[i+1] < 0:
            potential_sells.append(i + 1)
        else:
            continue

    if diffs[len(diffs) - 1] > 0:
        potential_sells.append(n-1)

    profit = 0
    buy = int()
    sell = int()

    idx = 0
    for b in potential_buys:
        for s in potential_sells[idx:]:
            potential_profit = prices[s] - prices[b]
            if potential_profit > profit:
                profit = prices[s] - prices[b]
                buy = b
                sell = s
        idx += 1

    return [buy, sell, profit]

out = make_money(prices)

plt.plot(prices)
plt.plot(out[0], prices[out[0]], marker='o')
plt.plot(out[1], prices[out[1]], marker='o')
plt.show()

print(prices)
print("Buy at", out[0], ", sell at", out[1], ". Profit = ", out[2])