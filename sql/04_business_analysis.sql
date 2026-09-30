-- ============================================
-- BUSINESS ANALYSIS
-- ============================================


-- 10. Pass Rate by Attendance Group

SELECT
    CASE
        WHEN attendance_percentage <= 60 THEN '0-60'
        WHEN attendance_percentage <= 70 THEN '60-70'
        WHEN attendance_percentage <= 80 THEN '70-80'
        WHEN attendance_percentage <= 90 THEN '80-90'
        ELSE '90-100'
    END AS attendance_group,

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
    ) AS pass_rate

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


-- 11. Pass Rate by Sleep Quality

SELECT
    sleep_quality,

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
    ) AS pass_rate

FROM student_exam_performance

GROUP BY sleep_quality

ORDER BY pass_rate DESC;


-- 12. Pass Rate by Device Availability

SELECT
    device_availability,

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
    ) AS pass_rate

FROM student_exam_performance

GROUP BY device_availability

ORDER BY pass_rate DESC;


-- 13. Pass Rate by Parent Education

SELECT
    parent_education,

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
    ) AS pass_rate

FROM student_exam_performance

GROUP BY parent_education

ORDER BY pass_rate DESC;