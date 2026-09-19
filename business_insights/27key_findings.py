import pandas as pd

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

print("===== KEY BUSINESS FINDINGS =====")

# 1. Overall performance
pass_rate = (data["pass_status"] == "Pass").mean() * 100

print("\n1. Overall Performance:")
print(f"The overall student pass rate is {pass_rate:.2f}%.")


# 2. Study hours
study_correlation = (
    data[["study_hours_per_day", "exam_score"]]
    .corr()
    .loc["study_hours_per_day", "exam_score"]
)

print("\n2. Study Hours:")
print(
    f"Study hours per day have a positive correlation "
    f"of {study_correlation:.2f} with exam score."
)


# 3. Attendance
attendance_correlation = (
    data[["attendance_percentage", "exam_score"]]
    .corr()
    .loc["attendance_percentage", "exam_score"]
)

print("\n3. Attendance:")
print(
    f"Attendance has a positive correlation "
    f"of {attendance_correlation:.2f} with exam score."
)


# 4. Previous GPA
gpa_correlation = (
    data[["previous_gpa", "exam_score"]]
    .corr()
    .loc["previous_gpa", "exam_score"]
)

print("\n4. Previous GPA:")
print(
    f"Previous GPA has the strongest correlation among the "
    f"selected academic factors, with a correlation of {gpa_correlation:.2f}."
)


# 5. Time management
time_correlation = (
    data[["time_management_score", "exam_score"]]
    .corr()
    .loc["time_management_score", "exam_score"]
)

print("\n5. Time Management:")
print(
    f"Time management has a very weak positive correlation "
    f"of {time_correlation:.2f} with exam score."
)


# 6. Study hours and pass rate
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

print("\n6. Study Hours and Pass Rate:")
print(study_pass_rate.round(2))


# 7. Attendance and pass rate
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

print("\n7. Attendance and Pass Rate:")
print(attendance_pass_rate.round(2))


# 8. Sleep quality
sleep_pass_rate = (
    data.groupby("sleep_quality")["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
)

print("\n8. Sleep Quality and Pass Rate:")
print(sleep_pass_rate.round(2))


# 9. Device availability
device_pass_rate = (
    data.groupby("device_availability")["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
)

print("\n9. Device Availability and Pass Rate:")
print(device_pass_rate.round(2))


# 10. Parent education
parent_pass_rate = (
    data.groupby("parent_education")["pass_status"]
    .apply(lambda x: (x == "Pass").mean() * 100)
)

print("\n10. Parent Education and Pass Rate:")
print(parent_pass_rate.round(2))


print("\n===== FINDINGS COMPLETE =====")