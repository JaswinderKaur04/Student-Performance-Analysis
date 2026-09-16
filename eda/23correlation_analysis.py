import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

numeric_columns = [
    "study_hours_per_day",
    "attendance_percentage",
    "previous_gpa",
    "time_management_score",
    "exam_score"
]

correlation = data[numeric_columns].corr()

print("Correlation Matrix:")
print(correlation.round(2))

fig = px.imshow(
    correlation,
    text_auto=".2f",
    title="Correlation Between Academic Factors and Exam Score",
    labels=dict(color="Correlation")
)

fig.show()