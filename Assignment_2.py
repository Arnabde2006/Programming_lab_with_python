# ==========================================
# Lab 2: Programming Lab With Python
# Course Code: BCACC393
# ==========================================

# Question 1: Display length of a string using len()
print("--- Question 1 ---")
user_text = input("Enter a string: ")
print("Length of string =", len(user_text))

# Question 2: Accept two strings and concatenate them
print("\n--- Question 2 ---")
first_text = input("Enter first string: ")
second_text = input("Enter second string: ")
concatenated_text = first_text + second_text
print("Concatenated string =", concatenated_text)

# Question 3: Accept a string and display it in uppercase and lowercase
print("\n--- Question 3 ---")
text_to_convert = input("Enter a string: ")
uppercase_text = text_to_convert.upper()
lowercase_text = text_to_convert.lower()
print("Uppercase =", uppercase_text)
print("Lowercase =", lowercase_text)

# Question 4: Count occurrences of a particular character using count()
print("\n--- Question 4 ---")
target_string = input("Enter a string: ")
search_char = input("Enter the character to count: ")
char_occurrences = target_string.count(search_char)
print(f"Occurrences of '{search_char}' =", char_occurrences)

# Question 5: Replace one word with another using replace()
print("\n--- Question 5 ---")
original_text = input("Enter a string: ")
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the new word: ")
updated_text = original_text.replace(word_to_replace, replacement_word)
print("Resulting string =", updated_text)

# Question 6: Display student's name and age using f-string
print("\n--- Question 6 ---")
student_name = input("Enter student's name: ")
student_age = int(input("Enter student's age: "))
print(f"Student's name is {student_name} and age is {student_age}.")

# Question 7: Accept first name and last name and display full name using f-string
print("\n--- Question 7 ---")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
full_name = f"{first_name} {last_name}"
print(f"Student's full name is {full_name}.")

# Question 8: Create a list of five numbers and display length, max, and min
print("\n--- Question 8 ---")
sample_numbers = [1, 3, 4, 30, 6]
list_length = len(sample_numbers)
max_value = max(sample_numbers)
min_value = min(sample_numbers)
print("List =", sample_numbers)
print("Length =", list_length)
print("Maximum =", max_value)
print("Minimum =", min_value)

# Question 9: Calculate sum of list elements using sum()
print("\n--- Question 9 ---")
numbers_for_sum = [1, 3, 5, 37, 34]
total_sum = sum(numbers_for_sum)
print("List =", numbers_for_sum)
print("Sum =", total_sum)

# Question 10: Add an element at the end of a list using append()
print("\n--- Question 10 ---")
append_demo_list = [1, 3, 5, 37, 34]
print("Before append =", append_demo_list)
new_element = 20
append_demo_list.append(new_element)
print("After append =", append_demo_list)

# Question 11: Insert an element at a specified position using insert()
print("\n--- Question 11 ---")
insert_demo_list = [1, 3, 5, 37, 34]
print("Before insert =", insert_demo_list)
target_index = 1
value_to_insert = 10
insert_demo_list.insert(target_index, value_to_insert)
print("After insert =", insert_demo_list)

# Question 12: Remove a specified element using remove()
print("\n--- Question 12 ---")
remove_demo_list = [1, 3, 5, 37, 34]
print("Before remove =", remove_demo_list)
element_to_remove = 34
remove_demo_list.remove(element_to_remove)
print("After remove =", remove_demo_list)

# Question 13: Remove the last element using pop()
print("\n--- Question 13 ---")
pop_demo_list = [1, 3, 5, 37, 34]
print("Before pop =", pop_demo_list)
removed_last_element = pop_demo_list.pop()
print("Popped element =", removed_last_element)
print("After pop =", pop_demo_list)

# Question 14: Sort list in ascending order using sort()
print("\n--- Question 14 ---")
sortable_list = [1, 37, 5, 3, 34]
print("Before sort =", sortable_list)
sortable_list.sort()
print("Sorted list =", sortable_list)

# Question 15: Create a tuple of five numbers and display length, max, and min
print("\n--- Question 15 ---")
sample_tuple = (4, 65, 468, 46, 6)
tuple_length = len(sample_tuple)
tuple_max = max(sample_tuple)
tuple_min = min(sample_tuple)
print("Tuple =", sample_tuple)
print("Length =", tuple_length)
print("Maximum =", tuple_max)
print("Minimum =", tuple_min)

# Question 16: Count occurrences of an element in a tuple using count()
print("\n--- Question 16 ---")
occurrences_tuple = (4, 65, 468, 6, 6, 6)
target_value = 6
occurrence_count = occurrences_tuple.count(target_value)
print("Tuple =", occurrences_tuple)
print(f"Number of times {target_value} occurs =", occurrence_count)

