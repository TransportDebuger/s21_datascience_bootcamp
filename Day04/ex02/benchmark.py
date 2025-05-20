import timeit
import sys

def get_gmail_loop(emails):
    result = []
    for email in emails:
        if email.endswith('@gmail.com'):
            result.append(email)
    return result

def get_gmail_comprehension(emails):
    return [email for email in emails if email.endswith('@gmail.com')]

def get_gmail_map(emails):
    mapped = map(lambda e: e if e.endswith('@gmail.com') else None, emails)
    return mapped

def get_gmail_filter(emails):
    return list(filter(lambda e: e.endswith('@gmail.com'), emails))

def parse_command_line_args():
    if len(sys.argv) != 3:
        print("Usage: ./benchmark.py <function_name> <number_of_calls>")
        print("Available function names: loop, list_comprehension, map, filter")
        sys.exit(1)

    func_name = sys.argv[1]
    try:
        calls = int(sys.argv[2])
    except ValueError:
        print("Number of calls must be an integer")
        sys.exit(1)

    return func_name, calls

def benchmark(func_name, calls):
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

    funcs = {
        'loop': lambda: get_gmail_loop(emails),
        'list_comprehension': lambda: get_gmail_comprehension(emails),
        'map': lambda: get_gmail_map(emails),
        'filter': lambda: get_gmail_filter(emails),
    }

    if func_name not in funcs:
        print(f"Unknown function name '{func_name}'. Available: loop, list_comprehension, map, filter")
        sys.exit(1)

    time = timeit.timeit(funcs[func_name], number=calls)
    print(time)

if __name__ == '__main__':
    try:
        func_name, calls = parse_command_line_args()
        benchmark(func_name, calls)

    except Exception as e:
        print(f"An error occurred: {e}")