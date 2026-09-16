import pandas as pd

data = pd.read_csv("data/student_exam_performance_cleaned.csv")

total_students = len(data)

passed_students = (data["pass_status"] == "Pass").sum()
failed_students = (data["pass_status"] == "Fail").sum()

pass_rate = passed_students / total_students * 100
fail_rate = failed_students / total_students * 100

average_exam_score = data["exam_score"].mean()
median_exam_score = data["exam_score"].median()

average_study_hours = data["study_hours_per_day"].mean()
average_attendance = data["attendance_percentage"].mean()

kpis = pd.DataFrame({
    "KPI": [
        "Total Students",
        "Passed Students",
        "Failed Students",
        "Pass Rate (%)",
        "Fail Rate (%)",
        "Average Exam Score",
        "Median Exam Score",
        "Average Study Hours per Day",
        "Average Attendance (%)"
    ],
    "Value": [
        total_students,
        passed_students,
        failed_students,
        pass_rate,
        fail_rate,
        average_exam_score,
        median_exam_score,
        average_study_hours,
        average_attendance
    ]
})

kpis["Value"] = kpis["Value"].round(2)

print("KPI Summary:")
print(kpis)