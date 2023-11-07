def fibonacci(n):
    fib_list = [0, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

def sum_fibonacci(n):
    fib_list = fibonacci(n)
    return sum(fib_list)

n = 50
result = sum_fibonacci(n)
print(f"The sum of the first {n} Fibonacci numbers is: {result}")
