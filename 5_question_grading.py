# ask for enter your grade
user_marks = float(input("Enter Student Marks : "))

# use if elif else conditional statement to give grades to Student according their marks

if user_marks < 25 : 
     print("you grade is : F")

 #user_number takes space between two marks to shows it vary between this two numbers 
elif 25 <= user_marks < 45: 
     print("You grade is : E")

elif 45 <= user_marks < 50:
     print("You grade is : D")

elif 50 <= user_marks <  60:
     print("Your Grade is : C")

elif  60 <= user_marks < 80:
     print("Your grade is : B")

else:
     user_marks > 80
     print ("Your grade is : A")


