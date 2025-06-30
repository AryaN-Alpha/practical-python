import random

names = [ 'Elwood', 'Jake', 'Curtis' ]
print(names[-1])

print(names*3) #replication creats array or 9 

list=[]
for i in range(10):
    list.append(random.randint(1,10)) 
print(list)

list.sort()
print(list)
list.sort(reverse=True)
print(list)


new_list = []
for i in range(10):
    new_list.append(random.randint(30,60)) 
print(new_list)

new_list2 = new_list[-5:]
new_list3 = new_list[0:-2]  
print(new_list2)
print(new_list3)



symbols = ' AAPL,IBM,MSFT,YHOO,SCO'

names = symbols.strip().split(',')

print('AAPL' in names)
print('AIG' not in names)
print('CAT' not in names)

print(names)
names.insert(2, "Aryan")
print(names)

names.remove("Aryan")
print(names)



names.append("YHOO")
names.append("YHOO")
print(names)
print(names.count("YHOO"))


names.remove('YHOO')
names.remove('YHOO')
print(names)

names_string1 = ','.join(names)
names_string2 = ':'.join(names)
names_string3 = '/'.join(names)
print(names_string1)
print(names_string2)
print(names_string3)


items=['spam', ['YHOO', 'RHT', 'HPQ', 'GOOG', 'AIG', 'AAPL', 'AA'], [101, 102, 103]]
print(items[1][2])
print(items[1][2][2])