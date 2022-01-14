#assignment 1

#question 1

#taking 3 numbers as input
print("first question")

number1=float(input("enter first number:-"))
number2=float(input("enter second number:-"))
number3=float(input("enter third number:-"))
average=(number1+number2+number3)/3 #making formula for average
print("average of the three numbers is :-",average)


#question2

print("second question")

standard_deduction=10000 
additional_dependant=3000
rate=0.02
gross_income=float(input("enter your gross income in dollars:"))
dependants=int(input("enter the number of dependants"))                   
taxable_income=gross_income-standard_deduction-(dependants*additional_dependant)
tax=taxable_income*rate
print("your total tax amount is:",tax)


#question3

print("third question")
print("student-[SID,NAME,GENDER,DEPT NAME,CGPA]")
student=[1,"shreya","F","ECE",9.3]
print("student=",student)


#question4

print("fourth question")
print("marks of five students")
marks_1=float(input("enter the marks of the first student:"))
marks_2=float(input("enter the marks of the second student:"))
marks_3=float(input("enter the marks of the third student:"))
marks_4=float(input("enter the marks of the fourth student:"))
marks_5=float(input("enter the marks of the fifth student:"))
marks=[marks_1,marks_2,marks_3,marks_4,marks_5]
print("marks before sorting:",marks)
marks.sort()
print("marks after sorting:",marks)


#question5

#a part
print("fifth question A part")
color_list=["red","green","white","black","pink","yellow"]
color_list.pop(3)
print(color_list)

#b part
print("fifth qyestion b part")
color_list=["red","green","white","black","pink","yellow"]
color_list[3:5]=["purple"]
print(color_list)








