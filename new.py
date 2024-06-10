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

# Plot overlapping histograms for each grade
plt.figure(figsize=(10, 6))
grades = data['Grade'].unique()
for grade in grades:
    subset = data[data['Grade'] == grade]
    sns.histplot(subset['Marks'], kde=True, label=f'Grade {grade}', element='step')

plt.title('Overlapping Marks Distribution for Each Grade')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.legend()
plt.show()

# Regression analysis (Grade vs Marks)
X = data['Grade'].values.reshape(-1, 1)
y = data['Marks'].values
reg = LinearRegression().fit(X, y)
print(f'Regression Coefficient: {reg.coef_[0]}')
print(f'Intercept: {reg.intercept_}')
print(f'R^2 Score: {reg.score(X, y)}')

# Plot regression line
plt.figure(figsize=(10, 6))
plt.scatter(data['Grade'], data['Marks'], color='blue', label='Data Points')
plt.plot(data['Grade'], reg.predict(X), color='red', linewidth=2, label='Regression Line')
plt.title('Regression Analysis (Grade vs Marks)')
plt.xlabel('Grade')
plt.ylabel('Marks')
plt.legend()
plt.show()
