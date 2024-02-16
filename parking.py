# hw calculate / print stats :
from os import system
system("cls")
p = ["Mercedes", None, "BMW", None, None, "Toyota", "BMW"]
free = 0
c_Mercedes = 0
c_BMW      = 0
c_Toyota   = 0
total      = len(p)
for i in range(len(p)):
    if p[i] == None:
        free+=1
    if p[i] == "Mercedes":
        c_Mercedes +=1
    if p[i] == "BMW":
        c_BMW +=1
    if p[i] == "Toyota":
        c_Toyota +=1
print("Parking (free/total):", free, "/", total, "place")
print("Mercedes ", '-', c_Mercedes,"\n" "BMW", '-', c_BMW, "\n" "Toyota", '-', c_Toyota,)      
