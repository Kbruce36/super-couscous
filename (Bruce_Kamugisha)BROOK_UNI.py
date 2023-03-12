# Define a function to calculate the final marks of a student
def calc_final_marks(test1, test2, coursework_marks, exam_marks):
    #Now we calculate the total coursework marks out of 40%
    coursework_total = max(test1, test2) + coursework_marks
    coursework_percentage = coursework_total * 0.4
    
    #Then we calculate the final exam marks out of 60%
    exam_percentage = exam_marks * 0.6
    
    #Then we calculate the final marks
    final_marks = coursework_percentage + exam_percentage
    
    return final_marks

#We define another function to prompt the user to enter the student details and marks
def get_student_details():
    # Get the name and academic year of the student
    name = str(input("Enter the name of the student: "))
    if int(name)*1 >= 1:
        print("non string")
    else:
        print()
    academic_year = input("Enter the academic year of the student: ")
    
    test1 = int(input("Enter the marks for test 1: "))
    test2 = int(input("Enter the marks for test 2: "))
    coursework_marks = int(input("Enter the marks for coursework: "))
    exam_marks = int(input("Enter the marks for exam: "))
    if exam_marks < 20 or exam_marks > 100:
        print("marks should be between 20 and 100")
    
    # Calculate the final marks
    final_marks = calc_final_marks(test1, test2, coursework_marks, exam_marks)
    pass_mark = 50
    if final_marks >= pass_mark:
        pass_fail = "Passed"
    else:
        pass_fail = "Failed"
    
    # Return the student details and final marks as a dictionary
    return {
        'name': name,
        'academic_year': academic_year,
        'final_marks': final_marks,
        'pass_fail': pass_fail
    }

# Define a function to save the student details and marks to a file
def save_details(details):
    # Open the file for writing
    with open('final_exam.txt', 'a') as f:      #"a" is used for appending data into the file and prevent overwriting the existing data.
        #we append or write the student details and final marks to the file that has been created
        f.write(f"Name: {details['name']}\n")
        f.write(f"Academic Year: {details['academic_year']}\n")
        f.write(f"Final Marks: {details['final_marks']}\n")
        f.write(f"passed or failed: {details['pass_fail']}\n\n")

# Get the number of students to enter marks for
num_students = int(input("Enter the number of students: "))

# Loop through each student and get their details and marks
for i in range(num_students):
    details = get_student_details()
    save_details(details)

print("Student details and marks saved to final_exam.txt")