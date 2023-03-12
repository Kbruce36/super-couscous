# Define a function to validate if the input is a string
def is_valid_name(name):
    if not isinstance(name, str):
        print("Error: Name should be a string")
        return False
    return True

# Define a function to calculate the final marks of a student
def calculate_final_marks(test1, test2, coursework_marks, exam_marks):
    # Check if marks are within the range of 20-100
    if not 20 <= test1 <= 100 or not 20 <= test2 <= 100 or not 20 <= coursework_marks <= 100 or not 20 <= exam_marks <= 100:
        print("Error: Marks should be between 20-100")
        return None
    
    # Calculate the total coursework marks out of 40%
    coursework_total = max(test1, test2) + coursework_marks
    coursework_percentage = coursework_total * 0.4
    
    # Calculate the final exam marks out of 60%
    exam_percentage = exam_marks * 0.6
    
    # Calculate the final marks
    final_marks = coursework_percentage + exam_percentage
    
    return final_marks

# Define a function to get the student details and marks
def get_student_details():
    # Get the name and academic year of the student
    name = input("Enter the name of the student: ")
    if not is_valid_name(name):
        return None
    
    academic_year = input("Enter the academic year of the student: ")
    
    # Get the course unit and code from the user
    course_unit = input("Enter the course unit: ")
    course_code = input("Enter the course code: ")
    
    # Get the marks for test 1, test 2, coursework, and exam
    test1 = int(input("Enter the marks for test 1: "))
    test2 = int(input("Enter the marks for test 2: "))
    coursework_marks = int(input("Enter the marks for coursework: "))
    exam_marks = int(input("Enter the marks for exam: "))
    
    # Calculate the final marks
    final_marks = calculate_final_marks(test1, test2, coursework_marks, exam_marks)
    
    # Check if final marks are valid
    if final_marks is None:
        return None
    
    # Calculate pass/fail
    pass_mark = 50
    if final_marks >= pass_mark:
        pass_fail = "Passed"
    else:
        pass_fail = "Failed"
    
    # Return the student details and final marks as a dictionary
    return {
        'name': name,
        'academic_year': academic_year,
        'course_unit': course_unit,
        'course_code': course_code,
        'final_marks': final_marks,
        'pass_fail': pass_fail
    }

# Define a function to save the student details and marks to a file
def save_student_details(details):
    # Open the file for writing
    with open('final_exam.txt', 'a') as f:
        # Write the student details and final marks to the file
        f.write(f"Name: {details['name']}\n")
        f.write(f"Academic Year: {details['academic_year']}\n")
        f.write(f"Course Unit: {details['course_unit']}\n")
        f.write(f"Course Code: {details['course_code']}\n")
        f.write(f"Final Marks: {details['final_marks']}\n")
        f.write(f"Pass/Fail: {details['pass_fail']}\n\n")
    
    # Print the location of the file
    print("Student details and marks saved to:", f.name)