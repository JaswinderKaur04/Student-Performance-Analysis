import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

# Calculate pass rate for each device availability category
pass_rate = (
    data.groupby("device_availability")["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
    .reset_index(name="pass_rate")
)

print("Pass Rate by Device Availability:")
print(pass_rate)

# Create visualization
fig = px.bar(
    pass_rate,
    x="device_availability",
    y="pass_rate",
    title="Pass Rate by Device Availability",
    labels={
        "device_availability": "Device Availability",
        "pass_rate": "Pass Rate (%)"
    },
    text_auto=".2f"
)

fig.show()