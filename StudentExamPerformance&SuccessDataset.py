import kagglehub

# Download latest version
path = kagglehub.dataset_download("mobeenfatimah/student-exam-performance-and-success-dataset")

print("Path to dataset files:", path)