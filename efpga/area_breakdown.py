import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams.update({'font.size': 15})

labels = ['Crossbar', 'BLE', 'CLB Config', 'Routing', 'Routing Config', 'Other']
colors = ['royalblue', 'cornflowerblue', 'lightsteelblue', 'brown', 'lightcoral', 'dimgray']
hatches = ['//'] * 3 + ['x'] * 2 + ['']
metrics = ['Instances', 'Area', 'Delay']

areas = [0.34, 0.09, 0.25,  0.23, 0.1, 0.13]
insts = [1.3, 0.28, 0.21, 0.765, 0.08, 0.27]
delays = [0.205, 0.355, 0, 0.44, 0, 0]
N = len(labels)

pct_insts = [i/sum(insts) for i in insts]
pct_areas = [i/sum(areas) for i in areas]
pct_delays = [i/sum(delays) for i in delays]

fig, ax = plt.subplots(figsize=(9, 5))

ind = np.arange(3)    # the x locations for the groups
width = 0.65         # the width of the bars

prev_insts = 0
prev_areas = 0
prev_delays = 0
plots = []
for i in range(N):
    plots.append(ax.bar(ind, [pct_insts[i], pct_areas[i], pct_delays[i]], width, label = labels[i],
                        bottom=[prev_insts, prev_areas, prev_delays], color = colors[i], hatch = hatches[i]))
    prev_delays += pct_delays[i]
    prev_areas += pct_areas[i]
    prev_insts += pct_insts[i]


# plt.ylabel('Percentage')
# plt.title('Scores by group and gender')
plt.xticks(ind, metrics)
# plt.yticks(np.arange(0, 81, 10))
# plt.legend((p1[0], p2[0]), ('Men', 'Women'))
# plt.legend(loc = 'upper right')
ax.legend(handles=plots[::-1], loc='upper right', fontsize = 12)
plt.show()


# ax.set_title('Scores ')
# ax.set_xticks(ind + width / 2)
# ax.set_xticklabels(('aes-sbox', 'cbc', 'mul32a', 'c1423', 'i9', 'too-lrg'))
#

# ax.autoscale_view()
#
# plt.xlabel('Benchmark')
# plt.ylabel('Delay (ps)')
#
# plt.show()