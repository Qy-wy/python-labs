class Student:
    students_quantity = 0

    def __init__(self, name, course, grades):
        self.name = name
        self.course = course
        self.grades = grades
        Student.students_quantity += 1

    def is_honors_student(self):
        total_sum = 0
        total_count = 0
        for subject_grades in self.grades.values():
            total_sum += sum(subject_grades)
            total_count += len(subject_grades)
        if total_count > 0:
            avg = total_sum / total_count
        else:
            avg = 0
        return avg > 8.5

    def avg_score_by_subject(self, subject):
        if subject in self.grades:
            scores = self.grades[subject]
            avg = sum(scores) / len(scores)
            return f"Average score for {subject} = {avg}"
        else:
            return f"The subject '{subject}' is not listed for this student."

student = Student("Anna", 2, {"programming": [9, 8, 10, 8, 10], "FE": [9, 8, 10, 9, 8]})
print(student.is_honors_student())
print(student.avg_score_by_subject('programming'))
