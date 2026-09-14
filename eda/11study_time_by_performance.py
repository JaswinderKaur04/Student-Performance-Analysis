import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

study_by_grade = (
    data.groupby("performance_grade")["study_hours_per_day"]
    .mean()
    .reset_index()
)

study_by_grade = study_by_grade.sort_values("study_hours_per_day", ascending=False)

print("Average Study Hours by Performance Grade:")
print(study_by_grade)

fig = px.bar(
    study_by_grade,
    x="performance_grade",
    y="study_hours_per_day",
    title="Average Study Hours by Performance Grade",
    labels={
        "performance_grade": "Performance Grade",
        "study_hours_per_week": "Average Study Hours per day"
    },
    text_auto=".2f"
)

fig.show()