import csv

# reading data as whole in a single string format
with open("Data/portfolio.csv" , 'rt') as file:
    data = file.read()
    print(data)



# Simple file read and storing data into array using split function
file_data=[]
with open("Data/portfolio.csv","rt") as file:
    for line in file:
        file_data.append(line.split(',')) 
        print(line)

print(file_data[1][2])
for lines in file_data:
    if(lines[1]!='shares'):
        print(int(lines[1])*2)


# by using external library called csv to read file in dictionary format
with open('Data/portfolio.csv') as file:
    data = csv.DictReader(file)
    for values in data:
        print(values['shares']*2)



#Lets practice how to write data into csv files 
with open("Testing_DataWriting/test.csv",'wt') as file:
    file.write("Aryan1,633,30") #Overwrites the data

    
# Lets practice how to write data into csv files 
with open("Testing_DataWriting/test.csv",'at') as file:
    file.write("name,rollno,marks\n")
    file.write("Aryan,63,20\n")