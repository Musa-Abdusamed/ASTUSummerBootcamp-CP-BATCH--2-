
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    target = s[-1]
    ans = 0

    for ch in s:
        if ch != target:
            ans += 1

    print(ans)
  
