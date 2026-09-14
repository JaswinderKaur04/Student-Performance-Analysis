import pandas as pd
import plotly.express as px

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

pass_counts = data["pass_status"].value_counts().reset_index()

pass_counts.columns = ["pass_status", "student_count"]

pass_counts["percentage"] = (
    pass_counts["student_count"] / len(data) * 100
)

print("Pass Status:")
print(pass_counts)

fig = px.pie(
    pass_counts,
    names="pass_status",
    values="student_count",
    title="Student Pass vs Fail Distribution",
    hole=0.4
)

fig.show()