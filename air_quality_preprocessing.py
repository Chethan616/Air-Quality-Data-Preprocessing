import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('AirQualityUCI.csv') # Load the dataset

# matrix of features
data = data.loc[:, ~data.columns.str.contains('Unnamed')]

# Taking care fo Missing Values
missing_values = data.isnull().sum()
print("Missing Values per Column:\n", missing_values)

# Drop rows where Date or Time is missing
data = data.dropna(subset=['Date', 'Time'])

# Convert Date and Time to datetime format
data['DateTime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], errors='coerce')

# Drop rows where DateTime conversion failed
data = data.dropna(subset=['DateTime'])

# Select only numeric columns for imputation
numeric_cols = data.select_dtypes(include=[np.number]).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())

# Feature Scaling
scaler = StandardScaler()
scaled_columns = ["CO(GT)", "PT08.S1(CO)", "C6H6(GT)", "NOx(GT)", "NO2(GT)"]
data[scaled_columns] = scaler.fit_transform(data[scaled_columns])

# Time-Based Feature Engineering
data['Hour'] = data['DateTime'].dt.hour
data['DayOfWeek'] = data['DateTime'].dt.dayofweek
data['Month'] = data['DateTime'].dt.month

# Outlier Detection using IQR
Q1 = data[scaled_columns].quantile(0.25)
Q3 = data[scaled_columns].quantile(0.75)
IQR = Q3 - Q1

outlier_condition = (data[scaled_columns] < (Q1 - 1.5 * IQR)) | (data[scaled_columns] > (Q3 + 1.5 * IQR))
data[scaled_columns] = np.where(outlier_condition, np.nan, data[scaled_columns])
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())  # Replacing outliers with median

# Exploratory Data Analysis
print("Summary Statistics:\n", data.describe())

# Visualizations
plt.figure(figsize=(10, 5))
sns.boxplot(data=data[scaled_columns])
plt.xticks(rotation=90)
plt.title("Boxplot for Scaled Features")
plt.show()

plt.figure(figsize=(10, 5))
sns.heatmap(data[scaled_columns].corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()