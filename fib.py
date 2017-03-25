def fib(n):
        a = 0
        b = 1
        for i in xrange(n):
                a,b = a + b, a
                print a

fib(20)
