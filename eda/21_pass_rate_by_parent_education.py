import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

# Calculate pass rate for each parent education category
pass_rate = (
    data.groupby("parent_education")["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
    .reset_index(name="pass_rate")
)

print("Pass Rate by Parent Education:")
print(pass_rate)

# Create visualization
fig = px.bar(
    pass_rate,
    x="parent_education",
    y="pass_rate",
    title="Pass Rate by Parent Education",
    labels={
        "parent_education": "Parent Education",
        "pass_rate": "Pass Rate (%)"
    },
    text_auto=".2f"
)

fig.show()