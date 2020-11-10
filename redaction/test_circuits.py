import numpy as np
import matplotlib.pyplot as plt
import matplotlib

# matplotlib.rcParams.update({'font.size': 22})
matplotlib.rcParams['xtick.labelsize'] = 9

gps = False

schemes = np.array(['original', 'eFPGA_generic', 'eFPGA_opt'])
if gps:
    metrics = np.array(['Delay\n(normalized to 0.98ns)', 'Power\n(normalized to 75.9mW)', 'Area\n(normalized to 96.0Kµm2)'])
else:
    metrics = np.array(['Delay\n(normalized to 1.55ns)', 'Power\n(normalized to 15.0mW)', 'Area\n(normalized to 4.28Kµm2)'])
N = metrics.shape[0]

stats_gps_orig = np.array([0.98, 75.9, 96])
stats_gps_efpga_gen = np.array([3.21, 103.7, 134])
stats_gps_efpga_opt = np.array([0.98, 110.7, 133])

stats_riscv_orig = np.array([1.55, 15.0, 4.28])
stats_riscv_efpga_gen = np.array([8.47, 25.7, 8.80])
stats_riscv_efpga_opt = np.array([3.66, 21.0, 8.08])


fig, ax = plt.subplots(figsize=(9*0.8, 4.2*0.8))
ind = np.arange(N)    # the x locations for the groups
width = 0.22         # the width of the bars

if gps:
    p1 = ax.bar(ind + 0*width, stats_gps_orig / stats_gps_orig, width, bottom=0)
    p2 = ax.bar(ind + 1*width, stats_gps_efpga_gen / stats_gps_orig, width, bottom=0)
    p3 = ax.bar(ind + 2*width, stats_gps_efpga_opt / stats_gps_orig, width, bottom=0)
else:
    p1 = ax.bar(ind + 0*width, stats_riscv_orig / stats_riscv_orig, width, bottom=0)
    p2 = ax.bar(ind + 1*width, stats_riscv_efpga_gen / stats_riscv_orig, width, bottom=0)
    p3 = ax.bar(ind + 2*width, stats_riscv_efpga_opt / stats_riscv_orig, width, bottom=0)

ax.set_xticks(ind + width * 1)
ax.set_xticklabels(metrics)

ax.legend((p1[0], p2[0], p3[0]), schemes)

if gps:
    ax.set_ylim([0, 4])
else:
    ax.set_ylim([0, 7])

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{:.2f}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(p1)
autolabel(p2)
autolabel(p3)
plt.show()
