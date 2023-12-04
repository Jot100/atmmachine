#for making sales list we use veriable name sales_in_week
sales_in_week =[]
# for loop is stands for taking a value from user of each day's sales
for day in ("Monday","Tuesday","Wednesday","Friday","Saturday","Sunday"):
     # here we use float as we know that flaot contains decimal numbers as well as whole
    
    sales = float(input(f"Enter sales for day {day}: $"))
    sales_in_week.append(sales)

#add the total sales for the week
total_sales = sum(sales_in_week)

# taking output from user
print(f"Total sales for the week: $",total_sales)
