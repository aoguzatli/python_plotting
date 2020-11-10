import numpy as np
import matplotlib.pyplot as plt
import matplotlib

fontsize = 15
matplotlib.rcParams.update({'font.size': fontsize})

TOTAL_BITS = 8119
USED_BITS = 4133

# NFO (OSSHNL-251): Mismatch found in the direction of terminal 'IN' in the placed master
# 'lab1/inv1/symbol' and its corresponding terminal in the switch master 'lab1/inv1/av_extracted',
# however, this terminal is printed in the netlist because the variable
# simCheckTermDirectionMismatch is either set to 'ignore' or is not set.
#
# ERROR (OSSHNL-912): Netlisting failed because terminal 'OUT' specified in placed master 'lab1/inv1/symbol'
# does not exist in switch master 'lab1/inv1/av_extracted'. To continue netlisting, either set
# the 'simCheckTermMismatchAction' to 'ignore', or set the
# 'simCheckTermMismatchAction' to 'warning' and 'nlAction' to 'ignore' for the
# missing terminal. 

def split_app(app):
    return [word[::-1] for word in app[::-1].split('_', 3)[::-1]]

def filter_app(d, prop, v):
    prop_idx = ['app', 'only_used', 'num_lut', 'num_routing', 'num_bits', 'ratio'].index(prop)
    return {key:val for key, val in d.items() if key[prop_idx] == v}

def sort(d, prop):
    prop_idx = ['app', 'only_used', 'num_lut', 'num_routing', 'num_bits', 'ratio'].index(prop)
    return dict(sorted(d.items(), key = lambda item: float(item[0][prop_idx])))

def prop(d, prop):
    prop_idx = ['app', 'only_used', 'num_lut', 'num_routing', 'num_bits', 'ratio'].index(prop)
    return np.array([key[prop_idx] for key, val in d.items()])

def vals(dict):
    return np.array(list(dict.values()))

def messy_edits(dict):
    app_idx = ['app', 'only_used', 'num_lut', 'num_routing', 'num_bits', 'ratio'].index('app')
    num_bits_idx = ['app', 'only_used', 'num_lut', 'num_routing', 'num_bits', 'ratio'].index('num_bits')
    out = {}

    for key, value in dict.items():
        if key[app_idx] in ['riscv_efpga', 'c432'] or key[num_bits_idx] == '896':
            pass
        elif key[app_idx] == 'c432_54':
            out[('c432',  *key[1:])] = value
        elif key[app_idx] == 'riscv_efpga_54':
            out[('riscv',  *key[1:])] = value
        elif key[app_idx] == 'xregs_comb_54':
            out[('pcode',  *key[1:])] = value
        else:
            out[key] = value

    return out


print(split_app('c432_54_False_256_256'))
with open('sat_results.txt') as f:
    lines = f.readlines()
    apps = [split_app(line.split()[0][4:]) for line in lines]
    apps = [tuple(app + [str(int(app[-1]) + int(app[-2])), str(float(app[-1])/(float(app[-2])+float(app[-1])))]) for app in apps]
    data = [line.split()[1] for line in lines]

unique_apps = list(set(apps))
num_timeouts = {}
seconds = {}
for app in unique_apps:
    num_timeouts[app] = 0
    seconds[app] = []
# num_timeouts = dict(zip(unique_apps, [0]*len(unique_apps)))
# seconds = dict(zip(unique_apps, [[]]*len(unique_apps)))
# print(seconds)
for i, val in enumerate(data):
    if val == 'Timeout':
        num_timeouts[apps[i]] += 1
    else:
        seconds[apps[i]].append(float(val))
# print(seconds)
seconds = {key:np.array(val) for key, val in seconds.items()}
seconds_wtimeout = {key:np.concatenate((val, np.ones(num_timeouts[key])*12*3600)) for key, val in seconds.items()}
seconds = sort(seconds, 'num_bits')
seconds_wtimeout = sort(seconds_wtimeout, 'num_bits')

averages = {key:np.average(val) for key, val in seconds.items()}
stdevs = {key:np.std(val)/2 for key, val in seconds.items()}
averages_wtimeout = {key:np.average(val) for key, val in seconds_wtimeout.items()}
stdevs_wtimeout = {key:np.std(val)/2 for key, val in seconds_wtimeout.items()}


# averages = sort(averages, 'num_bits')
# stdevs = sort(stdevs, 'num_bits')

c = 0.8
fig, ax = plt.subplots(figsize=(c*9, c*5))



