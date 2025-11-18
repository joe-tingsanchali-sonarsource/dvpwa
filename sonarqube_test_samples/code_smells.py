"""
Code Smells Test File
This file contains intentional code smells and bad practices for SonarQube testing.
"""

import time

# Code Smell 1: Unused imports
import sys
import json
import datetime
from typing import List, Dict

# Code Smell 2: Commented out code
# def old_function():
#     print("This is old code")
#     return True
# result = old_function()

# Code Smell 3: Too many parameters (>7 parameters)
def create_user(first_name, last_name, email, phone, address, city, state, zip_code, country, age):
    return {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'address': address,
        'city': city,
        'state': state,
        'zip': zip_code,
        'country': country,
        'age': age
    }

# Code Smell 4: Cognitive complexity - deeply nested conditionals
def process_order(order, user, payment):
    if order is not None:
        if user is not None:
            if user.is_active:
                if payment is not None:
                    if payment.amount > 0:
                        if payment.method == 'credit_card':
                            if payment.card_valid:
                                if order.items:
                                    return True
    return False

# Code Smell 5: Magic numbers scattered throughout
def calculate_discount(price):
    if price > 100:
        return price * 0.15
    elif price > 50:
        return price * 0.10
    elif price > 25:
        return price * 0.05
    return 0

# Code Smell 6: Duplicated code blocks
def send_welcome_email(user):
    subject = "Welcome!"
    body = f"Hello {user.name}, welcome to our platform!"
    sender = "noreply@example.com"
    recipient = user.email
    print(f"Sending email to {recipient}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    return True

def send_goodbye_email(user):
    subject = "Goodbye!"
    body = f"Hello {user.name}, sorry to see you go!"
    sender = "noreply@example.com"
    recipient = user.email
    print(f"Sending email to {recipient}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    return True

# Code Smell 7: Long method with too many lines and responsibilities
def process_user_registration(username, password, email, first_name, last_name, age, address):
    # Validate username
    if len(username) < 3:
        return False
    if len(username) > 20:
        return False
    
    # Validate password
    if len(password) < 8:
        return False
    has_digit = False
    has_upper = False
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
    if not has_digit or not has_upper:
        return False
    
    # Validate email
    if '@' not in email:
        return False
    if '.' not in email:
        return False
    
    # Hash password
    import hashlib
    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    # Save to database
    user_data = {
        'username': username,
        'password': hashed,
        'email': email,
        'first_name': first_name,
        'last_name': last_name,
        'age': age,
        'address': address
    }
    
    # Send welcome email
    print(f"Sending welcome email to {email}")
    
    # Log registration
    print(f"User {username} registered at {time.time()}")
    
    return True

# Code Smell 8: Empty except block
def risky_operation():
    try:
        result = 10 / 0
        return result
    except:
        pass

# Code Smell 9: Multiple return statements in small function
def get_status_code(status):
    if status == 'success':
        return 200
    if status == 'created':
        return 201
    if status == 'bad_request':
        return 400
    if status == 'unauthorized':
        return 401
    if status == 'not_found':
        return 404
    return 500

# Code Smell 10: Mutable default argument
def add_item(item, items=[]):
    items.append(item)
    return items

# Code Smell 11: Too complex boolean expression
def check_eligibility(age, income, credit_score, employment_status, debt_ratio):
    return (age >= 18 and age <= 65 and income > 30000 and credit_score > 650 and 
            employment_status == 'employed' and debt_ratio < 0.4 or 
            age > 65 and income > 50000 and credit_score > 700)

# Code Smell 12: Dead code - unreachable statement
def unreachable_code_example():
    return True
    print("This will never execute")
    x = 10
    return x

