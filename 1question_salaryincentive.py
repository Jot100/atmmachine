# first ask from employee about his/her salary

salary = float(input("user's salary $ :"))
# wy is indicates working years with company
wy = int(input("""User's years of working :"""))

# using if statement for gettinginformation weather user able to get Insentive or not.
if wy > 5: 
# multiply salary 0.05 beacuse we know 5% is = 5/100 
    new_Payable_amount = 0.05*salary

    #using f for define that it is a f-string 
    print(f"You are qualify for an incentive ${new_Payable_amount:.2f}")

else:
 # else is used for coming out from loop where if condition is not exist it will shows you that you are not eligible and get out from loop 
    wy < 5 
    print(f"You are not qualify for this ")



    