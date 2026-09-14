import pandas as pd
import plotly.express as px 

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

# Scatter plot
fig = px.scatter(
    data,
    x="attendance_percentage",
    y="previous_exam_score",
    title="Attendance Percentage vs Exam Score",
    labels={
        "attendance_percentage": "Attendance Percentage",
        "exam_score": "Exam Score"
    },
    trendline="ols"
)

fig.show()