import numpy as np
import matplotlib.pyplot as plt
import matplotlib

fontsize = 15
matplotlib.rcParams.update({'font.size': fontsize})

riscv_total_bits = 1264
riscv_bits = [4, 8, 16, 24, 32, 40, 48, 56, 64]
# riscv_secs = [148, 410, 1341, 10804, 10630, 36360, 59880, 108720, 232800]
# riscv_secs = [148, 410, 1341, 10804, 10630, 36360, 51880, 83720, 272800]
riscv_secs = [148, 410, 1341, 10804, 10630, 36360, 51880, 73720, 272800]

riscv_percentage = [bits/riscv_total_bits*100 for bits in riscv_bits]
riscv_hrs = [sec/3600 for sec in riscv_secs]

# riscv_lim_bits = riscv_bits[-1] + [64]
# riscv_lim_secs = riscv_secs[-1] + [232800]
# riscv_lim_secs = riscv_bits[-1] + [128]

gps_total_bits = 1008
gps_bits = [4, 8, 12, 16, 24, 32, 48, 64, 80, 96, 112, 128]
gps_secs = [560, 1190, 2520, 4200, 5285, 5280, 8580, 18600, 25900, 38420, 82600, 359200]

gps_percentage = [bits/gps_total_bits*100 for bits in gps_bits]
gps_hrs = [sec/3600 for sec in gps_secs]

fig, ax = plt.subplots(figsize=(9, 5))
#
# lut_bits = [4, 8, 16, 32]
# lut_secs = [148, 410, 1341, 10630]
#
# lut_bits = [4, 8, 16, 32]
# lut_secs = [148, 410, 1341, 10630]

# riscv_plot, = ax.plot(riscv_percentage, riscv_hrs, label = 'Obfus. RISC-V')
# gps_plot, = ax.plot(gps_percentage, gps_hrs, label = 'Obfus. GPS')
# plt.xlabel('Percentage of obfuscated bits (%)')

riscv_plot, = ax.plot(riscv_bits, riscv_hrs, label = 'Obfus. RISC-V', marker = 'o', markersize = 8)
# riscv_lim_plot, = ax.plot([riscv_bits[-1], 64], [riscv_hrs[-1], 35], linestyle='dashed', color='b')
gps_plot, = ax.plot(gps_bits, gps_hrs, label = 'Obfus. GPS', marker = 'o', markersize = 8)
# riscv_lim_plot, = ax.plot([gps_bits[-1], 128], [gps_hrs[-1], 30], linestyle='dashed', color='darkorange')

plt.xlabel('Number of key bits')
# plt.text(545, 80, '3 days', fontsize=fontsize-1, color = 'r')
# plt.text(97, 10, 'Fully obfuscated', fontsize=fontsize, color = 'r', rotation=90)
# plt.text(250, 80, '3 days', fontsize=fontsize, color = 'r')

# line, = plt.plot([0, 1450], [72, 72], label = '3 days', color = 'r', ls = '--')
# line, = plt.plot([10, 100], [72, 72], label = '3 days', color = 'r', ls = '--')

# plt.axhline(y=72, color = 'r', ls = '--')
# ax.axvline(x=100, color = 'r', ls = '--')
# ax.annotate('Fully obfuscated', xy=(100, 0), xycoords='data', )
ax.legend(handles=[riscv_plot, gps_plot], loc='upper right')

ax.annotate('Total key bits\nin obfus.\nRISCV\n(1264)',
            xy=(1264, 0.027842324061978303), xycoords='data',
            xytext=(0, 25), textcoords='offset points',
            # color = riscv_plot.get_color(),
            arrowprops=dict(arrowstyle="->", linewidth = 2, color = riscv_plot.get_color()),
            horizontalalignment='center', verticalalignment='bottom', fontsize = fontsize-1)

ax.annotate('Total key bits\nin obfus. GPS\n(1008)',
            xy=(1008, 0.0278423240619783033), xycoords='data',
            xytext=(0, 25), textcoords='offset points',
            # color = gps_plot.get_color(),
            arrowprops=dict(arrowstyle="->", linewidth = 2, color = gps_plot.get_color()),
            horizontalalignment='center', verticalalignment='bottom', fontsize = fontsize-1)


# ax.annotate('Fully\nobfuscated',
#             xy=(100, 0.03), xycoords='data',
#             xytext=(0, 25), textcoords='offset points',
#             arrowprops=dict(facecolor='black', arrowstyle="->", linewidth = 2),
#             horizontalalignment='center', verticalalignment='bottom', fontsize = fontsize-1)

plt.ylabel('SAT execution time (hrs)')
# ax.set_ylim(0, 26)
# ax.set_ylim(0, 82)
ax.set_xlim(0, 1450)
# ax.set_xlim(0, 110)
ax.set_yscale("log")
print(ax.get_ylim())
plt.show()