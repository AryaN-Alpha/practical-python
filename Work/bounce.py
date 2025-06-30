# bounce.py
#
# Exercise 1.5
initial_height=100
reduced_size=3/5;
new_height=initial_height

for i in range(10):
    new_height = new_height*reduced_size
    print(round(new_height , ndigits=2))