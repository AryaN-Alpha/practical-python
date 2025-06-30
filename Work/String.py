import re
symbols = ' AAPL,IBM,MSFT,YHOO,SCO'
print  (symbols[0], symbols[1])
# symbols[0]= 'b' error
new_word=',GOOG'

symbols = symbols+new_word
print(symbols)


new_word2='HPQ,'
symbols = new_word2+symbols
print(symbols)

print('GOOG' in symbols)
print('GO' in symbols)
print('G' in symbols)

print(symbols.lower())

print("From Start",symbols.find('GOOG'))
print("From End",symbols.rfind('GOOG'))

print(symbols[10:14])

print(symbols.replace('GOOG','REPLACED'))

new_string1= symbols.strip()      # used to remove white spaces
print(new_string1)

print(symbols.isalpha())          # Check if characters are alphabetic

print(symbols.isdigit())          # Check if characters are numeric

print(symbols.islower())          # Check if characters are lower-case
print(symbols.isupper())          # Check if characters are upper-case


print(symbols.startswith('HPQ'))  # Check if string starts with prefix


#fstrings


name="Aryan"
age= "22"
print(f'My name is {name} and I am "{age}" years old  ')


date= "Tomorrow is 30/06/2025 Today is 29/06/2025"

match = re.findall(r'\d+/\d+/\d+', date)  #\d+ mean digit in regex 
match1 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', date)
print(match)  
print(match1)                              

print(re.findall(r'(\d+)/(\d+)/(\d+)', date) )


list = symbols.split(',')
print(list)


s="sadasd"
print(dir(s))