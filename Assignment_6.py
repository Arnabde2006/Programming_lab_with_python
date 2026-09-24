# ---------------- Recursion ----------------

#1
print("Q1 - Factorial Using Recursion")

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

print("Factorial of 5 is",factorial(5))


#2
print("Q2 - Fibonacci Series Using Recursion")

def fibonacci(n):
    if n<=0:
        return []
    if n==1:
        return [0]
    if n==2:
        return [0,1]
    series=fibonacci(n-1)
    series.append(series[-1]+series[-2])
    return series

print("First 10 terms:",fibonacci(10))


#3
print("Q3 - Sum of Natural Numbers Using Recursion")

def sum_n(n):
    if n==0:
        return 0
    return n+sum_n(n-1)

print("Sum of first 10 natural numbers:",sum_n(10))


#4
print("Q4 - Reverse a Number Using Recursion")

def reverse_number(n,rev=0):
    if n==0:
        return rev
    return reverse_number(n//10,rev*10+n%10)

print("Reverse of 12345 is",reverse_number(12345))


# ---------------- Closures ----------------

#5
print("Q5 - Simple Closure Function")

def outer():
    msg="Hello from outer function"
    def inner():
        print(msg)
    return inner

f=outer()
f()


#6
print("Q6 - Closure for Power Calculation")

def power(n):
    def calc(x):
        return x**n
    return calc

square=power(2)
cube=power(3)
print("Square of 5:",square(5))
print("Cube of 5:",cube(5))
print("Power 4 of 3:",power(4)(3))


#7
print("Q7 - Counter Using Closure")

def make_counter():
    count=0
    def counter():
        nonlocal count
        count+=1
        return count
    return counter

c=make_counter()
print(c())
print(c())
print(c())


# ---------------- Decorators ----------------

#8
print("Q8 - Basic Function Decorator")

def display_message(func):
    def wrapper(*args,**kwargs):
        print("Function execution started")
        result=func(*args,**kwargs)
        print("Function execution completed")
        return result
    return wrapper

@display_message
def say_hello():
    print("Hello, World!")

say_hello()


#9
print("Q9 - Decorator for Measuring Execution")

import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f"Execution time of {func.__name__}: {end-start:.6f} seconds")
        return result
    return wrapper

@timer
def compute_sum(n):
    total=0
    for i in range(n):
        total+=i
    return total

print("Result:",compute_sum(1000000))


#10
print("Q10 - Decorator with Arguments")

def show_args(func):
    def wrapper(*args,**kwargs):
        print("Arguments passed:",args,kwargs)
        return func(*args,**kwargs)
    return wrapper

@show_args
def add(a,b):
    return a+b

print("Result:",add(10,20))


# ---------------- Classes and Objects ----------------

#11
print("Q11 - Create a Class and Objects")

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
s1.display()
s2.display()
s3.display()


#12
print("Q12 - Class Attributes")

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
print("After changing class attribute:",e1.company,e2.company)
e1.company="Personal Company"
print("After changing on e1 only:",e1.company,e2.company)


#13
print("Q13 - Methods in a Class")

class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

    def display(self):
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")

r=Rectangle(10,5)
r.display()


#14
print("Q14 - Private Methods")

class BankAccount:
    def __init__(self,balance,rate):
        self.balance=balance
        self.rate=rate

    def __calculate_interest(self):
        return self.balance*self.rate/100

    def show_interest(self):
        print(f"Interest on balance Rs.{self.balance} at {self.rate}% is Rs.{self.__calculate_interest()}")

acc=BankAccount(10000,5)
acc.show_interest()


# ---------------- Constructors and Destructors ----------------

#15
print("Q15 - Constructor in Python")

class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: Rs.{self.price}")

b=Book("Python Crash Course","Eric Matthes",599)
b.display()


#16
print("Q16 - Constructor and Destructor")

class Demo:
    def __init__(self):
        print("Object created (constructor called)")

    def __del__(self):
        print("Object destroyed (destructor called)")

d=Demo()
del d


# ---------------- Inheritance ----------------

#17
print("Q17 - Single Inheritance")

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


#18
print("Q18 - Multilevel Inheritance")

class Vehicle:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
        print(f"{self.brand} vehicle started")

class Car(Vehicle):
    def drive(self):
        print(f"{self.brand} car is being driven")

class ElectricCar(Car):
    def charge(self):
        print(f"{self.brand} electric car is charging")

ec=ElectricCar("Tesla")
ec.start()
ec.drive()
ec.charge()


#19
print("Q19 - Multiple Inheritance")

class Father:
    def father_skill(self):
        print("Father's skill: Carpentry")

class Mother:
    def mother_skill(self):
        print("Mother's skill: Cooking")

class Child(Father,Mother):
    pass

c=Child()
c.father_skill()
c.mother_skill()


# ---------------- Overloading and Method Overriding ----------------

#20
print("Q20 - Method Overloading Using Default Arguments")

class Calculator:
    def add(self,a,b,c=0):
        return a+b+c

calc=Calculator()
print("Add two numbers (10,20):",calc.add(10,20))
print("Add three numbers (10,20,30):",calc.add(10,20,30))


#21
print("Q21 - Operator Overloading")

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        return Point(self.x+other.x,self.y+other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1=Point(2,3)
p2=Point(4,5)
print("p1 + p2 =",p1+p2)


#22
print("Q22 - Method Overriding")

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks: Woof Woof")

class Cat(Animal):
    def sound(self):
        print("Cat meows: Meow Meow")

Animal().sound()
Dog().sound()
Cat().sound()


# ---------------- Abstract Base Class ----------------

#23
print("Q23 - Abstract Base Class (ABC)")

from abc import ABC,abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi*self.radius**2

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

print(f"Area of circle: {Circle(7).area():.2f}")
print(f"Area of rectangle: {Rectangle(10,5).area()}")
try:
    s=Shape()
except TypeError as e:
    print("Cannot instantiate abstract class:",e)


# ---------------- Metaclass ----------------

#24
print("Q24 - Basic Metaclass")

class MyMeta(type):
    def __new__(cls,name,bases,attrs):
        print(f"Creating class: {name}")
        return super().__new__(cls,name,bases,attrs)

class Student(metaclass=MyMeta):
    pass

s=Student()


#25
print("Q25 - Metaclass for Automatic Class Modification")

class CategoryMeta(type):
    def __new__(cls,name,bases,attrs):
        attrs["category"]="Python Class"
        return super().__new__(cls,name,bases,attrs)

class Teacher(metaclass=CategoryMeta):
    pass

class Course(metaclass=CategoryMeta):
    pass

print("Teacher.category:",Teacher.category)
print("Course.category:",Course.category)
