"""
Security Vulnerabilities Test File
This file contains intentional security vulnerabilities for SonarQube testing.
"""

import os
import pickle
import hashlib
import subprocess
import random
from flask import request

# Vulnerability 1: Hardcoded credentials
DATABASE_PASSWORD = "admin123"
API_KEY = "sk_live_12345678910abcdefgh"

# Vulnerability 2: Weak cryptographic hash (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Vulnerability 3: SQL Injection vulnerability
def get_user_by_email(email):
    import sqlite3
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Vulnerable to SQL injection
    query = "SELECT * FROM users WHERE email = '" + email + "'"
    cursor.execute(query)
    return cursor.fetchone()

# Vulnerability 4: Command Injection
def ping_host(hostname):
    # Vulnerable to command injection
    command = "ping -c 1 " + hostname
    os.system(command)

# Vulnerability 5: Insecure deserialization
def load_user_data(serialized_data):
    # Unsafe pickle usage
    return pickle.loads(serialized_data)

# Vulnerability 6: Path traversal vulnerability
def read_file(filename):
    # No validation of filename
    with open('/var/data/' + filename, 'r') as f:
        return f.read()

# Vulnerability 7: Weak random number generation for security
def generate_session_token():
    # Using random instead of secrets for security-critical operation
    return str(random.randint(1000000, 9999999))

# Vulnerability 8: XSS vulnerability (no output encoding)
def render_user_comment(comment):
    # Directly rendering user input without escaping
    html = "<div class='comment'>" + comment + "</div>"
    return html

# Vulnerability 9: Insecure SSL/TLS configuration
def make_api_request():
    import requests
    # Disabling SSL verification
    response = requests.get('https://api.example.com/data', verify=False)
    return response.json()

# Vulnerability 10: Open redirect vulnerability
def redirect_user(url):
    from flask import redirect
    # No validation of redirect URL
    return redirect(url)

# Vulnerability 11: Use of eval() with user input
def calculate_expression(expr):
    # Dangerous use of eval
    return eval(expr)

# Vulnerability 12: Weak cipher mode
def encrypt_data(data, key):
    from Crypto.Cipher import DES
    # DES is weak and deprecated
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(data)

