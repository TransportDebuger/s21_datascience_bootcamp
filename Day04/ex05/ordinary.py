import sys
import time

def read_all_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return lines

def get_stats(start_time):
    if sys.platform == 'win32':
        import psutil
        import os
        process = psutil.Process(os.getpid())
        mem_info = process.memory_info()
        peak_memory = getattr(mem_info, 'peak_wset', mem_info.rss)
        peak_memory_gb = peak_memory / (1024 ** 3)
        cpu_times = process.cpu_times()
        cpu_time = cpu_times.user + cpu_times.system
    else:
        import resource
        usage = resource.getrusage(resource.RUSAGE_SELF)
        if sys.platform == 'darwin':
            peak_memory_gb = usage.ru_maxrss / (1024 ** 3)
        else:
            peak_memory_gb = usage.ru_maxrss / (1024 ** 2)
        cpu_time = usage.ru_utime + usage.ru_stime

    return peak_memory_gb, cpu_time

def main():
    if len(sys.argv) != 2:
        print("Usage: python ordinary.py <path_to_ratings.csv>")
        sys.exit(1)

    filepath = sys.argv[1]
    start_time = time.time()

    lines = read_all_lines(filepath)
    for line in lines:
        pass

    peak_mem, cpu_t = get_stats(start_time)
    print(f"Peak Memory Usage = {peak_mem:.3f} GB")
    print(f"User Mode Time + System Mode Time = {cpu_t:.2f}s")

if __name__ == '__main__':
    main()