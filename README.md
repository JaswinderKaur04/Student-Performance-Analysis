# Student Performance Analysis

## 📌 Project Overview

This project analyzes student academic performance using **Python, SQL, and Power BI** to identify important patterns, relationships, and factors associated with student outcomes.

The project follows a complete end-to-end Data Analytics workflow:

**Data Understanding → Data Cleaning → Exploratory Data Analysis → Statistical Analysis → Business Insights → SQL Analysis → Power BI Dashboard → Final Documentation**

---

## 🎯 Business Problem

Educational institutions need to understand student performance and identify factors associated with academic outcomes.

This project aims to answer questions such as:

- What is the overall student pass rate?
- What is the average exam score?
- How does study time relate to student performance?
- How does attendance relate to pass rates?
- How does previous GPA relate to current exam performance?
- Which students may require additional academic support?
- What insights can help educational institutions monitor student performance?

---

## 📊 Dataset

The dataset contains **100,000 student records** and **44 variables** covering academic performance, study habits, attendance, lifestyle, learning resources, and examination-related information.

### Dataset Summary

- **Rows:** 100,000
- **Columns:** 44
- **Unique Students:** 100,000
- **Target Variables:** `exam_score`, `pass_status`, `performance_grade`, `performance_level`

### Main Variables

- Student ID
- Age
- Gender
- Education Level
- School Type
- Family Income
- Parent Education
- Urban/Rural
- Previous Exam Score
- Previous GPA
- Attendance Percentage
- Assignment Completion Rate
- Class Participation
- Study Hours Per Day
- Self Study Hours
- Private Tuition
- Online Learning Hours
- Study Consistency
- Study Environment
- Study Method
- Revision Frequency
- Practice Tests Completed
- Notes Quality
- Sleep Hours
- Sleep Quality
- Daily Screen Time
- Physical Activity Hours
- Break Frequency
- Stress Level
- Motivation Level
- Internet Access
- Device Availability
- Educational App Usage
- Online Course Hours
- Exam Difficulty
- Exam Preparation Days
- Questions Attempted
- Questions Correct
- Time Management Score
- Exam Anxiety Level
- Exam Score
- Performance Grade
- Pass Status
- Performance Level

---

## 🛠️ Tools & Technologies

### Python

- Pandas
- NumPy
- Plotly

### SQL

- MySQL

### Visualization

- Plotly
- Power BI

### Version Control

- Git
- GitHub

---

## 🔄 Project Workflow

Raw Dataset  
↓  
Data Understanding  
↓  
Data Cleaning & Preprocessing  
↓  
Exploratory Data Analysis  
↓  
Statistical Analysis  
↓  
Business Insights  
↓  
SQL Analysis  
↓  
Power BI Dashboard  
↓  
Final Documentation

---

# 1. Data Understanding

The dataset was first analyzed to understand:

- Dataset dimensions
- Column names
- Data types
- Missing values
- Duplicate records
- Numerical variables
- Categorical variables
- Target variables
- Overall data quality

---

# 2. Data Cleaning & Preprocessing

The following data-cleaning activities were performed:

- Checked missing values
- Checked duplicate students
- Analyzed data types
- Identified numerical and categorical variables
- Handled missing categorical values using the mode
- Validated the cleaned dataset
- Saved the cleaned dataset for further analysis

After cleaning, the analyzed dataset contained no missing values in the cleaned fields.

---

# 3. Exploratory Data Analysis

Exploratory Data Analysis was performed to identify patterns and relationships between student characteristics and academic performance.

The analysis included:

- Study hours
- Attendance
- Previous GPA
- Time management
- Sleep quality
- Device availability
- Parent education
- Performance grades
- Pass/fail status
- Performance levels

Interactive visualizations were created using **Plotly**.

---

# 4. Statistical Analysis

Correlation analysis was performed to examine relationships between selected numerical variables and exam score.

### Correlation with Exam Score

| Variable | Correlation |
|---|---:|
| Previous GPA | 0.45 |
| Study Hours | 0.36 |
| Attendance | 0.16 |
| Time Management | 0.10 |

These values describe associations observed in the dataset and do not establish causation.

---

# 5. Key Business Insights

## Overall Performance

- **Total Students:** 100,000
- **Overall Pass Rate:** 77.39%
- **Average Exam Score:** 61.95

---

## Study Hours vs Pass Rate

| Study Hours Per Day | Pass Rate |
|---|---:|
| 0–2 | 66.32% |
| 2–4 | 78.51% |
| 4–6 | 88.83% |
| 6–8 | 94.77% |
| 8–10 | 97.91% |
| 10+ | 99.23% |

The grouped results show that higher study-hour groups had higher pass rates in this dataset.

---

## Attendance vs Pass Rate

| Attendance | Pass Rate |
|---|---:|
| 0–60% | 52.25% |
| 60–70% | 65.68% |
| 70–80% | 71.88% |
| 80–90% | 77.81% |
| 90–100% | 83.41% |

Students in higher attendance groups had higher pass rates in this dataset.

---

## Previous GPA

Previous GPA had the strongest correlation with exam score among the selected variables:

**Correlation = 0.45**

This indicates a moderate positive association between previous GPA and current exam score.

---

## Study Hours

Study hours showed a positive association with exam score:

**Correlation = 0.36**

The grouped analysis also showed higher pass rates among students with higher study-hour levels.

