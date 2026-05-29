import csv
import os
from datetime import datetime

class StudentAttendanceSystem:

    def __init__(self):
        self.students = {}
        self.attendance = {}

    # -----------------------------
    # STUDENT DATABASE
    # -----------------------------
    def add_student(self):
        student_id = input("Enter Student ID: ")

        if student_id in self.students:
            print("Student already exists!")
            return

        name = input("Enter Student Name: ")
        course = input("Enter Course: ")

        self.students[student_id] = {
            "Name": name,
            "Course": course
        }

        print("Student Added Successfully!")

    def view_students(self):

        if not self.students:
            print("No students found.")
            return

        print("\nStudent Database")
        print("-" * 40)

        for sid, details in self.students.items():
            print(
                f"ID: {sid} | "
                f"Name: {details['Name']} | "
                f"Course: {details['Course']}"
            )

    # -----------------------------
    # SEARCH STUDENT
    # -----------------------------
    def search_student(self):

        keyword = input("Enter Student ID or Name: ").lower()

        found = False

        for sid, details in self.students.items():

            if keyword == sid.lower() or keyword in details["Name"].lower():

                print("\nStudent Found")
                print(f"ID: {sid}")
                print(f"Name: {details['Name']}")
                print(f"Course: {details['Course']}")
                found = True

        if not found:
            print("Student not found!")

    # -----------------------------
    # MARK ATTENDANCE
    # -----------------------------
    def mark_attendance(self):

        date = input("Enter Date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except:
            print("Invalid Date Format!")
            return

        self.attendance[date] = {}

        for sid in self.students:

            status = input(
                f"{self.students[sid]['Name']} (P/A): "
            ).upper()

            if status not in ['P', 'A']:
                status = 'A'

            self.attendance[date][sid] = status

        print("Attendance Recorded Successfully!")

    # -----------------------------
    # VIEW ATTENDANCE
    # -----------------------------
    def view_attendance(self):

        if not self.attendance:
            print("No attendance records available.")
            return

        for date, records in self.attendance.items():

            print(f"\nDate: {date}")

            for sid, status in records.items():

                print(
                    f"{sid} - "
                    f"{self.students[sid]['Name']} : "
                    f"{status}"
                )

    # -----------------------------
    # ATTENDANCE ANALYTICS
    # -----------------------------
    def attendance_analytics(self):

        if not self.attendance:
            print("No attendance data available.")
            return

        print("\nAttendance Analytics")
        print("-" * 40)

        for sid in self.students:

            total_days = 0
            present_days = 0

            for date in self.attendance:

                if sid in self.attendance[date]:
                    total_days += 1

                    if self.attendance[date][sid] == 'P':
                        present_days += 1

            percentage = (
                (present_days / total_days) * 100
                if total_days > 0 else 0
            )

            print(
                f"{self.students[sid]['Name']} "
                f"-> Present: {present_days}, "
                f"Total: {total_days}, "
                f"Attendance: {percentage:.2f}%"
            )

    # -----------------------------
    # DAILY SUMMARY
    # -----------------------------
    def daily_summary(self):

        if not self.attendance:
            print("No attendance records.")
            return

        for date, records in self.attendance.items():

            present = sum(
                1 for status in records.values()
                if status == 'P'
            )

            absent = sum(
                1 for status in records.values()
                if status == 'A'
            )

            print(f"\nDate: {date}")
            print(f"Present Students : {present}")
            print(f"Absent Students  : {absent}")

    # -----------------------------
    # CSV EXPORT
    # -----------------------------
    def export_csv(self):

        filename = "attendance_report.csv"

        with open(
                filename,
                "w",
                newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Date",
                "Student ID",
                "Student Name",
                "Course",
                "Attendance"
            ])

            for date, records in self.attendance.items():

                for sid, status in records.items():

                    writer.writerow([
                        date,
                        sid,
                        self.students[sid]["Name"],
                        self.students[sid]["Course"],
                        status
                    ])

        print(
            f"Attendance exported successfully to "
            f"{filename}"
        )

    # -----------------------------
    # MENU
    # -----------------------------
    def run(self):

        while True:

            print("\n")
            print("=" * 50)
            print("STUDENT ATTENDANCE SYSTEM")
            print("=" * 50)

            print("1. Add Student")
            print("2. View Students")
            print("3. Search Student")
            print("4. Mark Attendance")
            print("5. View Attendance")
            print("6. Attendance Analytics")
            print("7. Daily Attendance Summary")
            print("8. Export CSV")
            print("9. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.view_students()

            elif choice == "3":
                self.search_student()

            elif choice == "4":
                self.mark_attendance()

            elif choice == "5":
                self.view_attendance()

            elif choice == "6":
                self.attendance_analytics()

            elif choice == "7":
                self.daily_summary()

            elif choice == "8":
                self.export_csv()

            elif choice == "9":
                print("Exiting...")
                break

            else:
                print("Invalid Choice!")


# -----------------------------
# MAIN PROGRAM
# -----------------------------
system = StudentAttendanceSystem()
system.run()