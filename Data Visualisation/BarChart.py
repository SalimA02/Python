import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



data = {
    'Job Role': ['Software Engineer', 'Manager', 'Software Engineer', 'Manager', 'Designer', 'Manager', 'Manager', 'Manager', 'Designer', 'Software Engineer', 'Software Engineer', 'Software Engineer', 'Manager', 'Designer', 'Manager'],
    'Experience': [3, 2, 6, 2, 6, 3, 5, 5, 2, 6, 4, 6, 3, 4, 3],
    'Salary': [53037, 41220, 51993, 42040, 43931, 49848, 59012, 50478, 46065, 54065, 40433, 52943, 50555, 47240, 40117]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Pivot the DataFrame to create a matrix for the heatmap
df_pivot = df.pivot_table(index='Job Role', columns='Experience', values='Salary')

# Create the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df_pivot, cmap='Blues_r', annot=True)
plt.title('Salary Heatmap')
plt.xlabel('Experience')
plt.ylabel('Job Role')
plt.show()