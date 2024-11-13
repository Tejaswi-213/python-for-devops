#value = 1001
#print(value)
#value = "Hello, Gopi Thungam!"
#print(value)
#value = 3.14
#print("Area equals: ", 5*5*value)
##############code 2###################################
#age = 21

#if age >= 21:
    #print("Going to Vegas!")
    #print("Feeling lucky!")
#else:
    #print("One of these days...")
#############code 3##################################
#age = 19

#if age >= 21:
    #print("Going to Vegas!")
    #print("Feeling lucky!")
#else:
    #print("One of these days...")

#################code 4#############################
#pet = "dog"

#if pet == 'dog':
    #print("Remember to buy dog biscuits")
#elif pet == 'cat':
    #print("Buy some catnip")
#else:
    #print("Buy something")

########################code 5###############
#pet = "cat"

#if pet == 'dog':
#print("Remember to buy dog biscuits")
#elif pet == 'cat':
#print("Buy some catnip")
#else:
#print("Buy something")
###############code 6################
#day = 'sunday'
#season = 'fall'

#if season == 'fall' and day == 'sunday':
#    print('Football season is here!')
#else:
#    print('Football season is coming!')
#
#language = 'c#'

#if language == "python" or language == 'R':
#    print('learn some machine language!')
#else:
#    print('Learn Python and R')
############code 7##################
#day = 'sunday'
#season = 'summer'

#if season == 'fall' and day == 'sunday':
#    print('Football season is here!')
#else:
#    print('Football season is coming!')
#
#language = 'c#'

#if language == "python" or language == 'R':
#    print('learn some machine language!')
#else:
#    print('Learn Python and R')
####################code 8########################3
#import pandas as pd
#
#data = pd.read_csv('Seattle.csv')
#
#for index, row in data.iterrows():
#   if row['price'] > 50000:
#       print(row)
####################code 9#########################
#import pandas as pd

#data = pd.read_csv('Seattle.csv')

#filtered_data = data[data['price'] > 500000]

#print(filtered_data)
#################### code 10 #########################
#import pandas as pd

#data = pd.read_csv('Seattle.csv')

#for index, row in data.iterrows():
 #      print(row['price'], row['sqft_living'])
#################### code 11 ##################
##
#x = [35,34,32,37,77,77,71,27,35,34,62,54,57,47,50,57,59,52,61,47,50,48,39,40,45,39,44,50,48]
#y = [79,54,52,77,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,23,22,13,14,22,7,29,25,9,8]

#index = 0
#while index < len(x):
#   plt.scatter(x[index], y[index], marker='x', color='red')
#   index += 1

#plt.show()
#################### code 12 ##################
class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

    def show(self):
        print('Name:', self.name) 
        print('Age:', self.age) 
        print('GPA:', self.gpa)


#jim = Student('John Doe', 20, 3.5)
#Mary = Student('Mary Davis', 22, 4.0)
Gopi = Student('GOPI THUNGAM', 25, 3.8)

#jim.show()
#Mary.show()
Gopi.show()
