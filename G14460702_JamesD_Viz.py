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

# 2C. Histogram
seed_value = 2021
myrandom = np.random.default_rng(seed_value)
data = myrandom.normal(loc=70, scale=15, size=200)

plt.figure(figsize=(7, 4))
plt.hist(data, bins=15, color='slateblue', edgecolor='white', alpha=0.8)
plt.title('Histogram of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')

plt.show()

# 2D. Boxplot
plt.figure(figsize=(5, 4))
plt.boxplot(data, vert=True, patch_artist=True,
            boxprops=dict(facecolor='lightgreen', color='darkgreen'),
            medianprops=dict(color='black'))
plt.title('Box Plot of Scores')
plt.ylabel('Score')

plt.show()

# 2E. Bar Plots
categories = ['A', 'B', 'C', 'D']
values = [120, 95, 140, 110]

plt.figure(figsize=(10, 5))
plt.bar(categories, values, color=['#4C72B0', '#55A868', '#C44E52', '#8172B3'])
plt.title('Category Performance')
plt.ylabel('Value')
plt.show()

# 2F. Subplots
fig, axes = plt.subplots(1, 2, figsize=(10, 5))

x = np.linspace(0, 5, 50)
axes[0].plot(x, np.exp(-x), color='teal', linewidth=2)
axes[0].set_title('Exponential Decay')
axes[0].grid(True, alpha=0.3)

axes[1].scatter(np.random.randn(50), np.random.randn(50), c='firebrick', alpha=0.7)
axes[1].set_title('Random Scatter')
axes[1].grid(True, alpha=0.3)

fig.suptitle('Two-Panel Subplot Layout', y=0.98)
plt.tight_layout()

plt.show()

# 3. Output