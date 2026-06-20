addanotherstd = "yes"
stdDetails = {}

while True:
    if addanotherstd.lower() != "yes":
        break
    else:
        student_name = input("Enter Student Name: ").strip()

        # Keep asking for marks until the ENTIRE line is valid
        while True:
            marks = input("Enter Marks: ").split(" ")
            try:
                for i in range(1, len(marks), 2):
                    int(marks[i])  # just testing conversion, not storing yet
                break  # only reached if every mark converted successfully
            except ValueError:
                print("Invalid marks entered. Please enter numbers for marks. Try again.")

        studentsMarks = {}
        for i in range(0, len(marks), 2):
            studentsMarks[marks[i]] = int(marks[i + 1])
        stdDetails[student_name] = studentsMarks

        addanotherstd = input("Add another student? (yes/no): ").strip()

for student, marks in stdDetails.items():
    total_marks = sum(marks.values())
    average_marks = total_marks / len(marks)
    if average_marks >= 90:
        grade = "A"
    elif average_marks >= 75:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    elif average_marks >= 50:
        grade = "D"
    else:
        grade = "F"

    print("=" * 30)
    print(f"Report Card for: {student}")
    print("=" * 30)
    for subject, score in marks.items():
        print(f"{subject:<10}: {score}")
    print("-" * 30)
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Grade: {grade}")