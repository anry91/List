from os import system
system("cls")
order_name  = ["Pizza", "Salad", "Soupe"]
order_price = [75.00, 45.00, 15.00]
order_q     = [2, 1, 2]

for i in range(len(order_name)):
    subtotal = order_price[i]*order_q[i]
    total = order_price[i-2]*order_q[i-2] + order_price[i-1]*order_q[i-1] + order_price[i]*order_q[i]
    
    print((i+1), order_name[i], order_price[i], order_q[i], subtotal )
    
    
print(f"You have to pay :{total} ")
    
