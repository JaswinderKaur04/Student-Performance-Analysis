import pandas as pd

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

print("Number of columns:", len(data.columns))

for i, column in enumerate(data.columns, start=1):
    print(i, column, data[column].dtype)