import matplotlib.pyplot as plt
import numpy as np
import xlrd, math
from matplotlib.colors import ListedColormap

cmap = ListedColormap(['indianred', 'green'])
apps = ['sbox', 'aes', 'mul18', 'sobel']
wb = xlrd.open_workbook(r"C:\Users\Ahmet Oguz Atli\OneDrive\CMU\Research\eFPGA_paper\16nmFPGA_DATA.xlsx")

vdds = {}
freqs = {}
delays = {}
itotals = {}
powers = {}
energies = {}
edps = {}
edps_norm = {}

for i, app in enumerate(apps):
    sheet = wb.sheet_by_index(i)
    vdds[app] = [float(cell.value) for cell in sheet.col(0)[2:]]
    freqs[app] = [float(cell.value) for cell in sheet.col(1)[2:]]
    itotals[app] = [float(cell.value) for cell in sheet.col(4)[2:]]

    delays[app] = [1000/freq for freq in freqs[app]]
    powers[app] = [vdds[app][j]*itotals[app][j] for j in range(len(vdds[app]))]
    energies[app] = [powers[app][j]*delays[app][j] for j in range(len(powers[app]))]
    edps[app] = [energies[app][j]*delays[app][j] for j in range(len(energies[app]))]
    edps_norm[app] = [edps[app][j] / max(edps[app]) for j in range(len(energies[app]))]

app = 'sbox'
num_cells_y = len(vdds[app])
num_cells_x = 4*num_cells_y

xlims = [0, 700]
delta_x = (xlims[1] - xlims[0]) / num_cells_x
num_squares = [math.floor((freq-xlims[0])/delta_x) for freq in freqs[app]]
freq_lims = [round(xlims[0] + i*delta_x) for i in range(num_cells_x+1)]

# Reverse y axis because origin is at top-left
vdds[app].reverse()
num_squares.reverse()

image = np.zeros((num_cells_y, num_cells_x))
for j in range(num_cells_y):
    for i in range(num_squares[j]):
        image[j, i] = 1

print(image)

fig, ax = plt.subplots()

row_labels = range(num_cells_y)
ax.imshow(image, cmap=cmap, aspect = 2)


plt.yticks(range(num_cells_y), vdds[app])

freq_lims = [i if i%2 == 0 else '' for i in freq_lims ]
ax.set_xticks(np.arange(-.5, num_cells_x, 1), minor=True)
ax.set_yticks(np.arange(-.5, num_cells_y, 1), minor=True)
ax.set_xticklabels(freq_lims, minor=True)
ax.set_xticklabels([], minor=False)

ax.tick_params(axis='y', which='major', length=0)
ax.tick_params(axis='x', which='major', length=0)

ax.text(5, 2, 'PASS', color='w', fontsize=16, fontweight='bold')
ax.text(17, 5, 'FAIL', color='w', fontsize=16, fontweight='bold')

ax.grid(True, which='minor')

ax.set_xlabel('Frequency (MHz)')
ax.set_ylabel('VDD (V)')
# fig.tight_layout()
plt.show()
