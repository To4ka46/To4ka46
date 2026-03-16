def count_partitions(n):
    
    if n < 0:
        return 0
    if n == 0:
        return 1 

    dp = [0] * (n + 1)
    dp[0] = 1

    for part in range(1, n + 1):
        for k in range(part, n + 1):
            dp[k] += dp[k - part]

    return dp[n]

for i in range(1, 11):
    print(f"n({i}) = {count_partitions(i)}")

