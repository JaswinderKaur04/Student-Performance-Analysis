import pandas as pd

data = pd.read_csv("student_exam_performance.csv")

print("Attendance Percentage:")
print(data["attendance_percentage"].describe())

print("\nNotes Quality:")
print(data["notes_quality"].value_counts(dropna=False))

print("\nSleep Quality:")
print(data["sleep_quality"].value_counts(dropna=False))

print("\nDevice Availability:")
print(data["device_availability"].value_counts(dropna=False))

print("\nTime Management Score:")
print(data["time_management_score"].describe())