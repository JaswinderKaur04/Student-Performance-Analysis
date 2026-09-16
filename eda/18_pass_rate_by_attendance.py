import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

# Create attendance groups
data["attendance_group"] = pd.cut(
    data["attendance_percentage"],
    bins=[0, 60, 70, 80, 90, 100],
    labels=["0-60", "60-70", "70-80", "80-90", "90-100"],
    include_lowest=True
)

# Calculate pass rate for each attendance group
pass_rate = (
    data.groupby("attendance_group", observed=True)["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
    .reset_index(name="pass_rate")
)

print("Pass Rate by Attendance:")
print(pass_rate)

# Create visualization
fig = px.bar(
    pass_rate,
    x="attendance_group",
    y="pass_rate",
    title="Pass Rate by Attendance Percentage",
    labels={
        "attendance_group": "Attendance Percentage",
        "pass_rate": "Pass Rate (%)"
    },
    text_auto=".2f"
)

fig.show()