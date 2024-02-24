from os import system
from time import sleep
ads = [  
    "Buy this Python book for only 0.99$", 
    "Try this course of Python fro free!!!", 
    "Drink a lot of water (2L per day minimum)"
    ]
ads_duration = [
                2, 
                5,
                9

                ]
index = 0
while True:
    system("cls")
    print(f"Time for ads prensentation {ads_duration[index]} sec: {ads[index]}")
    sleep(ads_duration[index])
    index+=1
    if index >=len(ads):
        index = 0
   