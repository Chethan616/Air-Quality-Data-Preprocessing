Features & Steps Implemented

1. Handling Missing Values

Identifies missing values in the dataset.

Drops rows where the Date or Time column is missing.

Imputes missing numeric values using the median.

2. Feature Engineering

Converts Date and Time columns into a single DateTime column.

Extracts relevant time-based features: Hour, Day of the Week, and Month.

3. Feature Scaling

Uses StandardScaler to normalize numerical features like CO, NOx, and C6H6 concentrations.

4. Outlier Detection & Handling

Uses the Interquartile Range (IQR) method to detect outliers.

Replaces outliers with the median value of the respective column.

5. Exploratory Data Analysis (EDA)

Displays summary statistics for key features.

Generates visualizations:

Boxplots to observe feature distributions and outliers.

Heatmap to analyze feature correlations.

Technologies Used

Python

Pandas & NumPy for data manipulation

Matplotlib & Seaborn for data visualization

Scikit-learn for feature scaling

How to Run the Project

Clone the repository:

git clone https://github.com/Chethan616/air-quality-preprocessing.git

Navigate to the project folder:

cd air-quality-preprocessing

Install dependencies:

pip install pandas, numpy ,matplotlib , seaborn, scikit-learn

Run the script:

python preprocessing.py
