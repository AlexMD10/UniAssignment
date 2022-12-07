import BasicCarClass
import numpy as np
import pandas as pd
from BasicCarClass import Car
file = pd.read_csv('CarRegistry.csv')
print('CarRegistry.csv')
print(file)

print('Menu: ')
print('A - Add car to registry')
print('D - Delete Car from registry')
print('H - Hire out')
print('R - Return car to Garage')
print('U - Update Car Registry')
print('')
print('X - Exit')
userchoice = input()


#while not userchoice.upper == 'Q':
#print (menu())
if userchoice.upper() == 'A':
    car = []
    CarObject = BasicCarClass.Car(16, 'reg_num', 'manufacturer', 'model_type', 'SHMP', 3, 2200, 3000, 250, 45, False)
    reg_value = (input("What is the car's Registration Number?"))
    manu_value = (input(('What is the Manufactuer of the car?')))
    model_type = (input('What is the Model of the car?'))
    sipp_code = (input('What is the SIPP code for the car?'))
    max_seating_capacity = (input('What is the maximum seating capacity of the car?'))
    car.append(reg_value)
    car.append(manu_value)
    car.append(model_type)
    car.append(sipp_code)
    car.append(max_seating_capacity)
    reg = car[0]
    manu = car[1]
    model = car[2]
    sipp = car[3]
    max_seat = car[4]
    CarObject.reg_num(reg)
    CarObject.manufacturer(manu)
    CarObject.model_type(model)
    CarObject.sipp_code(sipp)
    CarObject.max_seating_capacity(4)
    # The code below writes a new row to the CSV, basically just gets an ID and makes the 
    # car list above into the form x,b,as,c,asf,
    #run the code and you'll see, should make sense
    csv_length = len(file)
    #goes through list and squishes it all into a string
    car_entry = str(csv_length + 1) + ',' + ','.join(str(x) for x in car)
    print(car_entry)
    #then open the file and write the new line easy peasy
    with open('CarRegistry.csv','a') as fd:
        fd.write(car_entry)
elif userchoice.upper() == 'D':
    (print('Which car do you want to delete from the registry? Please enter registration number: '))
    choice = input()
    #Did a simple delete too for you, pandas is super useful library to do it for you
    #Read up on it if you can but basically this the line below says to look in the 
    #dataframe (pandas converts csv to Dataframe which is just code way of reading it)
    #looks in the file and returns all rows where the REG column value does not
    # equal your choice
    file = file[file.REG != choice]
    #then literally just save the file, the index=False tells it not to create another 
    #index column
    file.to_csv('CarRegistry.csv', index=False)
elif userchoice.upper() == 'H':
    print(input('Which car do you want to hire out?: '))
    #you can probably do some similar here with the delete
    #try searching https://www.geeksforgeeks.org/how-to-replace-values-in-column-based-on-condition-in-pandas/
    #gives you a clue basically file.loc is the method
    #so like file.loc(file["REG"] === your_car_reg, "ONHIRE") = True
    #you will probably have to do some checks before hand though either with your class
    #or here
elif userchoice.upper() == 'R':
    print(input('Which car do you want to return?: '))
elif userchoice.upper() == 'X':
    exit()
else:
    print('invalid choice option')