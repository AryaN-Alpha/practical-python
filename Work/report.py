# report.py
#
# Exercise 2.4
import csv 
portfolio = []
def read_portfolio():

    with open('Data/portfolio.csv','rt') as file:
        row =  csv.DictReader(file)
        for key in row:   
            if(key['shares'].isdigit()):
                portfolio.append((key['name'] , int(key['shares']), float(key['price'])))
            
    print(portfolio)

read_portfolio()


def read_report():
    portfolio= []
    with open('Data/portfolio.csv') as file:
        data=csv.DictReader(file)
        for row in data:
            total = int(row['shares'])*float(row['price'])
            portfolio.append({'name':row['name'], 'shares':int(row['shares']), 'price':f'{float(row['price']):.2f}', 'total': f"{total:.2f}" })
    return portfolio        


Data = read_report()


def make_report(Data):
    Data_Tuple=[]
    for row in Data:
        temp=[]
        for key in row:
            temp.append(row[key])

        Data_Tuple.append(tuple(temp))
        temp=[]
    return Data_Tuple

Data_Tuple= make_report(Data)

def print_report(Data):
    print(f'{"Name":10s} {"Shares":10s} {"Price":10s}') 
    print(f'{"-"*10:10s} {"-"*10:10s} {"-"*10:10s}') 
    
    for row in Data:
        print(f'{row['name']:10s} {int(row['shares']):10d} {float(row['price']):10.2f}')    

print_report(Data)