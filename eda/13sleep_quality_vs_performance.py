import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

sleep_by_grade = (
    data.groupby(["performance_grade", "sleep_quality"])
    .size()
    .reset_index(name="student_count")
)

print("Students by Performance Grade and Sleep Quality:")
print(sleep_by_grade)

fig = px.bar(
    sleep_by_grade,
    x="performance_grade",
    y="student_count",
    color="sleep_quality",
    barmode="group",
    title="Sleep Quality by Performance Grade",
    labels={
        "performance_grade": "Performance Grade",
        "student_count": "Number of Students",
        "sleep_quality": "Sleep Quality"
    }
)

fig.show()