
t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    left = [-1] * n
    mn = p[0]
    mn_idx = 0

    for i in range(1, n):
        if p[i] > mn:
            left[i] = mn_idx
        if p[i] < mn:
            mn = p[i]
            mn_idx = i

    right = [-1] * n
    mn = p[-1]
    mn_idx = n - 1

    for i in range(n - 2, -1, -1):
        if p[i] > mn:
            right[i] = mn_idx
        if p[i] < mn:
            mn = p[i]
            mn_idx = i

    found = False
    for j in range(n):
        if left[j] != -1 and right[j] != -1:
            print("YES")
            print(left[j] + 1, j + 1, right[j] + 1)
            found = True
            break

    if not found:
        print("NO")
