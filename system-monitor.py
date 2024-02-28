

import random

# Simulate system parameters
cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_space = random.randint(0, 100)

# Function to check and print alerts
def check_and_alert(parameter_name, parameter_value, threshold):
    
    if parameter_value > threshold:
        print(f"High {parameter_name} usage! Current usage: {parameter_value}%")

# Check CPU usage
check_and_alert("CPU", cpu_usage, 90)

# Check memory usage
check_and_alert("Memory", memory_usage, 90)

# Check disk space
check_and_alert("Disk space", disk_space, 90)

pass
