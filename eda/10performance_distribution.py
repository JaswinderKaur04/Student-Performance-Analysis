import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

grade_counts = data["performance_grade"].value_counts().reset_index()

grade_counts.columns = ["performance_grade", "student_count"]

print(grade_counts)

fig = px.bar(
    grade_counts,
    x="performance_grade",
    y="student_count",
    title="Student Distribution by Performance Grade",
    labels={
        "performance_grade": "Performance Grade",
        "student_count": "Number of Students"
    },
    text="student_count"
)

fig.show()