def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for i in range(len(weights)):
        # Move backward to avoid repeating items
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(
                dp[w],
                values[i] + dp[w - weights[i]]
            )

    return dp[capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

answer = knapsack(weights, values, capacity)
print("Maximum Profit:", answer)
