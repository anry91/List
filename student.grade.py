from os import system
student = {
    'firstname': "Shara", 

    'lastname': "Doha", 
    'age': 21, 
    'grade_1': 7.0, 
    'grade_2': 9.00, 
    'grade_3': 5.00

}
system('cls')
#Print the dict
list_gr = []
avg = 0
### check if is float, print .2*simbols
for key in student.keys():
    if type(student[key]) != float:
        var = student[key]
        
    else:
        var = student[key]
        var = (f'{var:.2f}')
        

    print(f'{key:10} : {var} ')
#### function
def averageCalc():
    global avg
    avg =(student['grade_1']+ student['grade_2']+student['grade_3'])/3
    

averageCalc()
print(f'{avg:.2f}')
if avg > 5.00:
    print("Student passed exams")
else:
    print("Student did not pass the exams")