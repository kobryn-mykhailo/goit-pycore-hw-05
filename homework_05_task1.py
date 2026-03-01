# hw.05 Task 1: Fibonacci with caching using closures

def caching_fibonacci():
    # create empty dictionary to store already calculated results
    cache = {}

    def fibonacci(n):
        # base cases: fibonacci of 0 is 0, fibonacci of 1 is 1
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # check if we already calculated this number before
        if n in cache:
            return cache[n]

        # calculate fibonacci and save result to cache for future use
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # return the inner function that remembers cache between calls
    return fibonacci


# get the fibonacci function with caching
fib = caching_fibonacci()

# test the function
print(fib(10))  # 55
print(fib(15))  # 610