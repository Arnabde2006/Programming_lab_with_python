# ==========================================
# Lab 1: Programming Lab With Python
# Course Code: BCACC393
# ==========================================

# Question 1: Write a Python program to print Hello, World!.
print("--- Question 1 ---")
print("Hello, World!")
print()

# Question 2: Write a Python program to accept the user's name and display a welcome message.
print("--- Question 2 ---")
user_name = input("Enter your name: ")
print("Welcome,", user_name)
print()

# Question 3: Write a Python program to accept two numbers and calculate their sum, subtraction, multiplication, and division.
print("--- Question 3 ---")
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))
sum_result = first_number + second_number
difference_result = first_number - second_number
product_result = first_number * second_number
division_result = first_number / second_number if second_number != 0 else "Undefined (division by zero)"
print("Sum:", sum_result)
print("Subtraction:", difference_result)
print("Multiplication:", product_result)
print("Division:", division_result)
print()

# Question 4: Write a Python program to calculate the area of a circle by accepting the radius from the user.
print("--- Question 4 ---")
radius = float(input("Enter the radius of the circle: "))
circle_area = 3.14159 * (radius ** 2)
print("Area of circle:", circle_area)
print()

# Question 5: Write a Python program to calculate the area of a rectangle by accepting length and breadth from the user.
print("--- Question 5 ---")
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
rectangle_area = length * breadth
print("Area of rectangle:", rectangle_area)
print()

# Question 6: Write a Python program to convert temperature from Celsius to Fahrenheit.
print("--- Question 6 ---")
celsius_temp = float(input("Enter temperature in Celsius: "))
fahrenheit_temp = (celsius_temp * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit_temp)
print()

# Question 7: Write a Python program to accept a number and display its data type using the type() function.
print("--- Question 7 ---")
input_number = float(input("Enter a number: "))
print("Data type of entered number:", type(input_number))
print()

# Question 8: Write a Python program to demonstrate type casting by converting a string into an integer and a floating-point number.
print("--- Question 8 ---")
numeric_string = input("Enter a numeric string (e.g. 42): ")
converted_integer = int(numeric_string)
converted_float = float(numeric_string)
print("Original string:", numeric_string, "| Type:", type(numeric_string))
print("Converted to integer:", converted_integer, "| Type:", type(converted_integer))
print("Converted to float:", converted_float, "| Type:", type(converted_float))
print()

# Question 9: Write a Python program to accept three numbers and calculate their average.
print("--- Question 9 ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average_val = (num1 + num2 + num3) / 3
print("Average:", average_val)
print()

# Question 10: Write a Python program to accept a student's name and marks in three subjects and calculate the total and average marks.
print("--- Question 10 ---")
student_name = input("Enter student name: ")
subject1_marks = float(input("Enter marks for subject 1: "))
subject2_marks = float(input("Enter marks for subject 2: "))
subject3_marks = float(input("Enter marks for subject 3: "))
total_marks = subject1_marks + subject2_marks + subject3_marks
average_marks = total_marks / 3
print("Student Name:", student_name)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print()

# Question 11: Write a Python program to create a list of five numbers and display all the elements of the list.
print("--- Question 11 ---")
numbers_list = [10, 20, 30, 40, 50]
print("List elements:", numbers_list)
print()

# Question 12: Write a Python program to create a list of five numbers and display the first and last elements using indexing.
print("--- Question 12 ---")
sample_list = [10, 20, 30, 40, 50]
first_element = sample_list[0]
last_element = sample_list[-1]
print("First element:", first_element)
print("Last element:", last_element)
print()

# Question 13: Write a Python program to create a list of numbers and add a new element using the append() function.
print("--- Question 13 ---")
dynamic_list = [10, 20, 30, 40, 50]
print("Before append:", dynamic_list)
new_element = 60
dynamic_list.append(new_element)
print("After append:", dynamic_list)
print()

# Question 14: Write a Python program to create a list of numbers and remove an element using the remove() function.
print("--- Question 14 ---")
removable_list = [10, 20, 30, 40, 50]
print("Before remove:", removable_list)
element_to_remove = 30
removable_list.remove(element_to_remove)
print("After remove:", removable_list)
print()

# Question 15: Write a Python program to create a tuple of five numbers and display its elements.
print("--- Question 15 ---")
numbers_tuple = (10, 20, 30, 40, 50)
print("Tuple elements:", numbers_tuple)
print()

# Question 16: Write a Python program to create a string and display its first character, last character, and length.
print("--- Question 16 ---")
sample_string = input("Enter a string: ")
first_character = sample_string[0]
last_character = sample_string[-1]
string_length = len(sample_string)
print("First character:", first_character)
print("Last character:", last_character)
print("Length of string:", string_length)
print()

# Question 17: Write a Python program to create a list of five numbers and remove the last element using the pop() function. Display the list before and after using pop().
print("--- Question 17 ---")
pop_list = [10, 20, 30, 40, 50]
print("List before pop():", pop_list)
popped_element = pop_list.pop()
print("Popped element:", popped_element)
print("List after pop():", pop_list)
print()

# Question 18: Write a Python program to create a list of five elements and use pop() to remove an element at a specified index.
print("--- Question 18 ---")
indexed_pop_list = [10, 20, 30, 40, 50]
print("List before pop(index):", indexed_pop_list)
target_index = 2
removed_element = indexed_pop_list.pop(target_index)
print(f"Removed element at index {target_index}:", removed_element)
print("List after pop(index):", indexed_pop_list)