def plot0():
    rv = filter_app(averages, 'app', 'riscv_efpga')
    rv = filter_app(rv, 'ratio', '0.5')
    rv_true = filter_app(rv, 'only_used', 'True')
    rv_false = filter_app(rv, 'only_used', 'False')
    rv_stdevs = filter_app(stdevs, 'app', 'riscv_efpga')
    rv_stdevs = filter_app(rv_stdevs, 'ratio', '0.5')
    rv_true_stdevs = filter_app(rv_stdevs, 'only_used', 'True')
    rv_false_stdevs = filter_app(rv_stdevs, 'only_used', 'False')

    riscv_true_plot, = ax.plot(prop(rv_true, 'num_bits').astype(np.float), vals(rv_true).astype(np.float), label = 'Used bits', marker = 'o', markersize = 8, color='r')
    riscv_false_plot, = ax.plot(prop(rv_false, 'num_bits').astype(np.float), vals(rv_false).astype(np.float), label = 'All bits', marker = 'o', markersize = 8, color='b')
    riscv_lim_plot, = ax.plot(prop(rv_false, 'num_bits').astype(np.float), [12*3600]*len(prop(rv_false, 'num_bits')), linestyle='dashed', color='b')

    plt.fill_between(prop(rv_true, 'num_bits').astype(np.float), vals(rv_true).astype(np.float)-vals(rv_true_stdevs).astype(np.float), vals(rv_true).astype(np.float)+vals(rv_true_stdevs).astype(np.float), facecolor='r', alpha=0.5)
    plt.fill_between(prop(rv_false, 'num_bits').astype(np.float), vals(rv_false).astype(np.float)-vals(rv_false_stdevs).astype(np.float), vals(rv_false).astype(np.float)+vals(rv_false_stdevs).astype(np.float), facecolor='b', alpha=0.5)

    plt.xlabel('Number of key bits')
    plt.ylabel('SAT execution time (seconds)')

    ax.legend(handles=[riscv_true_plot, riscv_false_plot], loc='upper left')
    ax.set_yscale("log")
    plt.show()


def plot1():
    rv = filter_app(seconds_wtimeout, 'app', 'riscv_efpga')
    rv = filter_app(rv, 'ratio', '0.5')
    rv_true = filter_app(rv, 'only_used', 'True')
    rv_false = filter_app(rv, 'only_used', 'False')

    x_true = []
    y_true = []
    x_false = []
    y_false = []

    USED_BITS = 0

    for expt, s in rv_true.items():
        for second in s:
            # x_true.append(100 - (int(expt[4]) + USED_BITS)/TOTAL_BITS*100)
            x_true.append(int(expt[4]) + USED_BITS)
            y_true.append(second)

    for expt, s in rv_false.items():
        for second in s:
            # x_false.append(100 - int(expt[4])/TOTAL_BITS*100)
            x_false.append(int(expt[4]))
            y_false.append(second)

    riscv_true_plot = ax.scatter(x_true, y_true, label = 'RISC-V eFPGA_opt', marker = '2', s = 75, alpha = 0.5)
    riscv_false_plot = ax.scatter(x_false, y_false, label = 'RISC-V eFPGA_generic', marker = '2', s = 75, alpha = 0.5)
    lim_plot, = ax.plot([0, 8119], [12*3600]*2, linestyle='dashed', color='darkslategray')
    plt.text(2000, 10*3600, '12 hours timeout', fontsize=10, color = 'darkslategray', fontweight='bold')
    true_num_bits, = ax.plot([4133, 4133], [0, 20*3600], linestyle='dashed', color='#1f77b4', linewidth = 3)
    plt.text(3100, 1500, '# key bits to\ndeobfuscate\neFPGA_opt\n(worst case)', fontsize=10.5, color = '#1f77b4', fontweight='bold', ha='center', bbox=dict(facecolor='none', edgecolor='#1f77b4'))
    false_num_bits, = ax.plot([8119, 8119], [0, 20*3600], linestyle='dashed', color='#ff7f0e', linewidth = 3)
    plt.text(7000, 1500, '# key bits to\ndeobfuscate\neFPGA_generic', fontsize=10.5, color = '#ff7f0e', fontweight='bold', ha='center', bbox=dict(facecolor='none', edgecolor='#ff7f0e'))


    # ax.plot([100 - (int(n)+USED_BITS)/TOTAL_BITS*100 for n in prop(rv_true, 'num_bits')], [min(val) for val in vals(rv_true)], color='#1f77b4')
    # ax.plot([100 - int(n)/TOTAL_BITS*100 for n in prop(rv_false, 'num_bits')], [min(val) for val in vals(rv_false)], color='#ff7f0e')

    ax.plot([int(n) + USED_BITS for n in prop(rv_true, 'num_bits')], [min(val) for val in vals(rv_true)], color='#1f77b4')
    ax.plot([int(n) for n in prop(rv_false, 'num_bits')], [min(val) for val in vals(rv_false)], color='#ff7f0e')

    plt.xlabel('Number of key bits')
    plt.ylabel('SAT execution time (s)')

    ax.grid(True, which='major', linewidth=0.3)
    ax.grid(True, which='minor', linewidth=0.15)
    ax.legend(handles=[riscv_true_plot, riscv_false_plot], loc='upper right', fontsize=12, bbox_to_anchor=(0.95, 0.95))
    ax.set_ylim([900, 14*3600])
    ax.set_xlim([0, 8300])
    ax.set_yscale("log")
    plt.tight_layout()
    plt.savefig('sat_plot.png')


