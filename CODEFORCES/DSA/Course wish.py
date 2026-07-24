t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))

    cnt = [0] * (k + 2)
    pos = [[] for _ in range(k + 2)]

    for i in range(1, n + 1):
        cnt[b[i]] += 1
        pos[b[i]].append(i)

    need = False
    for i in range(1, n + 1):
        if b[i] != k + 1:
            need = True
            break

    all_full = True
    for i in range(1, k + 1):
        if cnt[i] < a[i]:
            all_full = False
            break

    if need and all_full:
        print(-1)
        continue

    ans = []

    def dfs(idx):
        lv = b[idx]
        if lv == k + 1:
            return

        if lv + 1 <= k and cnt[lv + 1] == a[lv + 1]:
            while pos[lv + 1] and b[pos[lv + 1][-1]] != lv + 1:
                pos[lv + 1].pop()
            dfs(pos[lv + 1][-1])

        cnt[lv] -= 1
        cnt[lv + 1] += 1
        b[idx] += 1
        pos[lv + 1].append(idx)
        ans.append(idx)

    for i in range(1, n + 1):
        while b[i] != k + 1:
            dfs(i)

    print(len(ans))
    if ans:
        print(*ans)
    else:
        print()
