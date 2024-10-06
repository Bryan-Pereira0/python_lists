#task1 + task2 in descending order and averaged 
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()
grades.reverse()
grades_count = len(grades)
grades_average = sum(grades) / grades_count
print(grades_average)
print(grades)