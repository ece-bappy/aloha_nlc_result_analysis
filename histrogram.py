import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

csv_files = ['2018j.csv','2022j.csv','2023j.csv', '2024j.csv']
years = [2018, 2022,2023, 2024]

# Read and combine data from all CSV files
data_list = []
for csv_file, year in zip(csv_files, years):
    data = pd.read_csv(csv_file)
    data['Year'] = year
    data_list.append(data)

# Combine all data into a single DataFrame
combined_data = pd.concat(data_list)

# Get unique grades
grades = combined_data['Grade'].unique()

# Plot overlapping histograms and distribution curves for each grade
for grade in grades:
    plt.figure(figsize=(10, 6))
    
    for year in years:
        subset = combined_data[(combined_data['Grade'] == grade) & (combined_data['Year'] == year)]
        sns.histplot(subset['Marks'], kde=True, label=f'{year}', element='step', stat='density', common_norm=False)
    
    plt.title(f'Level {grade} Marks Distribution Comparison')
    plt.xlabel('Marks')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True)
    
    # Save the plot as a high DPI image
    plt.savefig(f'Junior/grade_{grade}_marks_distribution_comparison.png', dpi=300)
    
    # Show the plot
    plt.show()
