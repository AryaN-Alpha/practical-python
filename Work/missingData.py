import csv 
import math
def read_data():
    with open('Data/missing.csv') as file:
        Data=csv.DictReader(file)
        for count ,row in enumerate(Data, start=10):
            try:
                total = int(row['shares']) * float(row['price'])
                print(row)
            except:
                print("Invalid Data at: ",count)

# read_data()


#Lets practice zip() it is used to combine 2 values
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]

# Data =zip(columns,values)
# Data_list=[]
# for row in Data:
#     Data_Tuple = tuple(row)
#     Data_list.append(Data_Tuple)
# print(Data_list)


# Data2 =  zip(columns,values) #returns a tuple
# Data2_list=[]
# for row in Data2:
#     Data2_dictionary= dict([row]) # dict method expects an iterable element so when we give it single key,value pair it tries to iterate it 
#     Data2_list.append(Data2_dictionary) # since its a string it iterates through it so its gets 4 elements n a m e 
#                                         # soo to solve this we have to make it a list or list of tuples ((row)) so it treat it as a single element
# print(Data2_list)




prices = {
    'GOOG': 490.1,
    'AA': 23.45,
    'IBM': 91.1,
    'MSFT': 34.23
}

def testing_Zip():
    prices_tuple= zip( prices.values(),prices.keys() )
    prices_tuple2= list(zip( prices.keys(),prices.values() ))
    prices_list =list(prices_tuple)
    print(prices_list)
    prices_list.sort()
    print(prices_list)
    print(min(prices_list))
    print(max(prices_list))

    prices_tuple2.sort()
    print( prices_tuple2) # didn't sort the data to sort we must place data in the fist index
testing_Zip()