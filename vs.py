import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Read the CSV file
data = pd.read_csv('2018.csv')

# Calculate mean, median, mode, and std for each grade
statistics = data.groupby('Grade')['Marks'].agg(['mean', 'median', lambda x: x.mode().iloc[0], 'std']).reset_index()
statistics.columns = ['Grade', 'Mean', 'Median', 'Mode', 'Std']
print(statistics)

# Create a 2x2 grid plot
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Mean vs Grade
axes[0, 0].plot(statistics['Grade'], statistics['Mean'], marker='o', linestyle='-', color='b', label='Mean')
axes[0, 0].set_title('Mean vs Grade')
axes[0, 0].set_xlabel('Grade')
axes[0, 0].set_ylabel('Mean Marks')
axes[0, 0].legend()

# Mode vs Grade
axes[0, 1].plot(statistics['Grade'], statistics['Mode'], marker='o', linestyle='-', color='r', label='Mode')
axes[0, 1].set_title('Mode vs Grade')
axes[0, 1].set_xlabel('Grade')
axes[0, 1].set_ylabel('Mode Marks')
axes[0, 1].legend()

# Median vs Grade
axes[1, 0].plot(statistics['Grade'], statistics['Median'], marker='o', linestyle='-', color='g', label='Median')
axes[1, 0].set_title('Median vs Grade')
axes[1, 0].set_xlabel('Grade')
axes[1, 0].set_ylabel('Median Marks')
axes[1, 0].legend()

# Std Dev vs Grade
axes[1, 1].plot(statistics['Grade'], statistics['Std'], marker='o', linestyle='-', color='m', label='Standard Deviation')
axes[1, 1].set_title('Standard Deviation vs Grade')
axes[1, 1].set_xlabel('Grade')
axes[1, 1].set_ylabel('Std Deviation Marks')
axes[1, 1].legend()

# Adjust layout
plt.tight_layout()

# Save the plot as a high DPI image
plt.savefig('grade_statistics_plot.png', dpi=300)

# Show the plot
plt.show()
