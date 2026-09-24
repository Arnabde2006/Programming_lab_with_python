#1
print("Q1 - Electricity Bill")

units=float(input("Enter units consumed: "))

if units<=100:
    bill=units*3
elif units<=300:
    bill=100*3+(units-100)*5
elif units<=500:
    bill=100*3+200*5+(units-300)*7
else:
    bill=100*3+200*5+200*7+(units-500)*9

print(f"Total electricity bill is Rs.{bill}")


#2
print("Q2 - Cinema Ticket Pricing")

age=int(input("Enter your age: "))

if age<5:
    print("Category: Infant, Price: Free")
elif age<=12:
    print("Category: Child, Price: Rs.100")
elif age<=59:
    print("Category: Adult, Price: Rs.200")
else:
    print("Category: Senior Citizen, Price: Rs.120")


#3
print("Q3 - ATM Withdrawal")

balance=float(input("Enter account balance: "))
amount=float(input("Enter withdrawal amount: "))

if amount>balance:
    print("Withdrawal denied: Insufficient balance")
elif amount%100!=0:
    print("Withdrawal denied: Amount must be a multiple of 100")
else:
    print("Withdrawal approved")
    balance=balance-amount
    print(f"Remaining balance: {balance}")


#4
print("Q4 - Library Fine Calculator")

days=int(input("Enter number of days book is late: "))

if days<=0:
    print("No fine, book returned on time")
elif days<=5:
    fine=days*2
    print(f"Fine amount: Rs.{fine}")
elif days<=10:
    fine=5*2+(days-5)*5
    print(f"Fine amount: Rs.{fine}")
else:
    fine=5*2+5*5+(days-10)*10
    print(f"Fine amount: Rs.{fine}")


#5
print("Q5 - Online Exam Result")

percentage=float(input("Enter percentage: "))

if percentage>=90:
    grade="A+"
    result="Pass"
elif percentage>=75:
    grade="A"
    result="Pass"
elif percentage>=60:
    grade="B"
    result="Pass"
elif percentage>=40:
    grade="C"
    result="Pass"
else:
    grade="F"
    result="Fail"

print(f"Grade: {grade}, Result: {result}")


#6
print("Q6 - The Daily Step Challenge")

total_steps=0
for day in range(1,8):
    steps=int(input(f"Enter steps walked on day {day}: "))
    total_steps=total_steps+steps

avg_steps=total_steps/7
print(f"Total steps in 7 days: {total_steps}")
print(f"Average steps per day: {avg_steps:.2f}")


#7
print("Q7 - The Classroom Attendance")

present=0
absent=0
for student in range(1,11):
    status=input(f"Enter status for student {student} (P/A): ").upper()
    if status=="P":
        present=present+1
    else:
        absent=absent+1

print(f"Total present: {present}")
print(f"Total absent: {absent}")


#8
print("Q8 - The Smart Piggy Bank")

total_savings=0
highest=0
for day in range(1,11):
    amount=float(input(f"Enter amount saved on day {day}: "))
    total_savings=total_savings+amount
    if amount>highest:
        highest=amount

print(f"Total savings: Rs.{total_savings}")
print(f"Highest amount saved in a single day: Rs.{highest}")


#9
print("Q9 - The Number Detective")

positive=0
negative=0
zero=0
for i in range(1,21):
    num=int(input(f"Enter number {i}: "))
    if num>0:
        positive=positive+1
    elif num<0:
        negative=negative+1
    else:
        zero=zero+1

print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zero count: {zero}")


#10
print("Q10 - The Cafeteria Counter")

food_count={}
for student in range(1,16):
    item=input(f"Enter food item ordered by student {student}: ")
    food_count[item]=food_count.get(item,0)+1

print("Food order count:", food_count)


#11
print("Q11 - The Treasure Hunt")

secret=42
attempts=0
guess=-1
while guess!=secret:
    guess=int(input("Guess the secret number: "))
    attempts=attempts+1
    if guess!=secret:
        print("Wrong guess, try again")

