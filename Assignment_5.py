#1
print("Q1 - Non-Parameterized Function")

def greet():
    print("Welcome to Python Programming")

greet()


#2
print("Q2 - Function with No Arguments")

def display_info():
    print("Name: Arnab De")
    print("Department: BCA (Hons)")
    print("College: Institute of Engineering and Management, Kolkata")

display_info()


#3
print("Q3 - Function with Positional Arguments")

def add_numbers(a,b):
    print(f"Sum: {a+b}")
    print(f"Difference: {a-b}")
    print(f"Product: {a*b}")
    if b!=0:
        print(f"Quotient: {a/b}")
    else:
        print("Quotient: Cannot divide by zero")

add_numbers(20,4)


#4
print("Q4 - Parameterized Function")

def calculate_square(n):
    print(f"Square of {n} is {n**2}")
    print(f"Cube of {n} is {n**3}")

calculate_square(5)


#5
print("Q5 - Void Function")

def display_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

display_table(7)


#6
print("Q6 - Fruitful Function")

def calculate_area(length,width):
    return length*width

area=calculate_area(12,5)
print(f"Area of rectangle is {area}")


#7
print("Q7 - Function Returning Multiple Values")

def calculate(a,b):
    return a+b,a-b,a*b,a/b

s,d,p,q=calculate(40,8)
print("Sum:",s)
print("Difference:",d)
print("Product:",p)
print("Quotient:",q)


#8
print("Q8 - Function with Positional Arguments")

def student_result(name,marks1,marks2,marks3):
    total=marks1+marks2+marks3
    percentage=total/3
    print(f"Name: {name}")
    print(f"Total marks: {total}")
    print(f"Percentage: {percentage:.2f}%")

student_result("Arnab",78,85,92)


#9
print("Q9 - Function with Keyword Arguments")

def student_details(name,age,course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

student_details(course="BCA",name="Arnab",age=20)


#10
print("Q10 - Positional and Keyword Arguments")

def employee_details(name,department,salary):
    print(f"Name: {name}, Department: {department}, Salary: Rs.{salary}")

print("Only positional:")
employee_details("Rahul","IT",50000)
print("Only keyword:")
employee_details(salary=60000,name="Priya",department="HR")
print("Positional + keyword:")
employee_details("Amit",salary=45000,department="Finance")


#11
print("Q11 - Default Arguments")

def power(base,exponent=2):
    return base**exponent

print("Only base (5):",power(5))
print("Base and exponent (2,10):",power(2,10))


#12
print("Q12 - Function to Check Even or Odd")

def is_even(n):
    return n%2==0

num=17
if is_even(num):
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")


#13
print("Q13 - Lambda Function - Square")

square=lambda x:x**2
print("Square of 9 is",square(9))


#14
print("Q14 - Lambda Function - Maximum")

maximum=lambda a,b:a if a>b else b
print("Larger of 25 and 40 is",maximum(25,40))


#15
print("Q15 - Lambda Function - Conditional Expression")

check=lambda n:"Positive" if n>0 else ("Negative" if n<0 else "Zero")
print(check(10))
print(check(-3))
print(check(0))


#16
print("Q16 - map() Function")

numbers=[1,2,3,4,5,6,7,8,9,10]
squares=list(map(lambda x:x**2,numbers))
print("Squares:",squares)


#17
print("Q17 - map() with Multiple Lists")

a=[10,20,30,40,50]
b=[1,2,3,4,5]
result=list(map(lambda x,y:x+y,a,b))
print("Sum of corresponding elements:",result)


#18
print("Q18 - filter() Function")

numbers=[10,15,20,25,30,35,40,45,50]
evens=list(filter(lambda x:x%2==0,numbers))
print("Even numbers:",evens)


#19
print("Q19 - filter() - Prime Numbers")

def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

numbers=[2,3,4,5,6,7,8,9,10,11,13,15,17,20]
primes=list(filter(is_prime,numbers))
print("Prime numbers:",primes)


#20
print("Q20 - reduce() Function")

from functools import reduce

numbers=[10,20,30,40,50]
total=reduce(lambda x,y:x+y,numbers)
print("Sum of all elements:",total)


#21
print("Q21 - reduce() - Product")

product=reduce(lambda x,y:x*y,range(1,11))
print("Product of numbers from 1 to 10:",product)


#22
print("Q22 - Iterators")

nums=[11,22,33,44,55]
it=iter(nums)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
try:
    print(next(it))
except StopIteration:
    print("StopIteration raised - all elements have been consumed")


#23
print("Q23 - Custom Iterator")

class CountDown:
    def __init__(self,start):
        self.current=start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current<1:
            raise StopIteration
        value=self.current
        self.current-=1
        return value

for n in CountDown(5):
    print(n)


#24
print("Q24 - Generator Function")

def generate_numbers(n):
    for i in range(1,n+1):
        yield i

for num in generate_numbers(10):
    print(num)


#25
print("Q25 - Generator + Filtering")

def gen_50():
    for i in range(1,51):
        yield i

def div_by_3_and_5(gen):
    for num in gen:
        if num%3==0 and num%5==0:
            yield num

for num in div_by_3_and_5(gen_50()):
    print(num)
