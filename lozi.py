n = int(input("tol ertefa ra vared konid: "))

for x in range(n):
    print(" " * (n - x), "*" * (2*x + 1))
for x in range(n - 2, -1, -1):
    print(" " * (n - x), "*" * (2*x + 1))
