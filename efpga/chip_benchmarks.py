import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 15})

td_fp = [3584, 4059, 5912, 5731, 4833, 5815]
td_nofp = [3565, 3965, 6024, 5602, 4599, 5491]
bu_fp = [4823, 5763, 7116, 7369, 6483, 7247]
bu_nofp = [5844, 8536, 7370, 7609, 8169, 7473]
buopt_fp = [4230, 4971, 7059, 6570, 5612, 6956]
buopt_nofp = [4220, 4966, 6828, 6641, 5560, 6567]
N = len(td_fp)

fig, ax = plt.subplots(figsize=(9, 4))
# ax.set_aspect(1)

ind = np.arange(N)    # the x locations for the groups
width = 0.32         # the width of the bars
p1 = ax.bar(ind, td_nofp, width, bottom=0)
p2 = ax.bar(ind + width, buopt_fp, width, bottom=0)

# ax.set_title('Scores ')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('aes-sbox', 'cbc', 'mul32a', 'c1423', 'i9', 'too-lrg'))

ax.legend((p1[0], p2[0]), ('Top-Down (w/o FP)', 'Bottom-Up (w/ FP)'))
ax.autoscale_view()

plt.xlabel('Benchmark')
plt.ylabel('Delay (ps)')

plt.show()