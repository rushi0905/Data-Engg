def fibonacci_series(n):
    a,b = 0,1
    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
fibonacci_series(10)  # Output: 0 1 1 2 3 5 8 13 21 34