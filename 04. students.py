# first task from the lecture

students = []
course_to_search = None

while True:
    student_info = input()
    
    if ":" no in student_info:
        course_to_search = student_info
        break
    
    
    name, ID, course = student_info.split(":")
    students.append({'name': name, 'ID': ID, 'course': course})
    
    
for student in students:
    if course_to_search.startswith(studen['course'][0:3]):
        print(f"{student[name]} - {student['ID']}")    

# Second task from me

