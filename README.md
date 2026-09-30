# Student Performance Analysis

## 📌 Project Overview

This project analyzes student academic performance using Python, SQL, and Power BI.

The objective is to identify the major factors associated with student performance, understand pass/fail patterns, and present actionable insights through an interactive dashboard.

The project follows a complete Data Analyst workflow:

- Data understanding
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Statistical analysis
- Business insights
- SQL analysis
- Power BI dashboard
- Final recommendations


---

## 🎯 Business Problem

Educational institutions need to understand the factors that influence student academic performance.

This analysis focuses on questions such as:

- What is the overall student pass rate?
- What is the average exam score?
- How does study time relate to performance?
- How does attendance relate to pass rates?
- How does previous academic performance relate to exam results?
- How do sleep quality and time management relate to performance?
- Which groups of students may require additional academic support?
- What insights can be used to support better academic planning?


---

## 📊 Dataset

The dataset contains:

- **100,000 students**
- **44 variables**

The dataset includes information related to:

- Student demographics
- Education background
- Previous academic performance
- Attendance
- Study habits
- Self-study
- Private tuition
- Online learning
- Study consistency
- Study environment
- Revision frequency
- Practice tests
- Sleep
- Screen time
- Physical activity
- Stress and motivation
- Internet and device availability
- Exam preparation
- Questions attempted and answered
- Time management
- Exam anxiety
- Final exam score
- Performance grade
- Pass/fail status
- Performance level


---

## 🛠️ Tools & Technologies

### Python

Used for:

- Data loading
- Data cleaning
- Missing-value handling
- Duplicate checking
- Data type analysis
- Exploratory Data Analysis
- Statistical analysis
- Business insights

Libraries:

- Pandas
- NumPy
- Plotly


### SQL / MySQL

Used for:

- Database creation
- Table creation
- Data verification
- Aggregation
- Filtering
- Grouping
- CASE statements
- Business analysis
- Student performance analysis


### Power BI

Used for:

- Interactive dashboard
- KPI visualization
- Performance analysis
- Study and attendance analysis
- Business insights
- Data storytelling


### Git & GitHub

Used for:

- Version control
- Project organization
- Tracking development progress
- Portfolio presentation


---

## 🔄 Project Workflow

Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning
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
Final Recommendations
🧹 Data Cleaning

The dataset was checked for:

Missing values
Duplicate records
Data types
Invalid or inconsistent values

Missing values were handled according to the type of variable.

For categorical variables, appropriate categorical replacement methods were used.

After preprocessing, the cleaned dataset contained no missing values in the analyzed fields.

📈 Exploratory Data Analysis

The analysis examined relationships between academic performance and factors such as:

Study hours
Attendance
Previous GPA
Time management
Sleep quality
Study habits
Exam preparation
Student learning behavior
📊 Key Findings
Overall Performance
Total students: 100,000
Overall pass rate: 77.39%
Average exam score: 61.95

Approximately 77% of students passed the exam based on the dataset's defined pass-status classification.

Study Hours

Observed pass rates increased across the study-hour groups:

Study Hours	Pass Rate
0–2	66.32%
2–4	78.51%
4–6	88.83%
6–8	94.77%
8–10	97.91%
10+	99.23%

The analysis shows a strong positive pattern between study hours and observed pass rates.

Attendance

Observed pass rates also increased across attendance groups:

Attendance	Pass Rate
0–60%	52.25%
60–70%	65.68%
70–80%	71.88%
80–90%	77.81%
90–100%	83.41%

Students with higher attendance had higher observed pass rates in this dataset.

Correlation Analysis

The analysis identified the following correlations with exam score:

Variable	Correlation
Previous GPA	0.45
Study Hours	0.36
Attendance	0.16
Time Management	0.10

Previous GPA and study hours showed stronger positive correlations with exam score than attendance and time management.

🗄️ SQL Analysis

The SQL analysis was performed using MySQL.

The SQL workflow includes:

Database creation
Table creation
Data import
Data verification
Student count analysis
Pass/fail analysis
Pass-rate calculations
Performance-grade analysis
Study-hour analysis
Attendance analysis
Previous-GPA analysis
Sleep-quality analysis
Device-availability analysis
Time-management analysis
Student-support identification
Overall business summary
Final data validation

SQL files are organized inside:

sql/
📊 Power BI Dashboard

The Power BI dashboard provides an interactive view of student performance.

The dashboard focuses on:

Total students
Pass/fail performance
Average exam score
Study hours
Attendance
Academic performance
Student performance groups
Business-level insights

The dashboard was designed to provide a professional and easy-to-understand view of the analysis.

💡 Business Insights

The analysis indicates several observable patterns in the dataset:

Students with higher study hours had higher observed pass rates.
Students with higher attendance had higher observed pass rates.
Previous GPA had the strongest positive correlation with exam score among the selected variables.
Study hours also showed a positive relationship with exam score.
Students with lower academic performance can be identified using combinations of exam score, attendance, study hours, previous GPA, and time-management measures.
SQL analysis provides a reproducible way to investigate these patterns directly from the database.
📌 Recommendations

Based on the observed patterns in the dataset:

Monitor students with consistently low attendance.
Identify students with low study hours for additional academic support.
Use previous academic performance to identify students who may benefit from early intervention.
Encourage effective study planning and time management.
Monitor students with consistently low exam scores.
Use dashboard insights to support academic monitoring and decision-making.
📁 Project Structure
Student-Performance-Analysis/
│
├── data/
│   └── student_exam_performance_cleaned.csv
│
├── preprocessing/
│
├── eda/
│
├── business_insights/
│
├── sql/
│   ├── 01_database_and_table.sql
│   ├── 02_data_verification.sql
│   ├── 03_basic_analysis.sql
│   ├── 04_business_analysis.sql
│   ├── 05_advanced_business_analysis.sql
│   └── 06_final_validation.sql
│
├── powerbi/
│
├── README.md
│
└── .gitignore
🔍 Important Note

The findings in this project describe patterns observed in the dataset.

Correlation and group-level comparisons do not by themselves establish causation.

For example, a higher pass rate among students with more study hours indicates an observed association in this dataset; it does not by itself prove that increasing study hours will cause a particular increase in exam performance.

🚀 Skills Demonstrated

This project demonstrates practical experience with:

Python
Pandas
NumPy
Plotly
Data Cleaning
Exploratory Data Analysis
Statistical Analysis
SQL
MySQL
Power BI
Data Visualization
Business Analysis
Data Storytelling
Git
GitHub
👩‍💻 Project Author

Jaswinder Kaur

Data Analyst / Data Analyst Trainer

Skills demonstrated through this project:

Python | Pandas | SQL | MySQL | Power BI | Data Analysis | Data Visualization | Git | GitHub
