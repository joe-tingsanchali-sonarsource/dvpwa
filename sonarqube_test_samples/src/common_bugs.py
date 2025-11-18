"""
Common Bugs Test File
This file contains intentional bugs and errors for SonarQube testing.
"""

# Bug 1: Variable used before assignment
def get_total_price():
    if False:
        total = 100
    return total  # total might not be defined

# Bug 2: Division by zero risk
def calculate_average(numbers):
    return sum(numbers) / len(numbers)  # Will fail if numbers is empty

# Bug 3: Comparing with None using == instead of is
def check_value(value):
    if value == None:  # Should use 'is None'
        return False
    return True

# Bug 4: Modifying list while iterating
def remove_negatives(numbers):
    for num in numbers:
        if num < 0:
            numbers.remove(num)  # Unsafe modification during iteration
    return numbers

# Bug 5: Incorrect exception handling order
def parse_data(data):
    try:
        return int(data)
    except Exception as e:  # Too broad, should be more specific
        print("Error")
    except ValueError:  # Will never be reached
        print("Value error")

# Bug 6: Resource leak - file not closed
def read_config():
    file = open('config.txt', 'r')
    data = file.read()
    # File not closed
    return data

# Bug 7: Shadowing built-in names
def process_list(list):  # 'list' shadows built-in
    sum = 0  # 'sum' shadows built-in
    for item in list:
        sum += item
    return sum

# Bug 8: Incorrect string comparison
def validate_input(user_input):
    if user_input is "admin":  # Should use ==, not is
        return True
    return False

# Bug 9: Missing return statement in non-void function
def get_user_age(user):
    if hasattr(user, 'age'):
        return user.age
    # Missing return for else case

# Bug 10: Unreachable code after return
def calculate_score(points):
    if points > 100:
        return 100
        points = 100  # Unreachable
    return points

# Bug 11: Incorrect use of is for comparison
def check_number(value):
    if value is 42:  # Should use ==
        return "Found"
    return "Not found"

# Bug 12: Off-by-one error in loop
def get_first_ten_items(items):
    result = []
    for i in range(1, 11):  # Should start from 0
        result.append(items[i])
    return result

# Bug 13: Comparing with identity operator instead of equality
def is_valid(status):
    if status is 'active':  # Should be ==, not is for strings
        return True
    return False

# Bug 14: Incorrect variable scope
class Counter:
    def increment(self):
        count = 0  # Local variable, not using instance variable
        count += 1
        return count  # Will always return 1

# Bug 15: Missing break in case-like structure
def get_day_type(day):
    day_type = "unknown"
    if day == "Monday":
        day_type = "weekday"
    if day == "Tuesday":
        day_type = "weekday"
    if day == "Wednesday":
        day_type = "weekday"
    # Inefficient structure, should use elif
    return day_type

# Bug 16: Incorrect boolean logic
def is_eligible(age, has_license):
    return not (age >= 18 or has_license)  # Logic likely incorrect

# Bug 17: Type confusion
def add_numbers(a, b):
    return a + b  # No type checking, could concatenate strings

# Bug 18: Ignoring function return value
def save_user(user):
    validate_user(user)  # Return value ignored
    # Continue without checking if validation passed
    return True

def validate_user(user):
    if not user.get('email'):
        return False
    return True

