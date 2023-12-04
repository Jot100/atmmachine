#section is identify as a single class
section = int(input("Enter your days of Attandce : "))
Total_classes = int(input("Enter total classes begin days : ")) #total_classes shows how many classes have been held or will be held

leave_type_medical = str(input("If you took medical leave Y/N : "))
# N is a veriable which use for calculating percenatge 
 
if leave_type_medical == "Y":
  
  print("Studnet is eligible for sittitng in exam")

else:
  leave_type_medical == "N"
  print("student is not eligible for sitting in exam ")