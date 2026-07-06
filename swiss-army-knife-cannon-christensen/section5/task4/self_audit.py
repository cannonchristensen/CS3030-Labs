# Memory peak observed during testing: 213209088 bytes.

import os
import psutil
import random

# Get process ID
process = psutil.Process(os.getpid())

# Store memory and CPU times
memory = process.memory_info().rss
cpu_times = process.cpu_times()

# Print results
print(f'Before:\nMemory: {memory} bytes\nCPU time: {cpu_times.user+cpu_times.system}')

# Make 5,000,000 random numbers
numbers = [random.randint(1, 10000) for _ in range(5000000)]

# Update memory and CPU times
memory = process.memory_info().rss
cpu_times = process.cpu_times()

# Print results
print(f'After:\nMemory: {memory} bytes\nCPU time: {cpu_times.user+cpu_times.system}')