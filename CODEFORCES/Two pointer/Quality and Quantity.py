
def solve():
    n = int(input())
    a = sorted(map(int, input().split()))

    blue = a[0] + a[1]
    red = a[-1]

    l = 2
    r = n - 2

    while l <= r:
        if red > blue:
            print("YES")
            return

        blue += a[l]
        red += a[r]
        l += 1
        r -= 1

    if red > blue:
        print("YES")
    else:
        print("NO")


t = int(input())
for _ in range(t):
    solve()
