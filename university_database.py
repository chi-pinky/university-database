# Description: This script creates a SQLite database for a university system.
import sqlite3

# Connect to database (or create one)
conn = sqlite3.connect('university.db')
cursor = conn.cursor()



# 1. Create all tables (only if they don't already exist)
try:
    cursor.executescript("""
    CREATE TABLE IF NOT EXISTS Students (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        date_of_birth TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Instructors (
        instructor_id INTEGER PRIMARY KEY, 
        name TEXT NOT NULL,
        department TEXT NOT NULL,
        phone_number TEXT UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT NOT NULL,
        credit_hours INTEGER NOT NULL CHECK (credit_hours > 0),
        department TEXT NOT NULL,
        instructor_id INTEGER NOT NULL,  -- Foreign key references Instructors table
        FOREIGN KEY (instructor_id) REFERENCES Instructors(instructor_id) ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS Enrollments (
        student_id INTEGER NOT NULL,
        course_id INTEGER NOT NULL,
        PRIMARY KEY (student_id, course_id),  -- Composite primary key to prevent duplicates
        FOREIGN KEY (student_id) REFERENCES Students(student_id) ON DELETE CASCADE,
        FOREIGN KEY (course_id) REFERENCES Courses(course_id) ON DELETE CASCADE
    );
    """)
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

# 2. Insert sample data
students = [
    ('Daniella Ishicheli', '1998-01-01', 'daniella.ishicheli@miva.edu.ng'),
    ('Chinwe Okoro', '1999-02-20', 'chinwe.okoro@miva.edu.ng'),
    ('Emeka Uche', '2001-03-05', 'emeka.uche@miva.edu.ng'),
    ('Amina Yusuf', '2002-04-10', 'amina.yusuf@miva.edu.ng'),
    ('Samuel Ojo', '2000-05-25', 'samuel.ojo@miva.edu.ng'),
    ('Zainab Bello', '1998-06-18', 'zainab.bello@miva.edu.ng'),
    ('Ifeanyi Obi', '2001-07-07', 'ifeanyi.obi@miva.edu.ng'),
    ('Mariam Abdullahi', '2000-08-22', 'mariam.abdullahi@miva.edu.ng'),
    ('Kunle Akinwale', '1999-09-11', 'kunle.akinwale@miva.edu.ng'),
    ('Fatima Suleiman', '1998-10-30', 'fatima.suleiman@miva.edu.ng'),
    ('Tunde Afolayan', '2001-11-12', 'tunde.afolayan@miva.edu.ng'),
    ('Ngozi Nwosu', '2000-12-01', 'ngozi.nwosu@miva.edu.ng'),
    ('Bashir Lawal', '2002-01-17', 'bashir.lawal@miva.edu.ng'),
    ('Chiamaka Eze', '1999-02-14', 'chiamaka.eze@miva.edu.ng'),
    ('Peter Amos', '2000-03-09', 'peter.amos@miva.edu.ng'),
    ('Yemi Balogun', '1998-04-26', 'yemi.balogun@miva.edu.ng'),
    ('Rashida Musa', '2001-05-13', 'rashida.musa@miva.edu.ng'),
    ('David Okon', '2002-06-04', 'david.okon@miva.edu.ng'),
    ('Sofia Etim', '2000-07-19', 'sofia.etim@miva.edu.ng'),
    ('Ismaila Garba', '1998-08-03', 'ismaila.garba@miva.edu.ng')
]

instructors = [
    ('Adekunle Adebayo', 'Computer Science', '+234 801 234 5678'),
    ('Bola Aluko', 'Electrical Engineering', '+234 802 345 6789'),
    ('Chidera Anozie', 'Mechanical Engineering', '+234 803 456 7890'),
    ('Yusuf Balogun', 'Civil Engineering', '+234 804 567 8901'),
    ('Nneka Chukwu', 'Mathematics', '+234 805 678 9012'),
    ('Femi Daramola', 'Business Administration', '+234 806 789 0123'),
    ('Oluwaseun Esan', 'Literature', '+234 807 890 1234'),
    ('Grace Fasanya', 'History', '+234 808 901 2345'),
    ('Gbenga Fashola', 'Chemistry', '+234 809 012 3456'),
    ('Funmi George', 'Accounting', '+234 810 123 4567'),
    ('Obinna Igbokwe', 'Computer Science', '+234 811 234 5678'),
    ('Aisha Kabir', 'Electrical Engineering', '+234 812 345 6789'),
    ('Opeyemi Lamidi', 'Mechanical Engineering', '+234 813 456 7890'),
    ('Fatima Mohammed', 'Civil Engineering', '+234 814 567 8901'),
    ('Tomiwa Odewale', 'Mathematics', '+234 815 678 9012'),
    ('Ngozi Okafor', 'Business Administration', '+234 816 789 0123'),
    ('Chinyere Onuoha', 'Literature', '+234 817 890 1234'),
    ('Kolade Popoola', 'History', '+234 818 901 2345'),
    ('Yetunde Quadri', 'Chemistry', '+234 819 012 3456'),
    ('Ahmed Sule', 'Accounting', '+234 820 123 4567')
]

