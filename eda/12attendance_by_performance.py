import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

attendance_by_grade = (
    data.groupby("performance_grade")["attendance_percentage"]
    .mean()
    .reset_index()
)

attendance_by_grade = attendance_by_grade.sort_values(
    "attendance_percentage",
    ascending=False
)

print("Average Attendance by Performance Grade:")
print(attendance_by_grade)

fig = px.bar(
    attendance_by_grade,
    x="performance_grade",
    y="attendance_percentage",
    title="Average Attendance by Performance Grade",
    labels={
        "performance_grade": "Performance Grade",
        "attendance_percentage": "Average Attendance (%)"
    },
    text_auto=".2f"
)

fig.show()