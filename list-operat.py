from os import system
guests_1 = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2 = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3 = [ "Tobey Weiss", "Kadie Barnes", "Diya Griffin" ]
all_guest =(guests_1 + guests_2 +guests_3)
#print(all_guest)
system("cls")
final_list = []
for i in range(len(all_guest)):
    if all_guest[i] in final_list:
        ### Print the same name
        print(' FOUND ', all_guest[i])
    else:
        final_list.append(all_guest[i])
### print(all_guest) for campare        
print('Original List:  ',all_guest)    
print('Unsorted List:  ',final_list)
#sorted alphabetic list
final_list = sorted(final_list)
print('Sorted List A-Z:', final_list)

    