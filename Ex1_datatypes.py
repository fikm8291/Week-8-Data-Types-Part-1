# -------------------------------------------
# Exercise 1: Dictionaries & Data Structures
# -------------------------------------------
#
# GOAL:
# 1. Review data types: strings, integers, and lists.
# 2. Master Dictionaries: Storing data in KEY-VALUE pairs.
# 3. Practise the Collaborative Git Workflow: Pull -> Commit -> Push.
# 4. Practise the Pair Programming Workflow: Driver vs Navigator.
#
# CONCEPT:
# Dictionaries allow you to group related data together under one variable.
# Unlike a list which uses numbers (0, 1, 2), a dictionary uses "Keys".
#
# example_record = {"name": "Ammar", "role": "Trainee", "id": 101}
# 
# To access data: print(example_record["name"]) -> Output: Ammar
# To add data:    example_record["status"] = "Active"
#
# PAIR PROGRAMMING RULES:
# - The DRIVER types the code.
# - The NAVIGATOR reads the instructions and guides the driver.
# - You will SWITCH seats and computers after every task!
# -------------------------------------------


# -------------------------------------------
# Task 1: Building a Single Record
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Building a Single Record\n"
    + "-------------------------------------------")

# CONCEPT: Creating a dictionary from user input.
# To use a dictionary, use curly brackets {} and separate keys/values with colons.

# TODO:
# 1. Ask the user for three pieces of information: a Subject, a Priority (Low/High), and a Description.
# 2. Create a dictionary called 'log_entry' using these three inputs as values.
# 3. Use the keys: "subject", "priority", and "description".
# 4. Print the dictionary to the console.
# 5. Print a summary using an f-string: "Log Created: [SUBJECT] ([PRIORITY])"
#
# EXPECTED OUTPUT:
# Enter Subject: System Update
# Enter Priority: High
# Enter Description: Server restart required.
# Log Created: System Update (High)

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file (Ctrl+S or Cmd+S).
# 2. Open the terminal.
# 3. Run:
#    git add Ex1_datatypes.py
#    git commit -m "Completed Task 1"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 2: Managing Multiple Records (Logic)
# -------------------------------------------
# INSTRUCTION: You are now at a new computer. Get the latest code!
# 1. Open the terminal.
# 2. Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 2: Managing Multiple Records\n"
    + "-------------------------------------------")

# CONCEPT: To store many records, we put our dictionaries inside a LIST.
# all_records = [record1, record2]

# TODO:
# 1. Create an empty list called 'database'.
# 2. Add (append) your 'log_entry' dictionary from Task 1 into this list.
# 3. Use a 'while' loop to ask the user if they want to add another entry (y/n).
# 4. If 'y', repeat the inputs from Task 1, create a new dictionary, and append it to the list.
# 5. After the loop, print: "Total records in system: [COUNT]"
#
# HINT: Use len(database) to get the total count.

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex1_datatypes.py
#    git commit -m "Completed Task 2"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# Task 3: Data Retrieval (Loops)
# -------------------------------------------
# INSTRUCTION: Run: `git pull origin main`

print("\n-------------------------------------------\n"
    + "Task 3: Data Retrieval & Formatting\n"
    + "-------------------------------------------")

# TODO:
# 1. Print a header: "--- SYSTEM LOG VIEW ---"
# 2. Use a 'for' loop to iterate through your 'database' list.
# 3. For every record, print the details in a clean format:
#    "Subject: [Subject Value]"
#    "Priority: [Priority Value]"
#    "Details: [Description Value]"
#    (Add a dashed line between records for clarity).
#
# HINT: Inside the loop, access values using record["subject"]

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex1_datatypes.py
#    git commit -m "Completed Task 3"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: Input Validation Gatekeeper
# -------------------------------------------
# INSTRUCTION: Run `git pull origin main` first.

print("\n-------------------------------------------\n"
    + "Extension 1: Input Validation Gatekeeper\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a new input for an "Office Location".
# 2. Use an 'if' statement to check if the input is empty using len() or == "".
# 3. IF it is empty, print "ERROR: Location cannot be blank."
# 4. ELSE, print "Location [INPUT] accepted."
#
# HINT: Validation ensures your program doesn't save "blank" data.

# Write your code below:


# Extension 2: Search & Filter Logic
# -------------------------------------------
print("\n-------------------------------------------\n"
    + "Extension 2: Search & Filter Logic\n"
    + "-------------------------------------------")

# TODO:
# 1. Ask the user for a Subject to search for.
# 2. Create a variable 'found = False'.
# 3. Loop through the 'database' list.
# 4. IF the record's subject matches the search (use .lower() to be safe):
#    - Print the full record details.
#    - Set 'found = True'.
# 5. After the loop, if 'found' is still False, print "No matching records found."

# Write your code below:


# -------------------------------------------
# SAVING YOUR WORK
# -------------------------------------------
# 1. Save your file.
# 2. Run:
#    git add Ex1_datatypes.py
#    git commit -m "Completed extensions"
#    git push origin main
#
# *** STOP! ***
# SWITCH SEATS AND COMPUTERS NOW.
# -------------------------------------------


# -------------------------------------------
# ADVANCED ACTIVITY: Auto-Generated ID Numbers
# -------------------------------------------
# INSTRUCTION: Run `git pull origin main` first.

print("\n-------------------------------------------\n"
    + "ADVANCED ACTIVITY: Auto-Generated ID Numbers\n"
    + "-------------------------------------------")

# TODO:
# 1. Create a variable 'counter = 1001'.
# 2. Loop through your 'database' list.
# 3. Add a new key called "id" to each dictionary and set it to the value of 'counter'.
# 4. Increment the 'counter' by 1 after each record.
# 5. Print your records again, but this time include the ID in the output.

# Write your code below:


# -------------------------------------------
# FINAL SUBMISSION
# -------------------------------------------
# 1. Save this file.
# 2. Run:
#    git add Ex1_datatypes.py
#    git commit -m "Completed all activities"
#    git push origin main
# -------------------------------------------
