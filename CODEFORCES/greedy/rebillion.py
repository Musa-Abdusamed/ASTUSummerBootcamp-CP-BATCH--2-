
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total_zeros = a.count(0)

    pref = 0
    min_pref = 0

    for x in a:
        if x == 1:
            pref += 1
        else:
            pref -= 1
        min_pref = min(min_pref, pref)

    print(total_zeros + min_pref)