---

## Attendance

Attendance showed a positive association with exam score:

**Correlation = 0.16**

The grouped pass-rate analysis also showed higher pass rates among students with higher attendance levels.

---

## Time Management

Time management showed a weaker positive association with exam score:

**Correlation = 0.10**

---

# 6. Students Requiring Academic Support

Additional analysis was performed to identify students who may require academic support based on combinations of indicators such as:

- Low exam score
- Low attendance
- Low study hours
- Failed status

These indicators can help educational institutions identify students who may need further review or academic support.

---

# 7. SQL Analysis

The cleaned dataset was imported into **MySQL** for structured analysis.

### Database

`student_performance`

### Table

`student_exam_performance`

SQL analysis included:

- Total student count
- Pass/fail counts
- Overall pass rate
- Average exam score
- Pass rate by attendance
- Pass rate by sleep quality
- Pass rate by device availability
- Pass rate by parent education
- Average exam score by previous GPA group
- Pass rate by time-management group
- Average exam score by attendance group
- Average exam score by sleep quality
- Students requiring academic support
- Students with low attendance and low scores
- Students with low study hours and failure
- Top-performing students
- Overall business summary
- Final validation checks

---

# 8. SQL Validation

Final SQL validation confirmed:

- **100,000 students**
- **44 columns**
- **100,000 unique student IDs**
- **0 missing student IDs**
- **0 missing exam scores**
- **0 missing pass status**
- **77.39% overall pass rate**
- **61.95 average exam score**

---

# 9. Power BI Dashboard

A professional Power BI dashboard was created to present the major findings in an interactive format.

The dashboard includes analysis of:

- Overall student performance
- Total students
- Pass rate
- Average exam score
- Study hours
- Attendance
- Previous GPA
- Performance distribution
- Academic support indicators
- Key business insights

The dashboard was designed for a professional portfolio and company-submission context.

---

# 10. Project Structure

Student-Performance-Analysis/

├── data/
│   ├── student_exam_performance.csv
│   └── student_exam_performance_cleaned.csv
│
├── preprocessing/
│   ├── 1_data_understanding.py
│   ├── 2_checking_duplicate_students.py
│   ├── 3_finding_missing_values.py
│   ├── 4_analysis_of_data_types.py
│   └── 5_handling_acc_to_type_of_data.py
│
├── eda/
│   └── exploratory_analysis.py
│
├── business_insights/
│   └── 26_business_insights.py
│
├── sql/
│   ├── 01student_performance_analysis.sql
│   ├── 02data_verification.sql
│   ├── 03student_performance_analysis.sql
│   ├── 04business_analysis1.sql
│   ├── 05business_analysis2.sql
│   └── 06final_validation.sql
│
├── powerbi/
│   └── Student Performance Dashboard
│
├── README.md
└── .gitignore

---

# 11. Key Findings Summary

| Metric | Result |
|---|---:|
| Total Students | 100,000 |
| Total Variables | 44 |
| Overall Pass Rate | 77.39% |
| Average Exam Score | 61.95 |
| Previous GPA Correlation | 0.45 |
| Study Hours Correlation | 0.36 |
| Attendance Correlation | 0.16 |
| Time Management Correlation | 0.10 |

---

# 12. Analytical Note

The analysis identifies relationships and patterns within the dataset.

Correlation values and grouped comparisons describe **associations**, not causal relationships.

For example, students in higher study-hour groups had higher pass rates, but this analysis alone does not prove that increasing study hours will necessarily cause a particular student's performance to improve.

Further controlled analysis or experimental research would be required to establish causal relationships.

---

# 13. Business Recommendations

Based on the observed patterns in the dataset, educational institutions can consider:

- Monitoring students with consistently low attendance.
- Identifying students with low study hours and failing outcomes.
- Providing additional academic support to students with low performance.
- Monitoring previous academic performance as an early indicator.
- Encouraging effective study planning and time management.
- Using dashboards for regular student-performance monitoring.
- Combining multiple indicators rather than relying on a single metric.

---

# 14. Skills Demonstrated

This project demonstrates practical skills in:

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis
- Statistical Analysis
- Business Analysis
- Python
- Pandas
- NumPy
- Plotly
- SQL
- MySQL
- Power BI
- Data Visualization
- Git
- GitHub
- Business Insight Generation
- Data Quality Validation

---

# 15. Project Outcome

This project demonstrates an end-to-end **Data Analyst workflow**, starting from a raw dataset and progressing through:

- Data Understanding
- Data Cleaning
- Exploratory Data Analysis
- Statistical Analysis
- Business Insights
- SQL Analysis
- Data Validation
- Power BI Visualization
- Final Documentation

The project demonstrates how raw student data can be transformed into structured analysis, business insights, SQL-based reporting, and an interactive Power BI dashboard.

---

# 👤 Author

**Jaswinder Kaur**

Data Analyst 

### Skills

- Python
- Pandas
- NumPy
- OpenCV
- SQL
- MySQL
- Power BI
- Plotly
- Data Analysis
- Data Visualization
- Git & GitHub

---

# ⭐ Project Highlights

- 100,000 student records analyzed
- 44 variables
- Complete data-cleaning workflow
- Exploratory Data Analysis
- Statistical analysis
- Business insights
- MySQL analysis
- SQL validation
- Interactive Power BI dashboard