courses = [
    ('Computer Programming', '3', 'Computer Science', 1),
    ('Data Structures and Algorithms', '3', 'Computer Science', 1),
    ('Database Management Systems', '3', 'Computer Science', 1),
    ('Introduction to Artificial Intelligence', '4', 'Computer Science', 1),
    ('Software Engineering', '4', 'Computer Science', 1),
    ('Introduction to Electrical Engineering', '3', 'Electrical Engineering', 2),
    ('Thermodynamics', '3', 'Mechanical Engineering', 3),
    ('Fluid Mechanics', '3', 'Mechanical Engineering', 3),
    ('Structural Analysis', '4', 'Civil Engineering', 4),
    ('Engineering Mathematics', '3', 'Mathematics', 5),
    ('Principles of Management', '3', 'Business Administration', 6),
    ('Introduction to Marketing', '3', 'Business Administration', 6),
    ('Financial Accounting', '3', 'Accounting', 10),
    ('Entrepreneurship Development', '4', 'Business Administration', 6),
    ('Business Communication', '3', 'Business Administration', 6),
    ('African Literature', '3', 'Literature', 7),
    ('Creative Writing', '3', 'Literature', 7),
    ('History of Nigeria', '4', 'History', 8),
    ('General Chemistry', '3', 'Chemistry', 9),
    ('Mathematics for Scientists', '3', 'Mathematics', 5)
]

import random

# Generate random enrollments
enrollments = []
student_ids = list(range(1, len(students) + 1))  # Assuming student IDs are sequential
course_ids = list(range(1, len(courses) + 1))    # Assuming course IDs are sequential

for _ in range(20):  # Generate 20 random enrollments
    student_id = random.choice(student_ids)
    course_id = random.choice(course_ids)
    enrollments.append((student_id, course_id))



# 3. Insert data with IGNORE to avoid duplicates
cursor.executemany("INSERT OR IGNORE INTO Students (name, date_of_birth, email) VALUES (?, ?, ?)", students)
cursor.executemany("INSERT OR IGNORE INTO Instructors (name, department, phone_number) VALUES (?, ?, ?)", instructors)
cursor.executemany("INSERT OR IGNORE INTO Courses (course_name, credit_hours, department, instructor_id) VALUES (?, ?, ?, ?)", courses)
cursor.executemany("INSERT OR IGNORE INTO Enrollments (student_id, course_id) VALUES (?, ?)", enrollments)



# 4. Commit and close
conn.commit()

# List all students and their enrolled courses
print("\n-- All students and their enrolled courses --")
query = """
SELECT 
    Students.name AS student_name, 
    Courses.course_name AS course_name
FROM 
    Enrollments
JOIN 
    Students ON Enrollments.student_id = Students.student_id
JOIN 
    Courses ON Enrollments.course_id = Courses.course_id;
"""
for row in cursor.execute(query):
    print(f"Student: {row[0]}, Course: {row[1]}")

# Find the instructor teaching "Database Management Systems"
print("\n-- Instructor for 'Database Management Systems' --")
query = """
SELECT 
    Instructors.name AS instructor_name
FROM 
    Courses
JOIN 
    Instructors ON Courses.instructor_id = Instructors.instructor_id
WHERE 
    Courses.course_name = 'Database Management Systems';
"""
cursor.execute(query)
result = cursor.fetchone()
if result:
    print(f"Instructor: {result[0]}")
else:
    print("No instructor found for 'Database Management Systems'")


# Count how many students are enrolled in each course
print("\n-- Student count per course --")
query = """
SELECT 
    Courses.course_name AS course_name, 
    COUNT(Enrollments.student_id) AS student_count
FROM 
    Courses
LEFT JOIN 
    Enrollments ON Courses.course_id = Enrollments.course_id
GROUP BY 
    Courses.course_name;
"""
for row in cursor.execute(query):
    print(f"Course: {row[0]}, Enrolled Students: {row[1]}")
    
conn.close()

