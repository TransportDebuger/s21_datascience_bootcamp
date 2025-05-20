import timeit
import random
from collections import Counter

def generate_list():
    """Генерирует список из 1 000 000 случайных чисел от 0 до 100."""
    return [random.randint(0, 100) for _ in range(1_000_000)]

def count_numbers_myfunc(numbers):
    """Подсчёт количества чисел с помощью словаря (без Counter)."""
    counts = {i: 0 for i in range(101)}
    for num in numbers:
        counts[num] += 1
    return counts

def top_10_myfunc(numbers):
    """Поиск топ-10 чисел с наибольшим количеством (без Counter)."""
    counts = count_numbers_myfunc(numbers)
    # Сортируем по убыванию количества и берём первые 10
    top_10 = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
    return dict(top_10)

def count_numbers_counter(numbers):
    """Подсчёт количества чисел с помощью Counter."""
    return Counter(numbers)

def top_10_counter(numbers):
    """Поиск топ-10 чисел с помощью Counter.most_common()."""
    c = Counter(numbers)
    return dict(c.most_common(10))

def benchmark():
    numbers = generate_list()

    time_my_count = timeit.timeit(lambda: count_numbers_myfunc(numbers), number=1)
    time_counter_count = timeit.timeit(lambda: count_numbers_counter(numbers), number=1)

    time_my_top = timeit.timeit(lambda: top_10_myfunc(numbers), number=1)
    time_counter_top = timeit.timeit(lambda: top_10_counter(numbers), number=1)

    print(f"my function: {time_my_count}")
    print(f"Counter: {time_counter_count}")
    print(f"my top: {time_my_top}")
    print(f"Counter's top: {time_counter_top}")

if __name__ == '__main__':
    benchmark()