#getting two different values from user A & B both would be differ 
# A and B class name use for taking differ values 
A = int(input("Enter your Value of A : "))
B = int(input("Enter another Value of B : "))
# using if else conditional statement for comparing the values and getting correct answer
if A > B:
    #if the value of A is higher than the value of B, it will print following statement as The value of A is greater than B
    print("The value of A is greater than B")
    # if above condition does not exist than this function will check else statement if that will be false than it will come out from loop.
else:
    A < B
    #if the value of A is lower than the value of B, it will print following statement as The value of A is less than B
    print("the value of A is less than value of B")