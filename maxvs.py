import pandas as pd
import matplotlib.pyplot as plt

# List of CSV files and corresponding years
csv_files = ['2018.csv', '2022.csv', '2024.csv']
years = [2018, 2022, 2024]

# Dictionary to hold data for each year
data_dict = {}

# Read and store data for each year
for csv_file, year in zip(csv_files, years):
    data = pd.read_csv(csv_file)
    max_marks = data.groupby('Grade')['Marks'].max().reset_index()
    max_marks.columns = ['Grade', 'Max Marks']
    data_dict[year] = max_marks

# Plot Maximum Marks vs Grade for each year
plt.figure(figsize=(10, 6))

for year in years:
    plt.plot(data_dict[year]['Grade'], data_dict[year]['Max Marks'], marker='o', linestyle='-', label=f'{year}')

plt.title('Maximum Marks vs Grade for Each Year')
plt.xlabel('Grade')
plt.ylabel('Maximum Marks')
plt.legend()
plt.grid(True)

# Save the plot as a high DPI image
plt.savefig('max_marks_comparison.png', dpi=300)

# Show the plot
plt.show()
