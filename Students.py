import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_csv("students.csv")

#print(f'Number of students: {len(students['StudentID'])}')
#print(students.describe())
#print(f'Highest attendance: {max(students['Attendance'])}%')
#print(f'Lowest attendance: {min(students['Attendance'])}%')
#print(f'Students below 80% attendance: {len(students[students['Attendance'] < 80])}')
#print(f'Students above or at 90% attendance: {len(students[students['Attendance'] >= 90])}')
#print(f'Students that got an A: {len(students[students['Grade'] == 'A'])}')
#print(f'Students that got an B: {len(students[students['Grade'] == 'B'])}')
#print(f'Students that got an C: {len(students[students['Grade'] == 'C'])}')
#print(f'Students that got an D: {len(students[students['Grade'] == 'D'])}')
#print(f'Students that got an E: {len(students[students['Grade'] == 'E'])}')
#print(f'Students that got an F: {len(students[students['Grade'] == 'F'])}')

#students.insert(5, "AtRisk", False)
#students["AtRisk"] = students['Attendance'] < 80
#print(students.head())

#print(students.sort_values(['Attendance'], ascending = [False]).head())

plt.hist(students['Attendance'])
plt.show()