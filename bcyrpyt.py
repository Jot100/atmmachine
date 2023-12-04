import bcrypt #importing libraries
input_password = b"pythonclassnavjotsingh!" #inputting the text and b implies bytecode 
hashed_password = bcrypt.hashpw(input_password, bcrypt.gensalt())
print(hashed_password)