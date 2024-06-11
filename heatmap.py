import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# List of CSV files and corresponding years
csv_files = ["2018.csv", "2022.csv", "2024.csv"]
years = [2018, 2022, 2024]

# Read and combine data from all CSV files
data_list = []
for csv_file, year in zip(csv_files, years):
    data = pd.read_csv(csv_file)
    data["Year"] = year
    data_list.append(data)

# Combine all data into a single DataFrame
combined_data = pd.concat(data_list)

# Calculate the correlation matrix
correlation_matrix = combined_data.corr()

# Plot the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)

# Customize the plot
plt.title("Correlation Heatmap of Student Marks")
plt.show()
