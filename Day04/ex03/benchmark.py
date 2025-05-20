import sys
import timeit
from functools import reduce

def sum_squares_loop(n):
    """Суммирует квадраты чисел от 1 до n включительно с помощью цикла."""
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def sum_squares_reduce(n):
    """Суммирует квадраты чисел от 1 до n включительно с помощью reduce."""
    return reduce(lambda acc, x: acc + x * x, range(1, n + 1), 0)

def parse_args():
    """Парсит и проверяет аргументы командной строки."""
    if len(sys.argv) != 4:
        print("Usage: ./benchmark.py <function_name> <number_of_calls> <number>")
        print("function_name: loop or reduce")
        sys.exit(1)

    func_name = sys.argv[1]
    if func_name not in ('loop', 'reduce'):
        print("Function name must be 'loop' or 'reduce'")
        sys.exit(1)

    try:
        calls = int(sys.argv[2])
        number = int(sys.argv[3])
    except ValueError:
        print("Number of calls and number must be integers")
        sys.exit(1)

    return func_name, calls, number

def benchmark(func_name, calls, number):
    funcs = {
        'loop': lambda: sum_squares_loop(number),
        'reduce': lambda: sum_squares_reduce(number),
    }

    time = timeit.timeit(funcs[func_name], number=calls)
    print(time)

if __name__ == '__main__':
    try:
        func_name, calls, number = parse_args()
        benchmark(func_name, calls, number)
    except Exception as e:
        print(f"An error occurred: {e}")