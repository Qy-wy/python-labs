import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10, 10)

fig, ax = plt.subplots(figsize=(6, 6))

heatmap = ax.imshow(data, cmap='viridis')

ax.set_title('Тепловая карта 10x10', fontsize=14)

plt.tight_layout()
plt.savefig('4_plot.png', dpi=300)
plt.show()
