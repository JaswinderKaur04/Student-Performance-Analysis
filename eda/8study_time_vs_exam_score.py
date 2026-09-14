import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")


# Average exam score by study hours
study_analysis = (
    data.groupby("study_hours_per_day")["exam_score"]
    .mean()
    .reset_index()
)

print("Average Exam Score by Study Hours:")
print(study_analysis)


# Visualization
fig = px.line(
    study_analysis,
    x="study_hours_per_day",
    y="exam_score",
    markers=True,
    title="Study Hours vs Average Exam Score",
    labels={
        "study_hours_per_week": "Study Hours per day",
        "exam_score": "Average Exam Score"
    }
)

fig.show()