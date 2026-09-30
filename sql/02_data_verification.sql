USE student_performance;

-- Check total rows
SELECT COUNT(*) AS total_students
FROM student_exam_performance;

-- Check the imported columns and sample data
SELECT *
FROM student_exam_performance
LIMIT 5;

-- Check for duplicate student IDs
SELECT
    COUNT(*) AS total_students,
    COUNT(DISTINCT student_id) AS unique_students
FROM student_exam_performance;