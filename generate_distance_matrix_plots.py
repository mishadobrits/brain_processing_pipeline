from utils import config, config_str, read_npy, write_npy
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

random.seed(42)

distance_matrix = read_npy("distance_matrix.npy")
random.shuffle(distance_matrix)

# Create a 3x3 grid of subplots
n, m = config["generate_distance_matrix_plots"]["rows"], config["generate_distance_matrix_plots"]["cols"],
fig, axes = plt.subplots(n, m, figsize=(3.5 * n, int(2.5 * m)))
print(Counter([elem["group"] for elem in distance_matrix]))

# Plot each array as a heatmap in the grid
for i, ax in enumerate(axes.flat):
    if i < n * m and i < len(distance_matrix):
        #print(arrays[i][:3, :3]) #np.array([arrays[i][j, j] for j in range(len(arrays[i]))]))
        sns.heatmap(
            distance_matrix[i]["distance_matrix"],
            ax=ax,
            cmap='hot',  # Use 'hot' for intensity
            cbar=True,  # Disable individual colorbars
            xticklabels=False,
            yticklabels=False,
        )
        
        # Add label below the heatmap (adjust y-coordinate as needed)
        ax.text(
            0.5,  # Horizontal position (center)
            -0.05,  # Vertical position (below the heatmap)
            f"subject_id={distance_matrix[i]['subject_id']}\ngroup={distance_matrix[i]['group']}",  # Text based on index `i`
            ha='center',  # Horizontal alignment
            va='top',  # Vertical alignment
            transform=ax.transAxes,  # Use axes coordinates
            fontsize=12,  # Adjust font size
        )
    else:
        ax.axis('off')  # Turn off empty subplots

# Add GLOBAL TEXT BELOW THE ENTIRE HEATMAP GRID
fig.text(
    0.5,  # Horizontal position (center of figure)
    0.02,  # Vertical position (below subplots, adjust as needed)
    config_str,  # Your global text
    ha='center',  # Horizontal alignment
    va='bottom',  # Vertical alignment
    fontsize=14,
    fontweight='bold',
)

# Adjust layout to prevent overlap
plt.subplots_adjust(bottom=0.1, hspace=0.3, wspace=0.3)

# Save and close
plt.savefig('vars/images/distance_metrics.png', bbox_inches='tight')
plt.close()