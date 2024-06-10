import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# List of CSV files and corresponding years
csv_files = ['2018.csv', '2022.csv', '2024.csv']
years = [2018, 2022, 2024]

# Plot Grade vs Marks with OLS Regression for each year
for csv_file, year in zip(csv_files, years):
    # Read data
    data = pd.read_csv(csv_file)
    
    # Perform OLS regression
    X = sm.add_constant(data['Grade'])
    y = data['Marks']
    model = sm.OLS(y, X).fit()
    
    # Plot scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Grade', y='Marks', data=data, label=f'{year} Data')
    
    # Plot regression line
    sns.lineplot(x=data['Grade'], y=model.predict(X), label=f'{year} Regression Line')
    
    # Customize the plot
    plt.title(f'Grade vs Marks for {year}')
    plt.xlabel('Grade')
    plt.ylabel('Marks')
    plt.legend()
    plt.grid(True)
    
    # Save the plot as a high DPI image
    plt.savefig(f'grade_vs_marks_{year}.png', dpi=300)
    
    # Show the plot
    plt.show()
