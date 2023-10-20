'''Implement a function called sort_students that takes a list of student objects as input and sorts the list based on their CGPA (Cumulative Grade Point Average) in descending order. Each student object has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function with different input lists of students.'''


class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


# List of student objects
students = [
    Student("Rohit", "A123", 7.8),
    Student("Srikanth", "A124", 8.9),
    Student("Rohan", "A125", 9.1),
    Student("Priya", "A126", 9.9)
]

# Sort the students based on CGPA
sorted_students = sorted(students,
                         key=lambda student: student.cgpa,
                         reverse=True)

# Print the sorted list of students
print("Sorted List of Students:")
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {:.1f}".format(
      student.name, student.roll_number, student.cgpa))
