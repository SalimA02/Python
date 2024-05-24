import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a dictionary to store the data
data = {
    'Job Role': ['Software Engineer', 'Manager', 'Software Engineer', 'Manager', 'Designer', 'Manager', 'Manager', 'Manager', 'Designer', 'Software Engineer', 'Software Engineer', 'Software Engineer', 'Manager', 'Designer', 'Manager'],
    'Experience': [3, 2, 6, 2, 6, 3, 5, 5, 2, 6, 4, 6, 3, 4, 3],
    'Salary': [53037, 41220, 51993, 42040, 43931, 49848, 59012, 50478, 46065, 54065, 40433, 52943, 50555, 47240, 40117]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Pivot the DataFrame to create a matrix
pivot_df = df.pivot_table(values='Salary', index='Job Role', columns='Experience', aggfunc='mean')

# Create a heat map
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_df, annot=True, cmap='Blues', linewidths=0.5)
plt.title('Salary Heat Map')
plt.xlabel('Experience')
plt.ylabel('Job Role')
plt.show()