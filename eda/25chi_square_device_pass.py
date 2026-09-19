import pandas as pd
from scipy.stats import chi2_contingency

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

table = pd.crosstab(
    data["device_availability"],
    data["pass_status"]
)

print("Contingency Table:")
print(table)

chi2, p_value, degrees_of_freedom, expected = chi2_contingency(table)  #performs the Chi-Square test.

print("\nChi-Square Result:")
print("Chi-Square Statistic:", round(chi2, 2))
print("P-value:", p_value)
print("Degrees of Freedom:", degrees_of_freedom)

if p_value < 0.05:
    print("Result: There is a statistically significant association.")
else:
    print("Result: No statistically significant association detected.")