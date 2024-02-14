#hw 0:20:00
frieds = []
from os import system
system("cls")
while len(frieds) < 100:
    name = input("Add friend name: ")
    if name == "":
        break
    if name in frieds:                                #opreste programul daca se repeta numele
        print("Name ", name, "is already in de list")
        break
    frieds.append( name)
print("You have ", len(frieds), "friends")

for i in range(len(frieds)):
    print(i, ">>", frieds[i])