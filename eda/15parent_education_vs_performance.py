import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

parent_education_by_grade = (
    data.groupby(["performance_grade", "parent_education"])
    .size()
    .reset_index(name="student_count")
)

print("Students by Performance Grade and Parent Education:")
print(parent_education_by_grade)

fig = px.bar(
    parent_education_by_grade,
    x="performance_grade",
    y="student_count",
    color="parent_education",
    barmode="group",
    title="Parent Education by Performance Grade",
    labels={
        "performance_grade": "Performance Grade",
        "student_count": "Number of Students",
        "parent_education": "Parent Education"
    }
)

fig.show()