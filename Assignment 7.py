# ================= Part A - Object-Oriented Programming =================

#1
print("Q1 - Class and Objects")

class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def display(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

s1=Student("Arnab",1,85)
s2=Student("Rahul",2,78)
s3=Student("Priya",3,92)
for s in (s1,s2,s3):
    s.display()


#2
print("Q2 - Constructor")

class Employee:
    def __init__(self,name,employee_id,department,salary):
        self.name=name
        self.employee_id=employee_id
        self.department=department
        self.salary=salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Department: {self.department}")
        print(f"Salary: Rs.{self.salary}")

Employee("Amit",101,"IT",55000).display()


#3
print("Q3 - Instance and Class Attributes")

class Employee:
    company="ABC Technologies"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

e1=Employee("Amit",50000)
e2=Employee("Neha",60000)
print(e1.name,e1.salary,e1.company)
print(e2.name,e2.salary,e2.company)
Employee.company="XYZ Technologies"
print("Class attribute changed -> e1:",e1.company,"| e2:",e2.company)
e1.salary=70000
print("Instance attribute changed for e1 only -> e1 salary:",e1.salary,"| e2 salary:",e2.salary)


#4
print("Q4 - Instance Methods")

import math

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    def diagonal(self):
        return math.sqrt(self.length**2+self.width**2)

r=Rectangle(8,6)
print("Area:",r.area())
print("Perimeter:",r.perimeter())
print("Diagonal:",r.diagonal())


#5
print("Q5 - Private Attributes and Methods")

class BankAccount:
    def __init__(self,account_no,balance):
        self.__account_no=account_no
        self.__balance=balance

    def __calculate_interest(self):
        return self.__balance*5/100

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited Rs.{amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if amount>self.__balance:
            print("Insufficient balance")
        elif amount<=0:
            print("Invalid withdrawal amount")
        else:
            self.__balance-=amount
            print(f"Withdrew Rs.{amount}")

    def display_balance(self):
        print(f"Account No: {self.__account_no}, Balance: Rs.{self.__balance}")

    def show_interest(self):
        print(f"Interest at 5%: Rs.{self.__calculate_interest()}")

acc=BankAccount("SB1001",10000)
acc.display_balance()
acc.deposit(5000)
acc.withdraw(3000)
acc.withdraw(50000)
acc.display_balance()
acc.show_interest()


#6
print("Q6 - Inheritance")

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Student(Person):
    def __init__(self,name,age,roll_no,course):
        super().__init__(name,age)
        self.roll_no=roll_no
        self.course=course

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.roll_no}, Course: {self.course}")

Student("Arnab",20,101,"BCA").display()


#7
print("Q7 - Multilevel Inheritance")

class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is being driven")

class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")

ec=ElectricCar()
ec.start()
ec.drive()
ec.charge()


#8
print("Q8 - Multiple Inheritance")

class Father:
    def father_skill(self):
        print("Father's skill: Carpentry")

class Mother:
    def mother_skill(self):
        print("Mother's skill: Painting")

class Child(Father,Mother):
    pass

c=Child()
c.father_skill()
c.mother_skill()


#9
print("Q9 - Hierarchical Inheritance")

class Shape:
    def display(self):
        print("This is a shape")

class Circle(Shape):
    def area(self,r):
        return math.pi*r*r

class Rectangle(Shape):
    def area(self,l,w):
        return l*w

class Triangle(Shape):
    def area(self,b,h):
        return 0.5*b*h

c=Circle()
r=Rectangle()
t=Triangle()
c.display()
print(f"Circle area: {c.area(5):.2f}")
r.display()
print("Rectangle area:",r.area(10,4))
t.display()
print("Triangle area:",t.area(6,3))


#10
print("Q10 - Method Overriding")

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof Woof")

class Cat(Animal):
    def sound(self):
        print("Cat meows: Meow Meow")

class Cow(Animal):
    def sound(self):
        print("Cow moos: Moo Moo")

for a in (Animal(),Dog(),Cat(),Cow()):
    a.sound()


#11
print("Q11 - Operator Overloading")

class Distance:
    def __init__(self,feet,inches):
        self.feet=feet
        self.inches=inches

    def __add__(self,other):
        total_inches=self.inches+other.inches
        total_feet=self.feet+other.feet+total_inches//12
        return Distance(total_feet,total_inches%12)

    def __str__(self):
        return f"{self.feet} feet {self.inches} inches"

d1=Distance(5,8)
d2=Distance(3,7)
print("d1:",d1)
print("d2:",d2)
print("d1 + d2 =",d1+d2)


#12
print("Q12 - Method Overloading Using Default Arguments")

class Calculator:
    def add(self,a,b,c=0):
        return a+b+c

calc=Calculator()
print("Two numbers (10,20):",calc.add(10,20))
print("Three numbers (10,20,30):",calc.add(10,20,30))


#13
print("Q13 - Abstract Base Class (ABC)")

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.r=r

    def area(self):
        return math.pi*self.r**2

class Rectangle(Shape):
    def __init__(self,l,w):
        self.l=l
        self.w=w

    def area(self):
        return self.l*self.w

class Triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h

    def area(self):
        return 0.5*self.b*self.h

print(f"Circle: {Circle(7).area():.2f}")
print("Rectangle:",Rectangle(10,5).area())
print("Triangle:",Triangle(8,4).area())


#14
print("Q14 - Polymorphism")

def show_area(shape):
    print(f"{type(shape).__name__} area = {shape.area():.2f}")

shapes=[Circle(3),Rectangle(4,6),Triangle(5,10)]
for sh in shapes:
    show_area(sh)


#15
print("Q15 - Metaclass")

class MyMeta(type):
    def __new__(cls,name,bases,attrs):
        attrs["category"]="Python Class"
        return super().__new__(cls,name,bases,attrs)

class Book(metaclass=MyMeta):
    pass

class Pen(metaclass=MyMeta):
    pass

print("Book.category:",Book.category)
print("Pen.category:",Pen.category)


# ================= Part B - Errors, Exceptions and File Handling =================

#16
print("Q16 - Handling Division by Zero")

try:
    a=float(input("Enter numerator: "))
    b=float(input("Enter denominator: "))
    print("Result:",a/b)
except ZeroDivisionError:
    print("Error: Denominator cannot be zero")


#17
print("Q17 - Multiple Exception Handling")

try:
    a=int(input("Enter first integer: "))
    b=int(input("Enter second integer: "))
    print("Result:",a/b)
except ValueError:
    print("Error: Please enter valid integers")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")


#18
print("Q18 - try-except-else-finally")

try:
    n=int(input("Enter an integer: "))
except ValueError:
    print("Error: Invalid integer")
else:
    print(f"Square of {n} is {n*n}")
finally:
    print("Execution completed (finally block)")


#19
print("Q19 - Raising User-Defined Exceptions")

class InvalidAgeError(Exception):
    pass

try:
    age=int(input("Enter your age: "))
    if age<18:
        raise InvalidAgeError("Age must be 18 or above")
    print("Valid age. Access granted.")
except InvalidAgeError as e:
    print("InvalidAgeError:",e)
except ValueError:
    print("Error: Please enter a number")


#20
print("Q20 - Handling Multiple Exceptions")

try:
    a=float(input("Enter first value: "))
    b=float(input("Enter second value: "))
    print("Addition:",a+b)
    print("Subtraction:",a-b)
    print("Multiplication:",a*b)
    print("Division:",a/b)
    print("Modulus:",a%b)
    print("Power:",a**b)
except ValueError:
    print("Error: Invalid input, please enter numbers only")
except ZeroDivisionError:
    print("Error: Division by zero")
except OverflowError:
    print("Error: Result too large")
except Exception as e:
    print("Unexpected error:",e)


#21
print("Q21 - Create and Write to a Text File")

name=input("Enter student name: ")
roll=input("Enter roll number: ")
course=input("Enter course: ")
marks=input("Enter marks: ")

with open("student.txt","w") as f:
    f.write(f"Student Name: {name}\n")
    f.write(f"Roll Number: {roll}\n")
    f.write(f"Course: {course}\n")
    f.write(f"Marks: {marks}\n")
print("student.txt created successfully")


#22
print("Q22 - Read Data from a File")

print("Using read():")
with open("student.txt","r") as f:
    print(f.read())

print("Using readline():")
with open("student.txt","r") as f:
    line=f.readline()
    while line:
        print(line,end="")
        line=f.readline()


#23
print("\nQ23 - Count Lines, Words, and Characters")

lines=words=chars=0
with open("student.txt","r") as f:
    for line in f:
        lines+=1
        words+=len(line.split())
        chars+=len(line)
print("Lines:",lines)
print("Words:",words)
print("Characters:",chars)


#24
print("Q24 - Copy File Contents")

with open("source.txt","w") as f:
    f.write("This is the source file.\nIt has two lines.\n")

with open("source.txt","r") as src,open("destination.txt","w") as dest:
    dest.write(src.read())
print("File copied successfully from source.txt to destination.txt")


#25
print("Q25 - File Handling with Exception Handling")

fname=input("Enter filename: ")
f=None
try:
    f=open(fname,"r")
    print(f.read())
except FileNotFoundError:
    print("Error: File not found")
except PermissionError:
    print("Error: Permission denied")
except Exception as e:
    print("Unexpected error:",e)
finally:
    if f:
        f.close()
    print("File operation completed")
