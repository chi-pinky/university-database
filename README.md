# University Database Management System

This project is a Python script that creates and manages a SQLite database for a university system. It includes tables for students, instructors, courses, and enrollments, and provides functionality to insert sample data and query the database.

## Features

1. **Database Schema**:
   - `Students`: Stores student details such as name, date of birth, and email.
   - `Instructors`: Stores instructor details such as name, department, and phone number.
   - `Courses`: Stores course details such as course name, credit hours, department, and instructor.
   - `Enrollments`: Tracks which students are enrolled in which courses.

2. **Sample Data**:
   - Predefined lists of students, instructors, and courses are inserted into the database.
   - Random enrollments are generated to simulate student-course relationships.

3. **Queries**:
   - List all students and their enrolled courses.
   - Find the instructor teaching a specific course (e.g., "Database Management Systems").
   - Count the number of students enrolled in each course.

## Prerequisites

- Python 3.x
- SQLite (comes pre-installed with Python)

## How to Run

1. Clone or download this repository.
2. Navigate to the directory containing the script.
3. Run the script using Python:
   ```bash
   python university_database.py
   ```
4. The script will:
   - Create the database (`university.db`) if it doesn't already exist.
   - Populate the database with sample data.
   - Execute and display the results of predefined queries.

## Output

The script outputs the following:
1. A list of all students and their enrolled courses.
2. The instructor teaching "Database Management Systems".
3. The number of students enrolled in each course.

## Notes

- The script uses `INSERT OR IGNORE` to prevent duplicate entries when inserting data.
- Foreign key constraints ensure data integrity (e.g., cascading deletes for enrollments when a student or course is deleted).

## License

This project is for educational purposes and is provided as-is without any warranty.
