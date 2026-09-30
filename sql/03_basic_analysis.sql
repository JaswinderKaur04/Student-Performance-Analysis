-- ============================================
-- SQL ANALYSIS
-- ============================================

USE student_performance;


-- 1. Total number of students
SELECT COUNT(*) AS total_students
FROM student_exam_performance;


-- 2. Pass and Fail count
SELECT
    pass_status,
    COUNT(*) AS student_count
FROM student_exam_performance
GROUP BY pass_status;


-- 3. Overall Pass Rate
SELECT
    ROUND(
        SUM(CASE WHEN pass_status = 'Pass' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS pass_rate
FROM student_exam_performance;


-- 4. Average Exam Score
SELECT
    ROUND(AVG(exam_score), 2) AS average_exam_score
FROM student_exam_performance;


-- 5. Average Attendance
SELECT
    ROUND(AVG(attendance_percentage), 2) AS average_attendance
FROM student_exam_performance;


-- 6. Average Study Hours per Day
SELECT
    ROUND(AVG(study_hours_per_day), 2) AS average_study_hours
FROM student_exam_performance;


-- 7. Performance Grade Distribution
SELECT
    performance_grade,
    COUNT(*) AS student_count
FROM student_exam_performance
GROUP BY performance_grade
ORDER BY student_count DESC;


-- 8. Performance Level Distribution
SELECT
    performance_level,
    COUNT(*) AS student_count
FROM student_exam_performance
GROUP BY performance_level
ORDER BY student_count DESC;


-- 9. Pass Rate by Study Hours
SELECT
    CASE
        WHEN study_hours_per_day <= 2 THEN '0-2'
        WHEN study_hours_per_day <= 4 THEN '2-4'
        WHEN study_hours_per_day <= 6 THEN '4-6'
        WHEN study_hours_per_day <= 8 THEN '6-8'
        WHEN study_hours_per_day <= 10 THEN '8-10'
        ELSE '10+'
    END AS study_hours_group,

    COUNT(*) AS total_students,

    SUM(CASE WHEN pass_status = 'Pass' THEN 1 ELSE 0 END) AS passed_students,

    ROUND(
        SUM(CASE WHEN pass_status = 'Pass' THEN 1 ELSE 0 END)
        * 100.0 / COUNT(*),
        2
    ) AS pass_rate

FROM student_exam_performance

GROUP BY study_hours_group

ORDER BY
    CASE
        WHEN study_hours_group = '0-2' THEN 1
        WHEN study_hours_group = '2-4' THEN 2
        WHEN study_hours_group = '4-6' THEN 3
        WHEN study_hours_group = '6-8' THEN 4
        WHEN study_hours_group = '8-10' THEN 5
        ELSE 6
    END;