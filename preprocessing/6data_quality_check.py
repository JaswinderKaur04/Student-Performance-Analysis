import pandas as pd
data = pd.read_csv("student_exam_performance_cleaned.csv")

# Dataset shape

print("DataSet Shape : ")
print(data.shape)

# -------------------------------
# Numeric Columns
# -------------------------------

numeric_columns = data.select_dtypes(include="number").columns

print("\nNumerical Data Summary")
# print(data[numeric_columns].describe().T)


# -------------------------------
# Categorical columns
# -------------------------------

categorical_columns = data.select_dtypes(include="object").columns

print("\nCategorical Columns:")
print(categorical_columns.tolist())

# -------------------------------
# Unique values
# -------------------------------

print("\nCategorical Value Counts:")

for column in categorical_columns:
    print(f"\n{column}:")
    print(data[column].value_counts())


# -------------------------------
# Duplicate student IDs
# -------------------------------

print("\nDuplicate Student IDs:")
print(data["student_id"].duplicated().sum())
