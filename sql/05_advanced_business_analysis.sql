-- ============================================
-- 14. Average Exam Score by Previous GPA Group
-- ============================================

SELECT
    CASE
        WHEN previous_gpa < 5 THEN 'Below 5'
        WHEN previous_gpa < 6 THEN '5-6'
        WHEN previous_gpa < 7 THEN '6-7'
        WHEN previous_gpa < 8 THEN '7-8'
        WHEN previous_gpa < 9 THEN '8-9'
        ELSE '9+'
    END AS gpa_group,

    COUNT(*) AS total_students,

    ROUND(AVG(exam_score), 2) AS average_exam_score,

    ROUND(
        SUM(
            CASE
                WHEN pass_status = 'Pass' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS pass_rate

FROM student_exam_performance

GROUP BY gpa_group

ORDER BY
    CASE
        WHEN gpa_group = 'Below 5' THEN 1
        WHEN gpa_group = '5-6' THEN 2
        WHEN gpa_group = '6-7' THEN 3
        WHEN gpa_group = '7-8' THEN 4
        WHEN gpa_group = '8-9' THEN 5
        ELSE 6
    END;


-- ============================================
-- 15. Pass Rate by Time Management Group
-- ============================================

SELECT
    CASE
        WHEN time_management_score < 40 THEN 'Low'
        WHEN time_management_score < 70 THEN 'Medium'
        ELSE 'High'
    END AS time_management_group,

    COUNT(*) AS total_students,

    SUM(
        CASE
            WHEN pass_status = 'Pass' THEN 1
            ELSE 0
        END
    ) AS passed_students,

    ROUND(
        SUM(
            CASE
                WHEN pass_status = 'Pass' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS pass_rate,

    ROUND(AVG(exam_score), 2) AS average_exam_score

FROM student_exam_performance

GROUP BY time_management_group

ORDER BY
    CASE
        WHEN time_management_group = 'Low' THEN 1
        WHEN time_management_group = 'Medium' THEN 2
        ELSE 3
    END;


-- ============================================
-- 16. Average Exam Score by Attendance Group
-- ============================================

SELECT
    CASE
        WHEN attendance_percentage <= 60 THEN '0-60'
        WHEN attendance_percentage <= 70 THEN '60-70'
        WHEN attendance_percentage <= 80 THEN '70-80'
        WHEN attendance_percentage <= 90 THEN '80-90'
        ELSE '90-100'
    END AS attendance_group,

    COUNT(*) AS total_students,

    ROUND(AVG(exam_score), 2) AS average_exam_score

FROM student_exam_performance

GROUP BY attendance_group

ORDER BY
    CASE
        WHEN attendance_group = '0-60' THEN 1
        WHEN attendance_group = '60-70' THEN 2
        WHEN attendance_group = '70-80' THEN 3
        WHEN attendance_group = '80-90' THEN 4
        ELSE 5
    END;


-- ============================================
-- 17. Average Exam Score by Sleep Quality
-- ============================================

SELECT
    sleep_quality,

    COUNT(*) AS total_students,

    ROUND(AVG(exam_score), 2) AS average_exam_score

FROM student_exam_performance

GROUP BY sleep_quality

ORDER BY average_exam_score DESC;


-- ============================================
-- 18. Students Who May Need Academic Support
-- ============================================

SELECT
    student_id,
    exam_score,
    pass_status,
    performance_grade,
    study_hours_per_day,
    attendance_percentage,
    previous_gpa,
    time_management_score

FROM student_exam_performance

WHERE pass_status = 'Fail'

ORDER BY exam_score ASC

LIMIT 20;


-- ============================================
-- 19. Students with Low Attendance and Low Scores
-- ============================================

SELECT
    student_id,
    exam_score,
    attendance_percentage,
    study_hours_per_day,
    previous_gpa,
    time_management_score,
    performance_grade

FROM student_exam_performance

WHERE attendance_percentage < 60
  AND exam_score < 50

ORDER BY exam_score ASC;


-- ============================================
-- 20. Students with Low Study Hours and Failure
-- ============================================

SELECT
    student_id,
    exam_score,
    study_hours_per_day,
    attendance_percentage,
    previous_gpa,
    time_management_score,
    performance_grade

FROM student_exam_performance

WHERE study_hours_per_day < 4
  AND pass_status = 'Fail'

ORDER BY exam_score ASC;


-- ============================================
-- 21. Top 20 Performing Students
-- ============================================

SELECT
    student_id,
    exam_score,
    performance_grade,
    performance_level,
    study_hours_per_day,
    attendance_percentage,
    previous_gpa,
    time_management_score

FROM student_exam_performance

ORDER BY exam_score DESC

LIMIT 20;


-- ============================================
-- 22. Overall Business Summary
-- ============================================

SELECT

    COUNT(*) AS total_students,

    SUM(
        CASE
            WHEN pass_status = 'Pass' THEN 1
            ELSE 0
        END
    ) AS passed_students,

    SUM(
        CASE
            WHEN pass_status = 'Fail' THEN 1
            ELSE 0
        END
    ) AS failed_students,

    ROUND(
        SUM(
            CASE
                WHEN pass_status = 'Pass' THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS overall_pass_rate,

    ROUND(AVG(exam_score), 2) AS average_exam_score,

    ROUND(AVG(study_hours_per_day), 2) AS average_study_hours,

    ROUND(AVG(attendance_percentage), 2) AS average_attendance,

    ROUND(AVG(previous_gpa), 2) AS average_previous_gpa,

    ROUND(AVG(time_management_score), 2) AS average_time_management_score

FROM student_exam_performance;


-- ============================================
-- END OF BUSINESS ANALYSIS
-- ============================================