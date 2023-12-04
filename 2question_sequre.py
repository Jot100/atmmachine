# asking about lenght from user in centimeter (cm)
length = float(input("the value of lenth in cm is :"))

# asking about breadth from user in centimeter(cm)
breadth = float(input("the value of beadth in cm is :"))  
#using if statement for checking it is square or not
#if length is equals to breadth it will be a square
if length == breadth:
    
    print("It is Square")
#if length is not equals to breadth it will not a square

else:
 #when length is not equals to breadth print this is not a
    length /= breadth
    print("it is not a Square")
