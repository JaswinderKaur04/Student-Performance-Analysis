import pandas as pd

data = pd.read_csv("student_exam_performance.csv")


# print(data)
print("\n\n","=============================================================")
# print(data.info())

# Are there duplicate student records?

print(data.duplicated().sum())


