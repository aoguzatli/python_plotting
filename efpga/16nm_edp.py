import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import xlrd

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


fig, axes = plt.subplots(2, 2, figsize=(9, 6.5))

# Pareto plot
ax = axes[1, 0]
plots = []
for i, app in enumerate(apps):
    plot, = ax.plot(delays[app], energies[app], marker='o', label = apps[i])
    plots.append(plot)

ax.set_xlabel('Delay (ns)\n(c)')
ax.set_ylabel('Energy (pJ)')
ax.legend(handles=plots, loc='upper right')
ax.grid(True)

# EDP plot
ax = axes[1, 1]
plots = []
for i, app in enumerate(apps):
    plot, = ax.plot(vdds[app], edps_norm[app], marker='o', label = apps[i])
    plots.append(plot)

ax.set_xlabel('VDD (V)\n(d)')
ax.set_ylabel('Normalized EDP')
ax.legend(handles=plots, loc='upper right')
ax.grid(True)

# EDP plot
ax = axes[0, 0]
plots = []
for i, app in enumerate(apps):
    plot, = ax.plot(vdds[app], delays[app], marker='o', label = apps[i])
    plots.append(plot)

ax.set_xlabel('VDD (V)\n(a)')
ax.set_ylabel('Delay (ns)')
ax.legend(handles=plots, loc='upper right')
ax.grid(True)

# EDP plot
ax = axes[0, 1]
plots = []
for i, app in enumerate(apps):
    plot, = ax.plot(vdds[app], powers[app], marker='o', label = apps[i])
    plots.append(plot)

ax.set_xlabel('VDD (V)\n(b)')
ax.set_ylabel('Power (mW)')
ax.legend(handles=plots, loc='upper right')
ax.grid(True)

plt.show()