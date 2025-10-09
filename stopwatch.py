# stopwatch.py
import time
print("Press ENTER to start the stopwatch")
print("Press Ctrl + C to stop")
input()
print("Stopwatch started...")
start_time = time.time()
try:
    while True:
        elapsed_time = round(time.time() - start_time, 2)
        print(f"\rElapsed Time: {elapsed_time} seconds", end="")
        time.sleep(0.1)
except KeyboardInterrupt:
    print(f"\nFinal Time: {elapsed_time} seconds")
    print("Stopwatch stopped.")