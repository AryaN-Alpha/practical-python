# pcost.py
#
# Exercise 1.27

# data_list= []
# with open('Data/portfolio.csv' , 'rt') as file:
#     for line in file:
#         line = line.strip('\n')
#         data_list.append(line.split(','))  
# total=0
# for values in data_list:
#     if(values[0]!='name'):
#         shares=int(values[1])
#         price= float(values[2])
#         total= total+(shares*price)


# print("Total Stock Price: ",total)



#to read gzip compressed file we use gzip we cannot use open directly
# import gzip
# with gzip.open('Data/portfolio.csv.gz','rt') as file:
#     for line in file:
#         print(line)




import sys 
if(len(sys.argv)==2):
    filepath=sys.argv[1]
else:
    filepath="Data/portfolio.csv"


def portfolio_cost(path):
    data_list= []
    with open(path , 'rt') as file:
        for line in file:
            line = line.strip('\n')
            data_list.append(line.split(','))  
    total=0
    for values in data_list:
        if(values[0]!='name'):
            shares=int(values[1])
            price= float(values[2])
            total= total+(shares*price)


    return total


cost = portfolio_cost(filepath)
print("Total Stock Cost: ",portfolio_cost(filepath))