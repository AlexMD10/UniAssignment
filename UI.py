import BasicCarClass
import numpy as np
import pandas as pd
from BasicCarClass import Car
class UI:

    def __init__(self):
        self.file = pd.read_csv('CarRegistry.csv')
        self.carArray = []
        self.carObject = BasicCarClass.Car(16, 'reg_num', 'manufacturer', 'model_type', 'SHMP', 3, 2200, 3000, 250, 45, False)
        print(self.file)
        print('Menu: ')
        print('A - Add car to registry')
        print('D - Delete Car from registry')
        print('H - Hire out')
        print('R - Return car to Garage')
        print('U - Update Car Registry')
        print('')
        print('X - Exit')
        self.userChoice = input()

    def pushToCarArray(self, reg_value, manu_value, model_type, sipp_code, max_seating_capacity):
        self.carArray.append(reg_value)
        self.carArray.append(manu_value)
        self.carArray.append(model_type)
        self.carArray.append(sipp_code)
        self.carArray.append(max_seating_capacity)

        
    def addVehicleToDataBase(self):
        if self.userChoice.upper() == 'A':
            self.carObject
            
            reg_value = (input("What is the car's Registration Number?"))
            manu_value = (input(('What is the Manufactuer of the car?')))
            model_type = (input('What is the Model of the car?'))
            sipp_code = (input('What is the SIPP code for the car?'))
            max_seating_capacity = (input('What is the maximum seating capacity of the car?'))
            
            uiClass.pushToCarArray(reg_value, manu_value, model_type, sipp_code, max_seating_capacity)
            reg = self.carArray[0]
            manu = self.carArray[1]
            model = self.carArray[2]
            sipp = self.carArray[3]
            max_seat = self.carArray[4]
            self.carObject.reg_num(reg)
            self.carObject.manufacturer(manu)
            self.carObject.model_type(model)
            self.carObject.sipp_code(sipp)
            self.carObject.max_seating_capacity(4)
            # The code below writes a new row to the CSV, basically just gets an ID and makes the 
            # car list above into the form x,b,as,c,asf,
            #run the code and you'll see, should make sense
            csv_length = len(self.file)
            #goes through list and squishes it all into a string
            car_entry = str(csv_length + 2) + ',' + ','.join(str(x) for x in self.carArray)
            print(car_entry)
            #then open the file and write the new line easy peasy
            with open('CarRegistry.csv','a') as fd:
                fd.write('\n')
                return fd.write(car_entry)
    
    def deleteVehicleFromDatabase(self):
        if self.userChoice.upper() == 'D':
            (print('Which car do you want to delete from the registry? Please enter registration number: '))
            choice = input()
            #Did a simple delete too for you, pandas is super useful library to do it for you
            #Read up on it if you can but basically this the line below says to look in the 
            #dataframe (pandas converts csv to Dataframe which is just code way of reading it)
            #looks in the file and returns all rows where the REG column value does not
            # equal your choice
            self.file = self.file[self.file.REG != choice]
            #then literally just save the file, the index=False tells it not to create another 
            #index column
            return self.file.to_csv('CarRegistry.csv', index=False)
    
    def hireOutCar(self):
        if self.userChoice.upper() == 'H':
            print(('Which car do you want to hire out? Please enter registration number: '))
            choice = input()
            # print(choice)
            carToHireOut = self.file[self.file.REG == choice]
            if(carToHireOut['HIRED'].bool() == True):
                return print('This car has already been hired out sorry, sucks to be you...')
            else:
                self.file.loc[self.file['REG'] == choice, 'HIRED'] = True
                self.file.to_csv('CarRegistry.csv', index=False)
                return print('Have fun in that piece of shit car lol')
                
    def returnCar(self):
         if self.userChoice.upper() == 'R':
            print(('Which car do you want to return?: '))
            choice= input()
            self.file.loc[self.file['REG'] == choice, 'HIRED'] = False
            self.file.to_csv('CarRegistry.csv', index=False)
            return print('Christ, what did you do to that poor old car....')

    def generateUserChoices(self):
        uiClass.addVehicleToDataBase()
        uiClass.deleteVehicleFromDatabase()
        uiClass.hireOutCar()
        uiClass.returnCar()
        if self.userChoice.upper() == 'X':
            exit()
        

uiClass = UI()
uiClass.generateUserChoices()
