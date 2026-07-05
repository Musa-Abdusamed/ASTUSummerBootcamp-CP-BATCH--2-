

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    weights = [100 // x for x in a]
    dp = [False] * 101
    dp[0] = True
    for w in weights:
        for i in range(100, w - 1, -1):
            if dp[i - w]:
                dp[i] = True
    ok = all(dp[i] for i in range(101))

    print("Yes" if ok else "No")
