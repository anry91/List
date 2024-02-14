days   = ["Mo", "Tu", "Wd", "Th", "Fr", "Sa", "Su"]
temps  = [10.0, 9.0,   8.0,  0.0, -5.0, -10.0, 0.0]
i = 0
while (i <len(temps)): 
      
    if temps[i] < 0:
        sign = "+"
    else:
        sign = " "

#for i in range(7):
 #   if temps[i]<=0:
 #       sign = "*"
 #   else:
 #       sign = " "
    print(sign, days[i], temps[i])
    i +=1