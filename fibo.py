def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    c = 0
    while c < n:
        c = a + b
        a = b
        b = c
        if(c>n):
            break
        else:
            print(c)


fib(1000)
