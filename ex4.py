def golden_ratio(i):
    fib = [1, 1]
    for j in range(i-1):
        fib.append(fib[-1] + fib[-2])
    return fib[-1] / fib[-2]


golden_ratio(2)