def plot2():
    averages_edited = messy_edits(averages)
    stdevs_edited = messy_edits(stdevs)

    rv = filter_app(averages_edited, 'ratio', '0.5')
    rv_false = filter_app(rv, 'only_used', 'False')
    rv_stdev = filter_app(stdevs_edited, 'ratio', '0.5')
    rv_false_stdev = filter_app(rv_stdev, 'only_used', 'False')

    apps = list(set(prop(rv_false, 'app')))
    app_avgs = {app:filter_app(rv_false, 'app', app) for app in apps}
    app_stdevs = {app:filter_app(rv_false_stdev, 'app', app) for app in apps}
    plots = []

    for key, value in app_avgs.items():
        value_stdev = app_stdevs[key]
        plot, = ax.plot(100 - (prop(value, 'num_bits').astype(np.float)/8800*100), vals(value).astype(np.float), label = key, marker = 'o', markersize = 8)
        # plt.fill_between(prop(value, 'num_bits').astype(np.float), vals(value).astype(np.float)-vals(value_stdev).astype(np.float), vals(value).astype(np.float)+vals(value_stdev).astype(np.float), facecolor='r', alpha=0.5)
        plots.append(plot)

    plt.xlabel('Percentage of uncovered bits')
    plt.ylabel('SAT execution time (s)')

    ax.grid(True, which='major', linewidth=1)
    ax.grid(True, which='minor', linewidth=0.2)
    ax.legend(handles=plots, loc='lower right', fontsize=12)
    # ax.set_ylim([900, 14*3600])
    ax.set_xlim([100, 80])
    ax.set_yscale("log")
    plt.tight_layout()
    plt.show()


def plot3():
    seconds_edited = messy_edits(seconds_wtimeout)

    rv = filter_app(seconds_edited, 'ratio', '0.5')
    rv_false = filter_app(rv, 'only_used', 'False')

    apps = list(set(prop(rv_false, 'app')))
    app_x = {app:[] for app in apps}
    app_y = {app:[] for app in apps}
    app_min_x = {app:[] for app in apps}
    app_min_y = {app:[] for app in apps}
    plots = []

    TOTAL_BITS = 8850

    for expt, s in rv_false.items():

        for second in s:
            # app_x[expt[0]].append(100 - (int(expt[4]) + USED_BITS)/TOTAL_BITS*100)
            app_x[expt[0]].append(int(expt[4]))
            app_y[expt[0]].append(second)

        # app_min_x[expt[0]].append(100 - (int(expt[4]) + USED_BITS)/TOTAL_BITS*100)
        app_min_x[expt[0]].append(int(expt[4]))
        app_min_y[expt[0]].append(np.min(s))

    plot = ax.plot([0, 0], [0, 1], label = 'lala', alpha = 1)
    apps = ['riscv', 'pcode', 'c432', 'c880', 'c1355', 'c1908']
    for app in apps:
        minplot, = ax.plot(app_min_x[app], app_min_y[app])
        plot = ax.scatter(app_x[app], app_y[app], label = app, marker = '2', alpha = 0.5, color = minplot.get_color())
        plots.append(plot)


    riscv_lim_plot, = ax.plot([0, 10000], [12*3600]*2, linestyle='dashed', color='darkslategray')
    plt.text(3000, 10*3600, '12 hours timeout', fontsize=10, color = 'darkslategray', fontweight='bold')
    num_bits, = ax.plot([TOTAL_BITS, TOTAL_BITS], [0, 20*3600], linestyle='dashed', color='#ff7f0e', linewidth = 3)
    plt.text(7800, 2800, '# key bits to\ndeobfuscate\nthe design', fontsize=10.5, color = '#ff7f0e', fontweight='bold', ha='center', bbox=dict(facecolor='none', edgecolor='#ff7f0e'))

    plt.xlabel('Number of key bits')
    plt.ylabel('SAT execution time (s)')

    ax.grid(True, which='major', linewidth=1)
    ax.grid(True, which='minor', linewidth=0.2)
    ax.legend(handles=plots, loc='upper right', fontsize=11, bbox_to_anchor=(0.95, 0.95))
    ax.set_ylim([1500, 14*3600])
    ax.set_xlim([0, 9200])
    ax.set_yscale("log")
    plt.tight_layout()
    plt.show()


