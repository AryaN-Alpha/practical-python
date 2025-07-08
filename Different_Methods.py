from collections import Counter
from collections import defaultdict 


portfolio = [
    ('GOOG', 100, 490.1),
    ('IBM', 50, 91.1),
    ('CAT', 150, 83.44),
    ('IBM', 100, 45.23),
    ('GOOG', 75, 572.45),
    ('AA', 50, 23.15)
]


total_shares=Counter() #create an empty dictionary with property that if key doesn't exit it create a key with 0 value by default

for name , shares , price in portfolio:
    total_shares[name] =total_shares[name]+shares

print(total_shares["IBM"])
print(total_shares['AA'])




#For one-many relations where you want some key to be associated with multiple values use defaultdictionary
#it also create a key upon doesn't exit but it create an empty list of each element

holdings =defaultdict(list)
for name,shares,price in portfolio:
    holdings[name].append((name,shares,price))

print(holdings['IBM'])


import csv
# from collections import deque
# history = deque(maxlen=5)
# with open('Data/portfolio.csv') as file:
#     Data= csv.DictReader(file)
#     for line in Data:
#         history.append(line)
#     print(history)


new_Val = Counter()
with open('Data/portfolio.csv') as file:
    Data= csv.DictReader(file)
    for line in Data:
        
        new_Val[line['name']]=new_Val[line['name']]+int(line['shares'])
print(new_Val)