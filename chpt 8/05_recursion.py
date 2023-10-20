# n = int(input("enter the no"))
# product = 1
# for i in range(n):
#     product = product*(i+1)
# print(product)

# def fact_iter(n):
#     product = 1
#     for i in range(n):
#         product = product*(i+1)
#     return product
# g = int(input())
# f = fact_iter(g)
# print(f)

def fact_recur(n):
    if n==1 or n==0:
        return 1
    return n*fact_recur(n-1)
g = int(input())
f = fact_recur(g)
print(f)

