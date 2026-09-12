import pandas as pd

data = pd.read_csv("student_exam_performance.csv")

# Handliing categorical data
categorical_data = [
    "parent_education",
    "notes_quality",
    "sleep_quality",
    "device_availability"
]

for column in categorical_data:
    data[column] = data[column].fillna(data[column].mode()[0])
 
# mode()       → gives a Series
# mode()[0]    → gives the first mode value
# Find the most frequent value → take that value → use it to replace the missing values.
    
missing_values = data.isnull().sum()    
print(missing_values)


# Handling missing values for Numeric Data

numeric_data = [
    "previous_gpa",
    "attendance_percentage",
    "time_management_score"
]

for column in numeric_data:
    data[column] = data[column].fillna(data[column].median())
    
missing_values = data.isnull().sum()    
print(missing_values)    
    
    
data.to_csv("student_exam_performance_cleaned.csv", index=False)

print("\nCleaned dataset saved successfully.")    