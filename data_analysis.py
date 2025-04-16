import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('student_depression_dataset.csv')  

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(df.head())

# Display the data types of each column
print("\nData types of each column:")
print(df.dtypes)

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Fill missing values with the mean (if needed)
# Uncomment the line below if you want to handle missing values
# df = df.fillna(df.mean())

# Compute basic statistics for numerical columns
print("\nBasic statistics of numerical columns:")
print(df.describe())

# Visualization 1: Line Chart (Trends Over Time)
# Replace 'DateColumn' and 'ValueColumn' with actual column names
if 'DateColumn' in df.columns and 'ValueColumn' in df.columns:
    df['DateColumn'] = pd.to_datetime(df['DateColumn'])  # Ensure the date column is in datetime format
    df.sort_values('DateColumn', inplace=True)  # Sort by date
    plt.figure(figsize=(10, 6))
    plt.plot(df['DateColumn'], df['ValueColumn'], marker='o', label='Value Over Time')
    plt.title('Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.show()

# Visualization 2: Bar Chart (Comparison Across Categories)
# Replace 'CategoryColumn' and 'ValueColumn' with actual column names
if 'CategoryColumn' in df.columns and 'ValueColumn' in df.columns:
    category_means = df.groupby('CategoryColumn')['ValueColumn'].mean()
    plt.figure(figsize=(10, 6))
    category_means.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Average Value by Category')
    plt.xlabel('Category')
    plt.ylabel('Average Value')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()

# Visualization 3: Histogram (Distribution of a Numerical Column)
# Replace 'NumericalColumn' with the actual column name
if 'NumericalColumn' in df.columns:
    plt.figure(figsize=(10, 6))
    plt.hist(df['NumericalColumn'], bins=20, color='purple', edgecolor='black')
    plt.title('Distribution of Numerical Column')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.show()

# Visualization 4: Scatter Plot (Relationship Between Two Numerical Columns)
# Replace 'NumericalColumn1' and 'NumericalColumn2' with actual column names
if 'NumericalColumn1' in df.columns and 'NumericalColumn2' in df.columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(df['NumericalColumn1'], df['NumericalColumn2'], color='green', alpha=0.7)
    plt.title('Relationship Between NumericalColumn1 and NumericalColumn2')
    plt.xlabel('NumericalColumn1')
    plt.ylabel('NumericalColumn2')
    plt.grid()
    plt.show()    git rm --cached "Data analysis project"