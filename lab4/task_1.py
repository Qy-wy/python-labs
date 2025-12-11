import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 6, 300)

y1 = np.cos(x)**2 - x/5
y2 = np.exp(-0.3*x) * np.sin(5*x)

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(x, y1, 'b', label='y1 = cos^2(x) - x/5')
ax1.set_xlabel("x")
ax1.set_ylabel("y1", color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()
ax2.plot(x, y2, 'r', label='y2 = exp(-0.3x) * sin(5x)')
ax2.set_ylabel("y2", color='r')
ax2.tick_params(axis='y', labelcolor='r')

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper right", ncol=1)

x_max = x[np.argmax(y1)]
y_max = np.max(y1)
ax1.annotate(
    "Максимум y1",
    xy=(x_max, y_max),
    xytext=(x_max + 0.3, y_max + 0.2),
    arrowprops=dict(arrowstyle="->", color='blue')
)

x_min = x[np.argmin(y2)]
y_min = np.min(y2)
ax2.annotate(
    "Минимум y2",
    xy=(x_min, y_min),
    xytext=(x_min + 0.3, y_min + 0.2),
    arrowprops=dict(arrowstyle="->", color='blue')
)

plt.title("Графики двух функций")
plt.grid(True)
plt.show()
