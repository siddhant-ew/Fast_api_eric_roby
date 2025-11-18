from imports.grade_avg_services import calculate_homework

homework_assignment_grades = {
    "homework_1": 85,
    "homework_2": 100,
    "homework_3": 81
}

final_grade = calculate_homework(homework_assignment_grades)
print(final_grade)