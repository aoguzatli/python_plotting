import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.colors import ListedColormap

cmap = ListedColormap(['indianred', 'green'])
vdds = [0.6, 0.7, 0.8, 0.9, 1.0]
#freqs = [368, 684, 820, 1032, 1362]
freqs = [368, 684, 820, 1051, 1362]

num_cells_y = len(vdds)
num_cells_x = 2*num_cells_y
# num_cells_x = 12

xlims = [0, 1500]
delta_x = (xlims[1] - xlims[0]) / num_cells_x
num_squares = [math.floor((freq-xlims[0])/delta_x) for freq in freqs]
freq_lims = [round(xlims[0] + i*delta_x) for i in range(num_cells_x+1)]

# Reverse y axis because origin is at top-left
vdds.reverse()
num_squares.reverse()

image = np.zeros((num_cells_y, num_cells_x))
for j in range(num_cells_y):
    for i in range(num_squares[j]):
        image[j, i] = 1

print(image)

fig, ax = plt.subplots()

row_labels = range(num_cells_y)
ax.imshow(image, cmap=cmap, aspect = 2)


plt.yticks(range(num_cells_y), vdds)

freq_lims = [i if i%2 == 0 else '' for i in freq_lims ]
ax.set_xticks(np.arange(-.5, num_cells_x, 1), minor=True)
ax.set_yticks(np.arange(-.5, num_cells_y, 1), minor=True)
ax.set_xticklabels(freq_lims, minor=True)
ax.set_xticklabels([], minor=False)

ax.tick_params(axis='y', which='major', length=0)
ax.tick_params(axis='x', which='major', length=0)

# ax.text(5, 2, 'PASS', color='w', fontsize=16, fontweight='bold')
# ax.text(17, 5, 'FAIL', color='w', fontsize=16, fontweight='bold')

ax.grid(True, which='minor')

ax.set_xlabel('Frequency (MHz)')
ax.set_ylabel('VDD (V)')
# fig.tight_layout()
plt.show()
