
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = [0] * 101
    for x in a:
        cnt[x] += 1

    ans = []

    # First occurrence of each number
    for i in range(101):
        if cnt[i]:
            ans.append(i)
            cnt[i] -= 1

    # Remaining duplicates
    for i in range(101):
        while cnt[i]:
            ans.append(i)
            cnt[i] -= 1

    print(*ans)
