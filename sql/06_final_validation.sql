-- ============================================
-- FINAL SQL VALIDATION
-- Student Performance Analysis Project
-- ============================================

USE student_performance;


-- ============================================
-- 1. Total Rows
-- ============================================

SELECT COUNT(*) AS total_students
FROM student_exam_performance;


-- ============================================
-- 2. Total Columns
-- ============================================

SELECT COUNT(*) AS total_columns
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'student_performance'
  AND TABLE_NAME = 'student_exam_performance';


-- ============================================
-- 3. Duplicate Student IDs
-- ============================================

SELECT
    COUNT(*) AS total_students,
    COUNT(DISTINCT student_id) AS unique_student_ids
FROM student_exam_performance;


-- ============================================
-- 4. Missing Student IDs
-- ============================================

SELECT COUNT(*) AS missing_student_ids
FROM student_exam_performance
WHERE student_id IS NULL
   OR TRIM(student_id) = '';


-- ============================================
-- 5. Missing Exam Scores
-- ============================================

SELECT COUNT(*) AS missing_exam_scores
FROM student_exam_performance
WHERE exam_score IS NULL;


-- ============================================
-- 6. Missing Pass Status
-- ============================================

SELECT COUNT(*) AS missing_pass_status
FROM student_exam_performance
WHERE pass_status IS NULL;


-- ============================================
-- 7. Exam Score Range
-- ============================================

SELECT
    MIN(exam_score) AS minimum_score,
    MAX(exam_score) AS maximum_score,
    ROUND(AVG(exam_score), 2) AS average_score
FROM student_exam_performance;


-- ============================================
-- 8. Pass/Fail Validation
-- ============================================

SELECT
    pass_status,
    COUNT(*) AS student_count
FROM student_exam_performance
GROUP BY pass_status;


-- ============================================
-- 9. Final Overall Summary
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
    ) AS pass_rate,

    ROUND(AVG(exam_score), 2) AS average_exam_score

FROM student_exam_performance;


-- ============================================
-- END OF FINAL VALIDATION
-- ============================================