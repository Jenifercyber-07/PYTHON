import csv

students = [
    {"Name": "Jenifer", "Tamil": 80, "English": 70, "Maths": 90, "Physics": 85, "Chemistry": 88},
    {"Name": "Lakshmi", "Tamil": 75, "English": 65, "Maths": 70, "Physics": 72, "Chemistry": 68},
    {"Name": "Ragavi", "Tamil": 40, "English": 50, "Maths": 30, "Physics": 35, "Chemistry": 25},
    {"Name": "Subha", "Tamil": 59, "English": 89, "Maths": 97, "Physics": 79, "Chemistry": 67},
    {"Name": "Risitha", "Tamil": 59, "English": 89, "Maths": 97, "Physics": 79, "Chemistry": 67},

]

for stu in students:
    total = stu["Tamil"] + stu["English"] + stu["Maths"] + stu["Physics"] + stu["Chemistry"]
    stu["Average"] = total / 5

    if (stu["Tamil"]>=35 and stu["English"]>=35 and stu["Maths"]>=35 and 
        stu["Physics"]>=35 and stu["Chemistry"]>=35):
        stu["Result"] = "Pass"
    else:
        stu["Result"] = "Fail"

with open("students.csv", "w", newline="") as f:
    fieldnames = ["Name", "Tamil", "English", "Maths", "Physics", "Chemistry", "Average", "Result"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("Student data saved")

with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)