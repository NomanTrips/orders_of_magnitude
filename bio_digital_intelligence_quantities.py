
import matplotlib.pyplot as plt
from math import log

# Quantities and their labels
ordered_quantities = {
    'bat *': 10e9,  # 10 billion
    'gpt3 params': 175e9,  # 175 billion
    '# gpt4 params **': 1.6e12,  # 1.6 trillion
    '# cells human body': 37.2e12,  # 37.2 trillion
    '# synapses human neocortex': 60e12  # 60 trillion
}

# Calculate radii (fourth root) and define exponential forms
radii = {label: value ** 0.25 for label, value in ordered_quantities.items()}
exp_forms = {
    'bat *': "10^9",
    'gpt3 params': "175^9",
    '# gpt4 params **': "1.6^12",
    '# cells human body': "37.2^12",
    '# synapses human neocortex': "60^12"
}

# Colors for the circles
colors = ['grey', 'green', 'purple', 'orange', 'blue']

# Note text
note_text = "* 'bat' = Total # of synapses in a bat brain.\n  ** 'gpt4 params' at rumored 200 billion X 8 = 1.6 trillion."

# Create a plot
fig, ax = plt.subplots(figsize=(14, 8), facecolor='white')

# Initialize the center of the first circle with padding
x_center = 100

# Plot each circle and labels
for label, radius in radii.items():
    circle = plt.Circle((x_center + radius, radius + 5), radius, alpha=0.6, edgecolor='none', facecolor=colors[list(radii.keys()).index(label)], linewidth=0)
    ax.add_patch(circle)
    label_text = f"{label}\n{exp_forms[label]}" if label == 'bat *' else f"{label}\n({exp_forms[label]})"
    plt.text(x_center + radius, radius + 5, label_text, ha='center', va='center', fontsize=9, color='black', linespacing=1.4)
    x_center += 2 * radius

# Add note at the bottom right with padding
plt.text(14000, -30, note_text, ha='right', va='top', fontsize=8, color='black')

# Set aspect, title, and remove axes
ax.set_aspect('equal')
ax.set_title('Biological and Digital Intelligence Quantities')
ax.set_xlim(0, x_center + 20)
ax.set_ylim(-25, max(radii.values()) * 2 + 10)
ax.axis('off')

plt.show()
