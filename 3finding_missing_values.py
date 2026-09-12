# Which columns have missing values?

import pandas as pd

data = pd.read_csv("student_exam_performance.csv")
missing_values = data.isnull().sum()

print(missing_values)

# ---------------------------------------------------------------------------------

# How many missing values are there?

# parent_education              6526
# previous_gpa                  7793
# attendance_percentage         9863
# notes_quality                 8407
# sleep_quality                 6994
# device_availability           2965
# time_management_score         9613


# ---------------------------------------------------------------------------------

# What percentage of the column is missing?

missing_percentage = (data.isnull().sum() / len(data)) * 100

print(missing_percentage)

# parent_education              6.526
# previous_gpa                  7.793
# attendance_percentage         9.863
# notes_quality                 8.407
# sleep_quality                 6.994
# device_availability           2.965
# time_management_score         9.613


print("-------------------------final data with missing value-----------------------")

missing_data = pd.DataFrame({
    "Missing Values": data.isnull().sum(),
    "Missing Percentage": (data.isnull().sum() / len(data)) * 100
})

missing_data = missing_data[missing_data["Missing Values"] > 0]

print(missing_data)
