# What is actually happening in this student-performance data?

import pandas as pd

data = pd.read_csv("data\student_exam_performance_cleaned.csv")


# -------------------------------
# Dataset shape
# -------------------------------

print("Dataset Shape:")
print(data.shape)


# -------------------------------
# Numerical summary
# -------------------------------

print("\nNumerical Summary:")
print(data.describe())


# -------------------------------
# Target variables
# -------------------------------

print("\nPerformance Grade:")
print(data["performance_grade"].value_counts())

print("\nPerformance Level:")
print(data["performance_level"].value_counts())

print("\nPass Status:")
print(data["pass_status"].value_counts())


# -------------------------------
# Average exam score
# -------------------------------

print("\nAverage Exam Score:")
print(data["exam_score"].mean())

print("\nMedian Exam Score:")
print(data["exam_score"].median())