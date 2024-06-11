import pandas as pd

# List of CSV files and corresponding years
csv_files = ['2018.csv', '2022.csv', '2023.csv', '2024.csv']
years = [2018, 2022, 2023, 2024]

# Open a text file to save the statistical summaries
with open('statistical_summary_s.txt', 'w') as file:
    for csv_file, year in zip(csv_files, years):
        # Read data
        data = pd.read_csv(csv_file)
        
        # Calculate statistical measures
        max_marks = data['Marks'].max()
        min_marks = data['Marks'].min()
        mean_marks = data['Marks'].mean()
        mode_marks = data['Marks'].mode().iloc[0]  # mode() returns a Series, take the first mode
        median_marks = data['Marks'].median()
        std_marks = data['Marks'].std()
        var_marks = data['Marks'].var()
        percentiles = data['Marks'].quantile([0.25, 0.5, 0.75])
        
        # Write the summary to the text file
        file.write(f'Statistical Summary for {year}:\n')
        file.write(f'Max Marks: {max_marks}\n')
        file.write(f'Min Marks: {min_marks}\n')
        file.write(f'Mean Marks: {mean_marks}\n')
        file.write(f'Mode Marks: {mode_marks}\n')
        file.write(f'Median Marks: {median_marks}\n')
        file.write(f'Standard Deviation: {std_marks}\n')
        file.write(f'Variance: {var_marks}\n')
        file.write(f'25th Percentile: {percentiles[0.25]}\n')
        file.write(f'50th Percentile (Median): {percentiles[0.5]}\n')
        file.write(f'75th Percentile: {percentiles[0.75]}\n')
        file.write('\n' + '='*80 + '\n\n')

print("Statistical summaries have been saved to 'statistical_summary.txt'")
