def f1(n):
    if n==0:return
    print("hello, n:", n)
    f1(n-1)
f1(5)