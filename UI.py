import BasicCarClass
import numpy as np
import pandas as pd
from BasicCarClass import Car
file = pd.read_csv('CarRegistry.dat')
print('CarRegistry.dat')
print(file)

#def menu(userchoice):
#f = open('CarRegistry.dat', 'r')
# writer = csv.DictWriter(f, fieldnames=['ID',
#         'REG',
#         'Manufacturer',
#         'Model',
#         'SIPP',
#         'Width',
#         'Length',
#         'Speed',
#         'MPG',
#         'OnHire'])
#CarArray = np.loadtxt
#print(f.read())
# data = []
# #f.readlines()
# for row in f:
#     fields = row.split(',')
#     print(fields)
#     data.append({
#         'ID':fields[0],
#         'REG':fields[1],
#         'Manufacturer':fields[2],
#         'Model':fields[3],
#         'SIPP':fields[4],
#         'Seats':fields[5],
#         'Width':fields[6],
#         'Length':fields[7],
#         'Speed':fields[8],
#         'MPG':fields[9],
#         'OnHire':fields[10]
#     })
#print(data)
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
    #print(car[2])
    reg = car[0]
    manu = car[1]
    model = car[2]
    sipp = car[3]
    max_seat = car[4]
    print(max_seat)
    CarObject.reg_num(reg)
    CarObject.manufacturer(manu)
    CarObject.model_type(model)
    CarObject.sipp_code(sipp)
    CarObject.max_seating_capacity(4)
    print('Your car is a:', CarObject)
elif userchoice.upper() == 'D':
    print(input('Which car do you want to delete from the registry?: '))
elif userchoice.upper() == 'H':
    print(input('Which car do you want to hire out?: '))
elif userchoice.upper() == 'R':
    print(input('Which car do you want to return?: '))
elif userchoice.upper() == 'X':
    exit()
else:
    print('invalid choice option')
  #   menu(userchoice)

# def menu():
#     print('A - Add car to registry')
#     print('D - Delete Car from registry')
#     print('H - Hire out')
#     print('R - Return car to Garage')
#     print('U - Update Car Registry')
#     print('X - Exit')
#
# menu()
# userchoice = str(input('Enter your choice'))
#while True:
# #    if userchoice.upper() == 'A':
#  #       print(input('What car do you want to add to the registry?:'))
#  #   elif userchoice.upper() == 'D':
#   #      print(input('Which car do you want to delete from the registry?: '))
#    # elif userchoice.upper() == 'H':
#     #    print(input('Which car do you want to hire out?: '))
#     #elif userchoice.upper() == 'R':
#         print(input('Which car do you want to return?: '))
#     elif userchoice.upper() == 'X':
#         exit()
#     else:
#         print('invalid choice option')

      #  menu()
       # userchoice = str(input('Enter your choice'))