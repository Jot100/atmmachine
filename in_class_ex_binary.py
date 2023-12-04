n1 = 25 #n1 is used for devidend number 

d = 2 # d is used for divisor 
r1 = int(n1%d)  #r1 is remainder
n2 = int(n1/d)  #n2 is used for new devidend number
r2 = int(n2%d)  #r2 is remainder
n3 = int(n2/d)  #n3 is another new devidend number after deviding n2/d
r3 = int(n3%d)  #r3 is remainder
n4 = int(n3/d)  #n4 is another new devidend number after deviding n3/d
r4 = int(n4%d)  #r4 is remainder
#used for print remainder r as a binary
print(r4)
print(r3)
print(r2)
print(r1)