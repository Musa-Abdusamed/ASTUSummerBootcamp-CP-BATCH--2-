
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    # check if any window of size k is all '1'
    bad = False
    cnt = 0

    for i in range(n):
        if s[i] == '1':
            cnt += 1

        if i >= k:
            if s[i - k] == '1':
                cnt -= 1

        if i >= k - 1 and cnt == k:
            bad = True

    if bad:
        print("NO")
        continue

    ones = []
    zeros = []

    for i in range(n):
        if s[i] == '1':
            ones.append(i)
        else:
            zeros.append(i)

    p = [0] * n
    val = n

    for i in zeros:
        p[i] = val
        val -= 1

    for i in ones:
        p[i] = val
        val -= 1

    print("YES")
    print(*p)
