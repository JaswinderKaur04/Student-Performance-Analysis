-- ============================================
-- STUDENT PERFORMANCE ANALYSIS
-- SQL PROJECT
-- ============================================

-- 1. Create database
CREATE DATABASE IF NOT EXISTS student_performance;

-- 2. Select database
USE student_performance;

-- ============================================
-- CREATE TABLE
-- ============================================

CREATE TABLE student_exam_performance (
    student_id VARCHAR(50) PRIMARY KEY,

    age INT,
    gender VARCHAR(20),
    socioeconomic_status VARCHAR(50),

    parental_education_level VARCHAR(100),
    parent_education VARCHAR(100),

    study_hours_per_day DECIMAL(5,2),
    attendance_percentage DECIMAL(5,2),

    previous_gpa DECIMAL(4,2),

    extracurricular_activities VARCHAR(100),
    tutoring VARCHAR(100),

    sleep_hours DECIMAL(4,2),
    sleep_quality VARCHAR(50),

    stress_level VARCHAR(50),
    mental_health_status VARCHAR(100),

    internet_access VARCHAR(50),
    device_availability VARCHAR(50),

    notes_quality VARCHAR(50),
    time_management_score DECIMAL(5,2),

    exam_score DECIMAL(5,2),
    pass_status VARCHAR(20),
    performance_grade VARCHAR(5),
    performance_level VARCHAR(50)
);