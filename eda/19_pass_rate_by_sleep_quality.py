import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

# Calculate pass rate for each sleep quality category
pass_rate = (
    data.groupby("sleep_quality")["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
    .reset_index(name="pass_rate")
)

print("Pass Rate by Sleep Quality:")
print(pass_rate)

# Create visualization
fig = px.bar(
    pass_rate,
    x="sleep_quality",
    y="pass_rate",
    title="Pass Rate by Sleep Quality",
    labels={
        "sleep_quality": "Sleep Quality",
        "pass_rate": "Pass Rate (%)"
    },
    text_auto=".2f"
)

fig.show()