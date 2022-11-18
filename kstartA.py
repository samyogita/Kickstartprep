def solve(i, p):
    l = r = 0
    count = 0
    while l < len(i) and r < len(p):
        if i[l] == p[r]:
            l += 1
            r += 1
        else:
            r += 1
            count += 1
    count += len(p) - r
    if l != len(i):
        return('IMPOSSIBLE')
    else:
        return(count)
    
t = int(input())
for T in range(1, t+1):
    i = input()
    p = input()
    ans = solve(i,p)
    print(f'Case #{T}: {ans}')

