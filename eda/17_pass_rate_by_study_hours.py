import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

# Create study-hour groups based on hours per day
# pd.cut() puts numerical values into ranges/bins.
data["study_hours_group"] = pd.cut(
    data["study_hours_per_day"],
    bins=[0, 2, 4, 6, 8, 10, float("inf")],  #float("inf") means infinity.
    # 0 to 2
    # 2 to 4
    # 4 to 6
    # 6 to 8
    # 8 to 10
    # 10 and above
    labels=["0-2", "2-4", "4-6", "6-8", "8-10", "10+"],
    include_lowest=True  #makes sure the lowest boundary is included in the first group.
)

# Calculate pass rate
pass_rate = (
    data.groupby("study_hours_group", observed=True)["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100) #Percentage of students in that group who passed
    .reset_index(name="pass_rate") #After groupby(), Pandas has the groups as an index.
                                   #reset_index() converts the result back into a normal DataFrame.
)

print("Pass Rate by Study Hours per Day:")
print(pass_rate)

# Visualization
fig = px.bar(
    pass_rate,
    x="study_hours_group",
    y="pass_rate",
    title="Pass Rate by Study Hours per Day",
    labels={
        "study_hours_group": "Study Hours per Day",
        "pass_rate": "Pass Rate (%)"
    },
    text_auto=".2f"
)

fig.show()