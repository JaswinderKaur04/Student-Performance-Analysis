import pandas as pd

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

print("===== BUSINESS INSIGHTS DATA =====")

# 1. Overall pass rate
pass_rate = (data["pass_status"] == "Pass").mean() * 100

print("\nOverall Pass Rate:")
print(round(pass_rate, 2), "%")


# 2. Average exam score
print("\nAverage Exam Score:")
print(round(data["exam_score"].mean(), 2))


# 3. Study hours and exam score
print("\nStudy Hours vs Exam Score:")
print(
    data[["study_hours_per_day", "exam_score"]]
    .corr()
    .loc["study_hours_per_day", "exam_score"]
    .round(2)
)


# 4. Attendance and exam score
print("\nAttendance vs Exam Score:")
print(
    data[["attendance_percentage", "exam_score"]]
    .corr()
    .loc["attendance_percentage", "exam_score"]
    .round(2)
)


# 5. Previous GPA and exam score
print("\nPrevious GPA vs Exam Score:")
print(
    data[["previous_gpa", "exam_score"]]
    .corr()
    .loc["previous_gpa", "exam_score"]
    .round(2)
)


# 6. Time management and exam score
print("\nTime Management vs Exam Score:")
print(
    data[["time_management_score", "exam_score"]]
    .corr()
    .loc["time_management_score", "exam_score"]
    .round(2)
)


# 7. Pass rate by study hours
data["study_hours_group"] = pd.cut(
    data["study_hours_per_day"],
    bins=[0, 2, 4, 6, 8, 10, float("inf")],
    labels=["0-2", "2-4", "4-6", "6-8", "8-10", "10+"],
    include_lowest=True
)

study_pass_rate = (
    data.groupby("study_hours_group", observed=True)["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
)

print("\nPass Rate by Study Hours:")
print(study_pass_rate.round(2))


# 8. Pass rate by attendance
data["attendance_group"] = pd.cut(
    data["attendance_percentage"],
    bins=[0, 60, 70, 80, 90, 100],
    labels=["0-60", "60-70", "70-80", "80-90", "90-100"],
    include_lowest=True
)

attendance_pass_rate = (
    data.groupby("attendance_group", observed=True)["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
)

print("\nPass Rate by Attendance:")
print(attendance_pass_rate.round(2))


# 9. Pass rate by sleep quality
sleep_pass_rate = (
    data.groupby("sleep_quality")["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
)

print("\nPass Rate by Sleep Quality:")
print(sleep_pass_rate.round(2))


# 10. Pass rate by device availability
device_pass_rate = (
    data.groupby("device_availability")["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
)

print("\nPass Rate by Device Availability:")
print(device_pass_rate.round(2))


# 11. Pass rate by parent education
parent_pass_rate = (
    data.groupby("parent_education")["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
)

print("\nPass Rate by Parent Education:")
print(parent_pass_rate.round(2))


# 12. Performance grade distribution
print("\nPerformance Grade Distribution:")
print(data["performance_grade"].value_counts())


print("\n===== ANALYSIS COMPLETE =====")



# 0.36	Moderate positive relationship
# Attendance ↔ exam score	0.16	Weak positive relationship
# Previous GPA ↔ exam score	0.45	Strongest correlation among these factors
# Time management ↔ exam score	0.10