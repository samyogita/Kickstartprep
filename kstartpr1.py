t = int(input())
for T in range(1, t+1):
    n, m = map(int, input().split())
    c = list(map(int, input().split()))
    total = sum(c)
    ans = total % m
    print('Case #' + str(T)+ ': '+ str(ans) )
