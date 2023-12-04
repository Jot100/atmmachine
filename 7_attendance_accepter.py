#section is identify as a single class
section = int(input("Enter your days of Attandce : "))
Total_classes = int(input("Enter total classes begin days : "))  #total_classes shows how many classes have been held or will be held

# N is a veriable which use for calculating percenatge 
N = section/Total_classes*100
print(N)
# conditional sentance is used for checking requirements may meet or not 
if section > N:
  print("percentage of student {}%")
  print("Studnet is eligible for sittitng in exam")
else:
   section < N
   print("percentage of student {}%")
   print("studnet is eligible for sitting in exam")

