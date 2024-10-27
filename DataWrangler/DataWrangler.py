# Import necessary libraries
import pandas as pd
import numpy as np

# Load dataset (example: customer data)
# Replace 'customer_data.csv' with the path to your actual dataset file
df = pd.read_csv('customer_data.csv')

# Display initial information about the dataset
print("Initial Dataset Information:")
print(df.info())
print("\n")

# Step 1: Handle Missing Values
# Check for missing values
missing_values = df.isnull().sum()
print("Missing Values in Each Column:")
print(missing_values[missing_values > 0])

# Fill or drop missing values based on requirements
# Example: Fill missing values in 'age' with the mean
if 'age' in df.columns:
    df['age'].fillna(df['age'].mean(), inplace=True)

# Drop rows with missing values in essential columns
df.dropna(subset=['customer_id', 'email'], inplace=True)

# Step 2: Remove Duplicates
# Check for duplicate rows
duplicates = df.duplicated().sum()
print(f"\nNumber of Duplicate Rows: {duplicates}")

# Drop duplicate rows
df.drop_duplicates(inplace=True)

# Step 3: Data Transformation
# Example: Convert 'signup_date' to datetime format
if 'signup_date' in df.columns:
    df['signup_date'] = pd.to_datetime(df['signup_date'], errors='coerce')

# Extract 'year' and 'month' from 'signup_date' for easier analysis
df['signup_year'] = df['signup_date'].dt.year
df['signup_month'] = df['signup_date'].dt.month

# Example: Binning ages into categories
if 'age' in df.columns:
    bins = [0, 18, 25, 35, 45, 55, 65, 100]
    labels = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
    df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

# Step 4: Basic Insights
# Calculate average age by signup year
avg_age_per_year = df.groupby('signup_year')['age'].mean()
print("\nAverage Age by Signup Year:")
print(avg_age_per_year)

# Calculate customer count by age group
age_group_counts = df['age_group'].value_counts()
print("\nCustomer Count by Age Group:")
print(age_group_counts)

# Save the cleaned and transformed dataset
df.to_csv('cleaned_customer_data.csv', index=False)
print("\nData cleaning complete. Cleaned dataset saved as 'cleaned_customer_data.csv'.")
