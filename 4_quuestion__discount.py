#input taking input from user's purcased item quantitiy and pq is a purchased quantity


pq = int(input("Enter the quantity of items : "))

per_unit_cost = 100   # per_unit_cost is used to print what's the price of each item 

# total cost equals to multiplication of pq andper unit cost
total_cost = pq * per_unit_cost
print("The total cost is : ", total_cost)
# using if else statement for checking either conditions meets or not 

if total_cost > 1000:
    discount = total_cost * 0.10
    total_cost -= discount
    #f is float function to print floating numbers and here .f in {} will print one digit after .(dot)
    print(f"you have to pay after a 10% discount: {total_cost:.2f}")

else:
    total_cost < 1000
     #f is float function to print floating numbers and here .f in {} will print one digit after .(dot)
    print(f"sorry, you can't get discount ")
