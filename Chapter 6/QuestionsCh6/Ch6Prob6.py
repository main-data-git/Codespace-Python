# 90-100 => Ex
# 80-90 => A
# 70-80 => B
# 60-70 => C
# 50-60 => D
# 40-50 => E
# <40 => F


stu_marks = int(input("Enter your marks: "))

if stu_marks >= 90 and stu_marks <= 100:
    grade = "Ex"
elif stu_marks >= 80 and stu_marks < 90:
    grade = "A"
elif stu_marks >= 70 and stu_marks < 80:
    grade = "B"
elif stu_marks >= 60 and stu_marks < 70:
    grade = "C"
elif stu_marks >= 50 and stu_marks < 60:
    grade = "D"
elif stu_marks >= 40 and stu_marks < 50:
    grade = "E"
elif stu_marks < 40 and stu_marks >= 0:
    grade = "F"
else:
    grade = "Invalid marks"
    
print("Your grade is:", grade)


