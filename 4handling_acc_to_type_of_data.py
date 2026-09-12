import pandas as pd

data = pd.read_csv("student_exam_performance.csv")

missing_data = pd.DataFrame({
    "Missing Values": data.isnull().sum(),
    "Missing Percentage": (data.isnull().sum() / len(data)) * 100
})

missing_data = missing_data[missing_data["Missing Values"] > 0]

print(missing_data)
print("-------------------------------------------------------------------------------------------")
# categorical data 
print(data["parent_education"].value_counts(dropna=False))
print("-------------------------------------------------------------------------------------------")
# numeric data
print(data["previous_gpa"].describe())
print("-------------------------------------------------------------------------------------------")