import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns

# Create a DataFrame with athlete data
np.random.seed(0)
athlete_data = pd.DataFrame({
    'Athlete': ['John', 'Mary', 'David', 'Emily', 'Michael', 'Sarah', 'William', 'Olivia', 'James', 'Ava', 'Robert', 'Isabella', 'Richard', 'Mia', 'Charles', 'Sophia', 'Thomas', 'Charlotte', 'Christopher', 'Amelia'],
    'Height (cm)': np.random.normal(175, 10, 20),
    'Weight (kg)': np.random.normal(70, 10, 20),
    'Age': np.random.randint(18, 40, 20)
})

# Add missing values
athlete_data.loc[1, 'Height (cm)'] = np.nan
athlete_data.loc[5, 'Weight (kg)'] = np.nan
athlete_data.loc[10, 'Age'] = np.nan
athlete_data.loc[15, 'Height (cm)'] = np.nan

# Add  outliers
athlete_data.loc[0, 'Height (cm)'] = 250
athlete_data.loc[10, 'Weight (kg)'] = 200

# Display the original DataFrame
print("Original DataFrame:")
print(athlete_data)

# Plot the original data
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(athlete_data['Height (cm)'], athlete_data['Weight (kg)'], athlete_data['Age'])
ax.set_title('Scatter Plot of Original Data')
ax.set_xlabel('Height (cm)')
ax.set_ylabel('Weight (kg)')
ax.set_zlabel('Age')
plt.show()

# Clean the data
# Replace missing values with mean
athlete_data[['Height (cm)', 'Weight (kg)', 'Age']] = athlete_data[['Height (cm)', 'Weight (kg)', 'Age']].fillna(athlete_data[['Height (cm)', 'Weight (kg)', 'Age']].mean())

# Remove outliers (values more than 3 standard deviations away from the mean)
athlete_data = athlete_data[(np.abs(athlete_data[['Height (cm)', 'Weight (kg)', 'Age']] - athlete_data[['Height (cm)', 'Weight (kg)', 'Age']].mean()) <= (3 * athlete_data[['Height (cm)', 'Weight (kg)', 'Age']].std())).all(axis=1)]

# Display the cleaned DataFrame
print("\nCleaned DataFrame:")
print(athlete_data)

# Plot the cleaned data
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(athlete_data['Height (cm)'], athlete_data['Weight (kg)'], athlete_data['Age'])
ax.set_title('Scatter Plot of Cleaned Data')
ax.set_xlabel('Height (cm)')
ax.set_ylabel('Weight (kg)')
ax.set_zlabel('Age')
plt.show()

# Create a pairplot to visualize the relationships between variables
sns.pairplot(athlete_data)
plt.show()

# Create a heatmap to visualize the correlations between variables
sns.heatmap(athlete_data[['Height (cm)', 'Weight (kg)', 'Age']].corr(), annot=True, cmap='coolwarm', square=True)
plt.show()