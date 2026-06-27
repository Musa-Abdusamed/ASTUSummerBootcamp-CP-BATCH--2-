import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # count ones on left, zeros on right
    left  = 0  
    right = n-1  
    ops   = 0
    
    while left < right:
        while left < right and a[left] == 0:
            left += 1        
        while left < right and a[right] == 1:
            right -= 1       
        if left < right:
            ops += 1         
            left  += 1
            right -= 1
    
    print(ops)

t = int(input())
for _ in range(t):
    solve()
