import csv

def main():
    # Get the number of students
    num_students = int(input("Enter the number of students: "))

    # Open the CSV file for writing
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])
        
        # Loop to get each student's details
        for _ in range(num_students):
            first_name = input("Enter the student's first name: ")
            last_name = input("Enter the student's last name: ")
            exam_1 = int(input("Enter grade for Exam 1: "))
            exam_2 = int(input("Enter grade for Exam 2: "))
            exam_3 = int(input("Enter grade for Exam 3: "))
            
            # Write the student's record
            writer.writerow([first_name, last_name, exam_1, exam_2, exam_3])

    print("Grades have been written to grades.csv.")

if __name__ == "__main__":
    main()
