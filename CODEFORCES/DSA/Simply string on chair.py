t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    stop = n + 1
    ans = 0

    for i in range(1, n + 1):
        if i == stop:
            break

        ans += 1

        if p[i - 1] > i:
            stop = min(stop, p[i - 1])

    print(ans)
