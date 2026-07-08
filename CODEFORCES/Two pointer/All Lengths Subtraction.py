
def solve():
    n = int(input())
    need = list(map(int, input().split()))

    for k in range(n, 0, -1):
        found = False

        for l in range(n - k + 1):
            ok = True
            for i in range(l, l + k):
                if need[i] == 0:
                    ok = False
                    break

            if ok:
                for i in range(l, l + k):
                    need[i] -= 1
                found = True
                break

        if not found:
            print("NO")
            return

    print("YES")


t = int(input())
for _ in range(t):
    solve()
