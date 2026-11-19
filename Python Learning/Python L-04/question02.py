#Q2. Count the classrooms needed for the subjects below (one classroom per subject).
#"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
classrooms_needed = len(subjects)
print("Number of classrooms needed:", classrooms_needed)

# I will use a set to store the subjects because sets automatically handle duplicates, ensuring that each subject is only counted once. This way, I can easily determine the number of unique subjects and thus the number of classrooms needed.