def plot4():
    # seconds_edited = messy_edits(seconds)

    rv = filter_app(seconds_wtimeout, 'ratio', '0.5')
    rv_false = filter_app(rv, 'only_used', 'False')

    apps = list(set(prop(rv_false, 'app')))

    app_x = {app:[] for app in apps}
    app_y = {app:[] for app in apps}
    app_min_x = {app:[] for app in apps}
    app_min_y = {app:[] for app in apps}
    plots = []

    for expt, s in rv_false.items():
        USED_BITS = 0
        if expt[0] != 'riscv_efpga':
            TOTAL_BITS = 1.1*8119
        else:
            TOTAL_BITS = 1.0*8800

        for second in s:
            app_x[expt[0]].append(100 - (int(expt[4]) + USED_BITS)/TOTAL_BITS*100)
            # app_x[expt[0]].append(int(expt[4]))
            app_y[expt[0]].append(second)

        app_min_x[expt[0]].append(100 - (int(expt[4]) + USED_BITS)/TOTAL_BITS*100)
        app_min_y[expt[0]].append(np.min(s))

    apps = ['riscv_efpga', 'xregs_comb_54']
    for app in apps:
        minplot, = ax.plot(app_min_x[app], app_min_y[app])
        plot = ax.scatter(app_x[app], app_y[app], label = app, marker = '2', alpha = 0.7, color = minplot.get_color())
        plots.append(plot)

    plt.xlabel('Number of key bits')
    plt.ylabel('SAT execution time (s)')

    ax.grid(True, which='major', linewidth=1)
    ax.grid(True, which='minor', linewidth=0.2)
    ax.legend(handles=plots, loc='upper left', fontsize=12)
    # ax.set_ylim([900, 12.5*3600])
    # ax.set_xlim([100, 0])
    ax.set_xlim([100, 80])
    ax.set_yscale("log")
    plt.show()


def plot5():
    seconds_edited = messy_edits(seconds_wtimeout)

    rv = filter_app(seconds_edited, 'ratio', '0.5')
    rv_false = filter_app(rv, 'only_used', 'False')

    apps = list(set(prop(rv_false, 'app')))
    app_x = {app:[] for app in apps}
    app_y = {app:[] for app in apps}
    app_min_x = {app:[] for app in apps}
    app_min_y = {app:[] for app in apps}
    plots = []

    TOTAL_BITS = 8850

    for expt, s in rv_false.items():

        for second in s:
            # app_x[expt[0]].append(100 - (int(expt[4]) + USED_BITS)/TOTAL_BITS*100)
            app_x[expt[0]].append(int(expt[4]))
            app_y[expt[0]].append(second)

        # app_min_x[expt[0]].append(100 - (int(expt[4]) + USED_BITS)/TOTAL_BITS*100)
        app_min_x[expt[0]].append(int(expt[4]))
        app_min_y[expt[0]].append(np.min(s))

    plot = ax.plot([0, 0], [0, 1], label = 'lala', alpha = 1)
    apps = ['riscv', 'pcode', 'c432', 'c880', 'c1355', 'c1908']
    for app in apps:
        minplot, = ax.plot(app_min_x[app], app_min_y[app])
        plot = ax.scatter(app_x[app], app_y[app], label = app, marker = '2', alpha = 0.5, color = minplot.get_color())
        plots.append(plot)


    # riscv_lim_plot, = ax.plot([0, 10000], [12*3600]*2, linestyle='dashed', color='darkslategray')
    # plt.text(3000, 10*3600, '12 hours timeout', fontsize=9, color = 'darkslategray', fontweight='bold')
    # num_bits, = ax.plot([TOTAL_BITS, TOTAL_BITS], [0, 20*3600], linestyle='dashed', color='darkslategray')
    # plt.text(8000, 3000, '# key bits to\ndeobfuscate\nthe design', fontsize=10.5, color = 'darkslategray', ha='center')
    #
    # plt.xlabel('Percentage of uncovered bits')
    # plt.ylabel('SAT execution time (s)')

    # ax.grid(True, which='major', linewidth=1)
    # ax.grid(True, which='minor', linewidth=0.2)
    # ax.legend(handles=plots, loc='upper right', fontsize=11)
    ax.set_ylim([1500, 14*3600])
    ax.set_xlim([120, 1300])
    ax.set_yscale("log")
    plt.tight_layout()
    plt.show()

# plot0()
plot1()
# plot2()
# plot3()
# plot4()
# plot5()

print('Done')