# Question 17: Find position of an element in a tuple using index()
print("\n--- Question 17 ---")
index_demo_tuple = (4, 65, 468, 6, 6, 6)
searched_value = 65
found_position = index_demo_tuple.index(searched_value)
print("Tuple =", index_demo_tuple)
print(f"Position of {searched_value} =", found_position)

# Question 18: Convert list into tuple and display both
print("\n--- Question 18 ---")
source_list = [54, 22, 6, 70, 76]
converted_tuple = tuple(source_list)
print("Original list =", source_list)
print("Converted tuple =", converted_tuple)

# Question 19: Display student's name, roll number, and marks using f-string
print("\n--- Question 19 ---")
student_fullname = input("Enter student's name: ")
student_roll_no = int(input("Enter roll number: "))
student_marks = float(input("Enter marks: "))
print(f"Student's name is {student_fullname}, roll number is {student_roll_no}, and marks are {student_marks}.")

# Question 20: Accept name and 3 subject marks, calculate total & average, display using f-strings
print("\n--- Question 20 ---")
name_student = input("Enter student's name: ")
sub1_marks = float(input("Enter marks in Subject 1: "))
sub2_marks = float(input("Enter marks in Subject 2: "))
sub3_marks = float(input("Enter marks in Subject 3: "))

total_marks_obtained = sub1_marks + sub2_marks + sub3_marks
average_marks_obtained = total_marks_obtained / 3

print(f"Student Name: {name_student}")
print(f"Total Marks: {total_marks_obtained}")
print(f"Average Marks: {average_marks_obtained:.2f}")

# Question 21: Create a nested list containing three lists of numbers and display all elements
print("\n--- Question 21 ---")
nested_number_matrix = [
    [54, 22, 6, 70, 76],
    [45, 96, 48, 25, 75],
    [84, 92, 48, 55, 81]
]
print("Nested list =")
print(nested_number_matrix)

# Question 22: Create a nested list representing marks of 3 students in 3 subjects and calculate total for each
print("\n--- Question 22 ---")
student_marks_matrix = [
    [54, 22, 23],
    [45, 96, 48],
    [84, 48, 55]
]
for student_idx, marks_list in enumerate(student_marks_matrix, start=1):
    total_student_marks = sum(marks_list)
    print(f"Total marks of Student {student_idx} = {total_student_marks}")

# Question 23: Access a specific element of a nested list using row and column indexing
print("\n--- Question 23 ---")
grid_matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
print("Nested list:")
print(grid_matrix)
target_row, target_col = 1, 2
accessed_element = grid_matrix[target_row][target_col]
print(f"Element at row {target_row + 1}, column {target_col + 1} (index [{target_row}][{target_col}]) = {accessed_element}")

# Question 24: Nested tuple containing names and marks of 3 students, display details of each
print("\n--- Question 24 ---")
student_records_tuple = (
    ("Arnab", 85),
    ("Rahul", 78),
    ("Amit", 92)
)
for record in student_records_tuple:
    s_name, s_mark = record[0], record[1]
    print(f"Name: {s_name}, Marks: {s_mark}")

# Question 25: Nested tuple of numbers, calculate sum of elements of each inner tuple
print("\n--- Question 25 ---")
numbers_nested_tuple = (
    (10, 20, 30),
    (40, 50, 60),
    (70, 80, 90)
)
for tuple_idx, inner_tuple in enumerate(numbers_nested_tuple, start=1):
    inner_tuple_sum = sum(inner_tuple)
    print(f"Sum of tuple {tuple_idx} =", inner_tuple_sum)

# Question 26: Nested list of numbers, find maximum value from each inner list
print("\n--- Question 26 ---")
nested_lists_numbers = [
    [10, 25, 15],
    [45, 20, 35],
    [60, 55, 70]
]
for list_idx, inner_list in enumerate(nested_lists_numbers, start=1):
    max_in_list = max(inner_list)
    print(f"Maximum value of list {list_idx} =", max_in_list)

# Question 27: Nested list containing two lists of numbers, add corresponding elements
print("\n--- Question 27 ---")
two_lists_matrix = [
    [10, 20, 30],
    [40, 50, 60]
]
first_list = two_lists_matrix[0]
second_list = two_lists_matrix[1]
sum_corresponding_elements = []

for idx in range(len(first_list)):
    sum_corresponding_elements.append(first_list[idx] + second_list[idx])

print("First list =", first_list)
print("Second list =", second_list)
print("Sum of corresponding elements =", sum_corresponding_elements)

# Question 28: Nested tuple containing student names, roll numbers, and marks. Display using indexing and f-string.
print("\n--- Question 28 ---")
detailed_students_tuple = (
    ("Arnab", 101, 85),
    ("Rahul", 102, 78),
    ("Amit", 103, 92)
)
for student_record in detailed_students_tuple:
    student_name = student_record[0]
    student_roll = student_record[1]
    student_score = student_record[2]
    print(f"Student Name: {student_name}, Roll Number: {student_roll}, Marks: {student_score}")
