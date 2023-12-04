# below add list of answers for questions
ans_list = ["A", "C", "A", "A", "D", "B","C", "A", "C", "B", "A", "D","C", "A", "D", "C", "B", "B","D", "A"]
#initial score of candidate
Marks = 0
# use for loop to calculate numbers and taking user's input
for i in range(1,21):
    answer = input(f"Give answer for question {i} : ") #take inpput from user
    if answer.upper() == ans_list[i-1]: #answer.upper is used for taking answer in uppercase or conver it too
        Marks += 1 #score will be increase by + 1 if answer is correct
print("you got Marks :" , Marks,"/20") # used for printing result
if Marks > 15:
    print("you are eligible for getting Driver's license")
else:
    Marks   < 15
    print("You are not eligible for getting Driver's license ")
