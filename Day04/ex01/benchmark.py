import timeit

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

def benchmark():
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com', 'anna@live.com', 'philipp@gmail.com'] * 5

    def loop_func():
        get_gmail_loop(emails)

    def comp_func():
        get_gmail_comprehension(emails)

    def map_func():
        get_gmail_map(emails)

    loop_time = timeit.timeit(loop_func, number=90_000_000)
    comp_time = timeit.timeit(comp_func, number=90_000_000)
    map_time = timeit.timeit(map_func, number=90_000_000)

    min_time = min(loop_time, comp_time, map_time)
    if min_time == map_time:
        print("it is better to use a map")
    elif min_time == comp_time:
        print("it is better to use a list comprehension")
    else:
        print("it is better to use a loop")

    times_sorted = sorted([loop_time, comp_time, map_time])
    print(f"{times_sorted[0]} vs {times_sorted[1]} vs {times_sorted[2]}")

if __name__ == '__main__':
    try:
        benchmark()
    except Exception as e:
        print(f"An error occurred: {e}")