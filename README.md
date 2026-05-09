# 📧 Email Validation using Python

This project is a simple Python program that checks whether an email address is valid or not using basic string operations and conditions.

## 🚀 Features

- Checks minimum length of email (>= 6 characters)
- Ensures first character is an alphabet
- Validates presence of exactly one `@`
- Checks proper placement of `.`
- Allows only valid characters (letters, digits, `@`, `.`, `_`)
- Detects spaces in email
- Detects invalid characters

## 🧠 Logic Used

The program uses multiple nested conditions:

1. Length validation
2. First character check
3. `@` symbol validation (must be exactly one)
4. Dot (`.`) position check near domain
5. Character-wise validation loop:
   - No spaces allowed
   - Only allowed symbols: `@ . _`
   - Digits and alphabets allowed
   - Any other character is invalid

## 💻 How It Works

### Step-by-step flow:

1. User enters email
2. Program checks basic rules
3. If valid structure exists, it scans each character
4. Flags are used to detect:
   - Spaces
   - Invalid characters
5. Final decision is printed:
   - ✅ Right Email Address  
   - ❌ Wrong Email Address (1–5 reasons)

## 📌 Example

### Input: test_email@gmail.com
### Output: Right Email Address

### Input: test email@gmail.com
### Output: Wrong Email Address 5

## 🛠️ Technologies Used

- Python 3
- String methods
- Conditional statements
- Loops

## 📚 Learning Purpose

This project helps beginners understand:

- String validation
- Nested if-else conditions
- Looping through strings
- Logical operators
- Basic email validation rules

## ⚠️ Note

This is a **basic email validation project**, not a professional regex-based validator. It is created for learning purposes only.

## 🚀 Future Improvements

- Regex-based validation
- GUI version using Tkinter
- Better error messages
- Domain validation system

## 👨‍💻 Author

Developed by: Zoya Sarwa 
This project is built by me for learning Python basics, especially string handling and conditional logic.
