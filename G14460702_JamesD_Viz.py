#
# G14460702, 2025/12/03
# File: G14460702_JamesD_Viz.py
# Short description of the task
#
import matplotlib.pyplot as plt
import numpy as np
# 1. Input
time = np.linspace(0, 10, 100)
signal = np.sin(time) + 0.2 * np.random.randn(100)

# 2. Process
plt.figure(figsize=(9, 4))
plt.plot(time, signal, color='steelblue', linewidth=2, label='Sensor signal')
plt.title('Signal Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 3. Output