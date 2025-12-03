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

print(time)
print(signal)
# 2A. Line Chart
plt.figure(figsize=(9, 4))
plt.plot(time, signal, color='steelblue', linewidth=2, label='JamesD Sensor signal')
plt.title('JamesD: Signal Over Time')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True, alpha=0.3)

plt.show()

# 2B. Scatter Plot
sales = np.linspace(50, 200, 50)
costs = 40 + 1.8 * sales + np.random.normal(0, 30, 50)

plt.figure(figsize=(9, 4))
plt.scatter(sales, costs, c='darkorange', edgecolor='black', alpha=0.8, label='JamesD Samples')
plt.title('JamesD: Costs vs Sales')
plt.xlabel('Sales ($k)')
plt.ylabel('Costs ($k)')
plt.legend()
plt.grid(True, alpha=0.9)

plt.show()

# 3. Output