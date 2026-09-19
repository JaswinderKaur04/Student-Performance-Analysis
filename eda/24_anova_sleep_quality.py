import pandas as pd
from scipy.stats import f_oneway

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

poor = data[data["sleep_quality"] == "Poor"]["exam_score"]
fair = data[data["sleep_quality"] == "Fair"]["exam_score"]
good = data[data["sleep_quality"] == "Good"]["exam_score"]
excellent = data[data["sleep_quality"] == "Excellent"]["exam_score"]

f_statistic, p_value = f_oneway(
    poor,
    fair,
    good,
    excellent
)

print("ANOVA Result")
print("F-statistic:", round(f_statistic, 2))
print("P-value:", p_value)

if p_value < 0.05:
    print("Result: Significant difference between at least one sleep-quality group.")
else:
    print("Result: No statistically significant difference detected.")