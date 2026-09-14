import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

device_by_grade = (
    data.groupby(["performance_grade", "device_availability"])
    .size()
    .reset_index(name="student_count")
)

print("Students by Performance Grade and Device Availability:")
print(device_by_grade)

fig = px.bar(
    device_by_grade,
    x="performance_grade",
    y="student_count",
    color="device_availability",
    barmode="group",
    title="Device Availability by Performance Grade",
    labels={
        "performance_grade": "Performance Grade",
        "student_count": "Number of Students",
        "device_availability": "Device Availability"
    }
)

fig.show()