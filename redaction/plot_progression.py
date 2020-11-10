import numpy as np
import matplotlib.pyplot as plt
import matplotlib

with open('sat_progression.txt') as f:
    lines = f.readlines()
    iters = [int(line.split()[3][:-1]) for line in lines]
    clauses = [int(line.split()[5][:-1]) for line in lines]
    vars = [int(line.split()[7][:]) for line in lines]

experiments = []
for i in range(3):
    experiments.append([])
    experiment = experiments[i]
    for j in range(300):
        indices = [k for k, n in enumerate(iters) if n == j]
        if len(indices) <= i:
            break

        index = indices[i]
        experiment.append((clauses[index], vars[index]))

fig, ax = plt.subplots(figsize=(9, 5))

for i in range(3):
    exp = experiments[i]
    ax.plot(range(len(exp)), [trial[1] for trial in exp], label = f'Expt {i}')

plt.xlabel('Iteration')
plt.ylabel('Clauses')

# ax.legend(handles=[riscv_true_plot, riscv_false_plot], loc='upper left')


# ax.set_xlim(0, 1450)
# # ax.set_xlim(0, 110)
# ax.set_yscale("log")
# print(ax.get_ylim())
plt.show()