print(f"Correct! Number of attempts made: {attempts}")


#12
print("Q12 - The ATM Security System")

correct_pin=1234
attempts=0
access=False

while attempts<3:
    pin=int(input("Enter your PIN: "))
    attempts=attempts+1
    if pin==correct_pin:
        access=True
        break
    else:
        print("Incorrect PIN")

if access:
    print("Access granted")
else:
    print("Account locked after 3 incorrect attempts")


#13
print("Q13 - The Coffee Machine")

choice=0
while True:
    print("1.Coffee\n2.Tea\n3.Hot Chocolate\n4.Exit")
    choice=int(input("Select an option: "))
    if choice==1:
        print("Dispensing Coffee")
    elif choice==2:
        print("Dispensing Tea")
    elif choice==3:
        print("Dispensing Hot Chocolate")
    elif choice==4:
        print("Exiting machine")
        break
    else:
        print("Invalid option, try again")

    if choice==4:
        break


#14
print("Q14 - The Student Registration Counter")

count=0
more="yes"
while more=="yes":
    sname=input("Enter student name: ")
    roll=input("Enter roll number: ")
    count=count+1
    more=input("Register another student? (yes/no): ").lower()

print(f"Total number of registered students: {count}")


#15
print("Q15 - The Bank Deposit Machine")

overall_deposit=0
for customer in range(1,4):
    customer_total=0
    for deposit in range(1,4):
        amount=float(input(f"Enter deposit {deposit} for customer {customer}: "))
        customer_total=customer_total+amount
    print(f"Total deposit by customer {customer}: Rs.{customer_total}")
    overall_deposit=overall_deposit+customer_total

print(f"Overall bank deposit: Rs.{overall_deposit}")


#16
print("Q16 - The Mini Shopping System")

prices={"apple":50,"bread":40,"milk":30,"egg":6,"butter":90}
cart={}
subtotal=0

while True:
    pname=input("Enter product name (or 'checkout' to finish): ").lower()
    if pname=="checkout":
        break
    if pname not in prices:
        print("Product not available")
        continue
    qty=int(input(f"Enter quantity of {pname}: "))
    cart[pname]=cart.get(pname,0)+qty
    subtotal=subtotal+prices[pname]*qty

if subtotal>=5000:
    discount=subtotal*0.20
elif subtotal>=3000:
    discount=subtotal*0.10
elif subtotal>=1000:
    discount=subtotal*0.05
else:
    discount=0

final_bill=subtotal-discount

print("Purchased items:",cart)
print(f"Subtotal: Rs.{subtotal}")
print(f"Discount: Rs.{discount}")
print(f"Final bill: Rs.{final_bill}")


#17
print("Q17 - The Morning Exercise Challenge")

total_time=0
for day in range(1,8):
    minutes=int(input(f"Enter exercise minutes for day {day}: "))
    total_time=total_time+minutes

print(f"Total exercise time in 7 days: {total_time} minutes")


#18
print("Q18 - The Classroom Book Counter")

books=[]
for student in range(1,11):
    book=input(f"Enter book name brought by student {student}: ")
    books.append(book)

print("Books collected:",books)


#19
print("Q19 - The Fruit Basket")

fruits=[]
for i in range(1,6):
    fruit=input(f"Enter fruit {i}: ")
    fruits.append(fruit)

print("Fruits in the basket:",fruits)


#20
print("Q20 - The Daily Water Tracker")

total_glasses=0
for day in range(1,8):
    glasses=int(input(f"Enter glasses of water on day {day}: "))
    total_glasses=total_glasses+glasses

print(f"Total glasses of water consumed in the week: {total_glasses}")


#21
print("Q21 - The School Bus Attendance")

for seat in range(1,9):
    sname=input(f"Enter name of student for seat {seat}: ")
    print(f"Seat {seat}: {sname}")
