# Username Registration System

## Overview
This is a simple Python-based username registration system that demonstrates the use of tuples (immutable data) and sets (fast lookup). It allows users to register usernames while ensuring uniqueness and validity.

---

## Features
- Register a new user
- Prevent duplicate usernames
- Validate username format
- View all registered users
- Menu-driven interface

---

## Concepts Used
- Tuples (immutable data storage)
- Sets (O(1) lookup for fast checking)
- Functions
- Input handling
- Loop-based menu system

---

## Username Rules
- Must be at least 4 characters long
- Must contain only letters and numbers (no special characters)
- Must be unique (no duplicates allowed)

---

## How It Works
1. The system starts with a predefined tuple of users.
2. A set is created from the tuple for fast lookup.
3. When a new user is registered:
   - Input is converted to lowercase
   - Checked against the set for duplicates
   - Validated for length and format
   - If valid, added to tuple and set
4. Users can view all registered usernames.

---

## Code Structure

- `register(users, user_set)`
  - Handles user registration
  - Returns updated tuple and set

- `view(users)`
  - Displays all users

- Main loop
  - Menu-driven interface

---

## Example Usage

1. Run the program
2. Choose option:
   - 1 → Register user
   - 2 → View users
   - 3 → Exit
3. Enter username when prompted

---

## Sample Output

Enter choice: 1  
Enter username: rahul  
Registered successfully  

Enter choice: 2  
Registered Users:  
- aditya  
- rohan  
- kunal  
- rahul  

---

## Future Improvements
- Add login system
- Add password support
- Store data in file (JSON or database)
- Add username suggestions
- Implement GUI

---

## Learning Outcome
This project helps understand:
- Difference between mutable and immutable data types
- Efficient data lookup using sets
- Clean function-based design
- Basic system design thinking

---
