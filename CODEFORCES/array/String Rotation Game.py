
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    def blocks(st):
        cnt = 1
        for i in range(1, len(st)):
            if st[i] != st[i-1]:
                cnt += 1
        return cnt

    ans = 0

    for i in range(n):
        rotated = s[i:] + s[:i]
        ans = max(ans, blocks(rotated))

    print(ans)
