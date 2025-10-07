marks_maths = int(input("Enter marks in Maths: "))
marks_sci = int(input("Enter marks in Science: "))
marks_eng = int(input("Enter marks in English: "))

total_marks = marks_maths + marks_sci + marks_eng
percentage_marks = (total_marks / 300) * 100

if percentage_marks >= 40 and marks_maths >= 33 and marks_sci >= 33 and marks_eng >= 33:
    print("Pass")
else:
    print("Fail")
    
    