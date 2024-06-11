import pandas as pd
import statsmodels.api as sm

# List of CSV files and corresponding years
csv_files = ['2018j.csv', '2022j.csv', '2024j.csv']
years = [2018, 2022, 2024]

# Open a text file to save regression summaries
with open('Junior/ols_regression_summary.txt', 'w') as f:
    # Loop through each CSV file and corresponding year
    for csv_file, year in zip(csv_files, years):
        # Read data
        data = pd.read_csv(csv_file)
        
        # Perform OLS regression
        X = sm.add_constant(data['Grade'])
        y = data['Marks']
        model = sm.OLS(y, X).fit()
        
        # Write regression summary to the text file
        f.write(f'Regression Summary for {year}:\n')
        f.write(model.summary().as_text())
        f.write('\n\n')  # Add extra line for separation

print("Regression summaries saved successfully.")
