
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    mism = []

    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            mism.append(i)

    if not mism:
        print("Yes")
    else:
        if max(mism) - min(mism) + 1 == len(mism):
            print("Yes")
        else:
            print("No")
