import psutil
import platform


def bytes_to_mb(bytes_value):
    return bytes_value / 1024 / 1024


def print_task_manager():
    print(f"{'PID':>6} {'Name':<25} {'CPU %':>6} {'Memory MB':>10}")
    print("-" * 50)

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
        try:
            pid = proc.info['pid']
            name = proc.info['name'][:25]  # limit name length
            cpu = proc.info['cpu_percent']
            mem = bytes_to_mb(proc.info['memory_info'].rss)
            print(f"{pid:>6} {name:<25} {cpu:>6.1f} {mem:>10.2f}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


if __name__ == "__main__":
    print(f"Platform: {platform.system()} {platform.release()}")
    print_task_manager()
    # Print overall CPU and memory usage
    print("\nOverall system usage:")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    mem = psutil.virtual_memory()
    print(f"RAM Usage: {mem.percent}% ({bytes_to_mb(mem.used):.2f} MB / {bytes_to_mb(mem.total):.2f} MB)")
