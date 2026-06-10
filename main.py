
# print("Hello World")

# List of Numbers through #'s variable
numbers = [1, 15, 30, 45, 60]
# print(numbers)

# Function #1 named calculate_total
def calculate_total(nums_list):
    # Total variable to store the running total
    total = 0

    # This loop means go through every # in the list one at a time/ Add each # one by one starting from top
    for number in nums_list:
        total = total + number
    return total

# Function #2 named display_numbers
def display_numbers(nums_list):
    # Heading (print on terminal)
    print("Numbers in the list:")

    # This loop goes through every # in the list one at a time & prints the # on the terminal
    for number in nums_list:
        print(number)


display_numbers(numbers)
total = calculate_total(numbers)
print("The total is:", total)