# take the value of 3 persons A,B,C from user 

A = int(input("Enter Age of A : "))
B = int(input("Enter Age of B: "))
C = int(input("Enter Age of C: "))
#using tuple to compare 3 to each other
oldest = max("A","B","c")
younger = min("A","B","c")

print(f"oldest person is {oldest} ")
print(f"younger person is {younger} ")