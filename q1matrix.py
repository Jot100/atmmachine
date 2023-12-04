#generate matrix list row = 3 and column = 5
Matrix_list = [[0]*3 for _ in range(5)]
# create a loop for making 
for i in range(5):
    for j in range(3):
        Matrix_list[i][j] = int(input(f"Enter a whole number at row {i+1}, column {j+1}: "))
print(f"matrix $", Matrix_list)