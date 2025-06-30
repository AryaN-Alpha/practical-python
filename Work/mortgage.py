# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = int(input("enter the start of the month: "))
extra_payment_end_month = int(input("enter the end of the month: "))
extra_payment = int(input("enter extra payment: "))



count=0
while principal > 0:
    principal = principal * (1+rate/12) - payment
    if(principal<0):
        break
    total_paid = total_paid + payment
    count = count+1
    if(count>=extra_payment_start_month and count<=extra_payment_end_month):
        principal= principal-extra_payment
        total_paid=total_paid+extra_payment
        print("if condition: ",count)
    print(count,"\t" , total_paid ,"\t" ,principal)



print('Total paid', total_paid)
print('Months: ' , count)