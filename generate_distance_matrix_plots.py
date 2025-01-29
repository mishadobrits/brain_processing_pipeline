from utils import config, config_str, read_npy, write_npy
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter, defaultdict

random.seed(42)

distance_matrix = read_npy("distance_matrix.npy")
random.shuffle(distance_matrix)

group_to_data = defaultdict(list)
for elem in distance_matrix:
    group_to_data[elem["group"]].append(elem)

n, m = config["generate_distance_matrix_plots"]["rows"], config["generate_distance_matrix_plots"]["cols"]
fig, axes = plt.subplots(n, len(group_to_data) * m, figsize=(3.5 * len(group_to_data) * m, 2.5 * n))

for group_num, (group, records) in enumerate(group_to_data.items()):
    cur_data = group_to_data[group]
    for i, ax in enumerate(axes[:, m * group_num: m * (group_num + 1)].flat):
        if i >= n * m or i >= len(cur_data):
            break

        sns.heatmap(
            np.abs(cur_data[i]["distance_matrix"]),
            ax=ax,
            cmap='hot',
            cbar=True,
            xticklabels=False,
            yticklabels=False,
        )
        
        ax.set_xlabel(f"subject_id={cur_data[i]['subject_id']}\ngroup={cur_data[i]['group']}")

plt.figtext(0.5, 0.02, config_str, ha='center', va='bottom', weight="bold")

plt.subplots_adjust(bottom=0.1, hspace=0.3, wspace=0.3)

# Save and close
plt.savefig('vars/images/distance_metrics.png', bbox_inches='tight')
plt.close()