from typing import Callable
import timeit


def fib_hash(n: int, memo: dict[int, int] = {}):
    """Generate Fibonacci series using memoization / caching"""
    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_hash(n - 1, memo) + fib_hash(n - 2, memo)
    return memo[n]


def fib(n: int):
    """Generate Fibonacci series without any memoization / caching."""
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)


def benchmark(func: Callable, *args, number=1000):
    """Benchmark time-cost of any functions.

    Args:
        func (Callable): Function signature for benchmarking.
        number (int, optional): Number of times the function will be executed.
    """
    argv = ", ".join([str(a) for a in args])
    print(f"Executing {func.__name__}({argv}) for {number} times.")

    timer = timeit.Timer(lambda: func(*args))
    elapsed_time = timer.timeit(number=number)

    print(f"{func.__name__} executed {number} times in {elapsed_time:.4f} seconds")


if __name__ == "__main__":
    n = 40
    benchmark(fib, n, number=100)
    benchmark(fib_hash, n, number=1000)
