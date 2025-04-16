import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('student_depression_dataset.csv')  


print("First 5 rows of the dataset:")
print(df.head())


print("\nData types of each column:")
print(df.dtypes)

print("\nMissing values in each column:")
print(df.isnull().sum())



print("\nBasic statistics of numerical columns:")
print(df.describe())


if 'DateColumn' in df.columns and 'ValueColumn' in df.columns:
    df['DateColumn'] = pd.to_datetime(df['DateColumn'])  
    df.sort_values('DateColumn', inplace=True)  
    plt.figure(figsize=(10, 6))
    plt.plot(df['DateColumn'], df['ValueColumn'], marker='o', label='Value Over Time')
    plt.title('Trend Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid()
    plt.show()


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


if 'NumericalColumn' in df.columns:
    plt.figure(figsize=(10, 6))
    plt.hist(df['NumericalColumn'], bins=20, color='purple', edgecolor='black')
    plt.title('Distribution of Numerical Column')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(axis='y')
    plt.show()


if 'NumericalColumn1' in df.columns and 'NumericalColumn2' in df.columns:
    plt.figure(figsize=(10, 6))
    plt.scatter(df['NumericalColumn1'], df['NumericalColumn2'], color='green', alpha=0.7)
    plt.title('Relationship Between NumericalColumn1 and NumericalColumn2')
    plt.xlabel('NumericalColumn1')
    plt.ylabel('NumericalColumn2')
    plt.grid()
    plt.show()    git rm --cached "Data analysis project"
