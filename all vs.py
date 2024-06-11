import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# List of CSV files and corresponding years
csv_files = ['2018j.csv','2022j.csv','2023j.csv', '2024j.csv']
years = [2018, 2022,2023, 2024]
# Dictionary to hold data for each year
data_dict = {}

# Read and store data for each year
for csv_file, year in zip(csv_files, years):
    data = pd.read_csv(csv_file)
    statistics = data.groupby('Grade')['Marks'].agg(['mean', 'median', lambda x: x.mode().iloc[0], 'std']).reset_index()
    statistics.columns = ['Grade', 'Mean', 'Median', 'Mode', 'Std']
    data_dict[year] = statistics

# Create a 2x2 grid plot for mean, mode, median, and std
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Plot Mean vs Grade for each year
for year in years:
    axes[0, 0].plot(data_dict[year]['Grade'], data_dict[year]['Mean'], marker='o', linestyle='-', label=f'{year}')
axes[0, 0].set_title('Mean vs Level')
axes[0, 0].set_xlabel('Level')
axes[0, 0].set_ylabel('Mean Marks')
axes[0, 0].legend()

# Plot Mode vs Grade for each year
for year in years:
    axes[0, 1].plot(data_dict[year]['Grade'], data_dict[year]['Mode'], marker='o', linestyle='-', label=f'{year}')
axes[0, 1].set_title('Mode vs Level')
axes[0, 1].set_xlabel('Level')
axes[0, 1].set_ylabel('Mode Marks')
axes[0, 1].legend()

# Plot Median vs Grade for each year
for year in years:
    axes[1, 0].plot(data_dict[year]['Grade'], data_dict[year]['Median'], marker='o', linestyle='-', label=f'{year}')
axes[1, 0].set_title('Median vs Level')
axes[1, 0].set_xlabel('Level')
axes[1, 0].set_ylabel('Median Marks')
axes[1, 0].legend()

# Plot Std Dev vs Grade for each year
for year in years:
    axes[1, 1].plot(data_dict[year]['Grade'], data_dict[year]['Std'], marker='o', linestyle='-', label=f'{year}')
axes[1, 1].set_title('Standard Deviation vs Level')
axes[1, 1].set_xlabel('Level')
axes[1, 1].set_ylabel('Std Deviation Marks')
axes[1, 1].legend()

# Adjust layout
plt.tight_layout()

# Save the plot as a high DPI image
plt.savefig('Junior/grade_statistics_comparison.png', dpi=300)

# Show the plot
plt.show()
