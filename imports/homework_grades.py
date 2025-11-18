homework_assignment_grades = {
    "homework_1": 85,
    "homework_2": 100,
    "homework_3": 81
}

def calculate_homework(homework_assignment_arg):
    sum_of_grades = 0
    for homework in homework_assignment_arg.values():
        sum_of_grades += homework
    final_grade = round(sum_of_grades/ len((homework_assignment_arg).keys()),2)
    return final_grade


test = calculate_homework(homework_assignment_grades)
print(test)
