def sum_recur(n):
    if n==1 or n==0:
        return 1
    return n+sum_recur(n-1)
g = int(input())
f = sum_recur(g)
print(f)
