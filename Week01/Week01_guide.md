# Week 01 Lab Guide - Complete Step-by-Step Tutorial

## What is This Lab About?

Welcome to your first programming lab! In this lab, you will:
1. Learn basic Python coding concepts
2. Create a GitHub account (a place to store your code online)
3. Write Python code to answer questions
4. Submit your work

Don't worry if you're new to programming - we'll explain everything in simple terms!

---

## Part 1: The Coding Questions

Below are the sample coding questions you need to solve. Let's go through each one step by step.

---

### Question 1: Adding Comments

**What is a comment?**
A comment is a note in your code that the computer ignores. It's like a sticky note for yourself or other programmers. In Python, we use the `#` symbol to write comments.

**Task:**
- Add a comment that says "Sample Coding Questions 01 Week 01"
- Add another comment with your first and last name

**Solution:**
```python
# Sample Coding Questions 01 Week 01
# John Smith
```

**Explanation:**
- The `#` symbol tells Python: "Don't run this line, it's just a note"
- Replace "John Smith" with YOUR actual name
- Comments help others (and future you!) understand your code

---

### Question 2: Defining Variables (Arrays/Lists)

**What is a variable?**
A variable is like a labeled box where you store information. For example, `age = 25` creates a box labeled "age" containing the number 25.

**What is an array (list)?**
An array (called a "list" in Python) is a variable that can hold multiple values at once. Think of it like a shopping list that holds many items.

**Task:**
Define an array variable with the elements: 1, 4, 7, 9

**Solution:**
```python
# Question 2: Defining an array (list)
my_array = [1, 4, 7, 9]
```

**Explanation:**
- `my_array` is the name of our variable (you can name it anything)
- Square brackets `[ ]` tell Python this is a list
- The numbers are separated by commas
- You can also call it `numbers = [1, 4, 7, 9]` or any other name you like

---

### Question 3: Order of Operations (Fully-Bracketed Version)

**What is order of operations?**
Just like in math class (PEMDAS/BEDMAS), Python follows a specific order when calculating:
1. `**` (exponents/powers) - FIRST
2. `*`, `/`, `//`, `%` (multiply, divide, floor divide, modulo) - SECOND
3. `+`, `-` (add, subtract) - THIRD

**What do these symbols mean?**
- `**` = power/exponent (example: `2 ** 3` means 2³ = 8)
- `//` = floor division (divides and rounds DOWN to whole number)
- `%` = modulo (gives the remainder after division)

**Task:**
Given variables a=1, b=2, c=3, d=4, write the fully-bracketed version of:
```
e = a - b ** c // d + a % c
```

**Solution:**
```python
# Question 3: Order of Operations
a = 1
b = 2
c = 3
d = 4

# Original expression:
# e = a - b ** c // d + a % c

# Fully-Bracketed Version:
e = (a - ((b ** c) // d)) + (a % c)
```

**Step-by-step explanation:**

Let's break it down following the order of operations:

1. **First, handle `**` (exponents):**
   - `b ** c` becomes `(b ** c)` → This is 2³ = 8

2. **Next, handle `//` and `%` (left to right):**
   - `(b ** c) // d` becomes `((b ** c) // d)` → This is 8 // 4 = 2
   - `a % c` becomes `(a % c)` → This is 1 % 3 = 1

3. **Finally, handle `-` and `+` (left to right):**
   - `a - ((b ** c) // d)` becomes `(a - ((b ** c) // d))` → This is 1 - 2 = -1
   - Then add `(a % c)` → This is -1 + 1 = 0

**Final answer:** `e = (a - ((b ** c) // d)) + (a % c)`

The result of `e` is `0`.

---

### Question 4: String Formatting

**What is string formatting?**
String formatting lets you insert variables into text and control how they appear (like adding decimal places to numbers).

**Task:**
Create a variable called "temperature" with the value 32.6. Print the sentence:
"The temperature today is: 32.600 degrees Celsius"
Use the format function and show exactly 3 decimal places (don't just type "32.600" manually).

**Solution:**
```python
# Question 4: Formatting
temperature = 32.6

print("The temperature today is: {:.3f} degrees Celsius".format(temperature))
```

**Explanation:**
- `temperature = 32.6` creates a variable storing the number
- `{:.3f}` is a placeholder that means:
  - `{}` = "put a value here"
  - `:.3f` = "show 3 decimal places" (f stands for "float" which means decimal number)
- `.format(temperature)` tells Python to put the temperature value in the placeholder
- The output will show `32.600` (the extra zeros are added automatically)

**Alternative solution using f-strings (modern Python):**
```python
temperature = 32.6
print(f"The temperature today is: {temperature:.3f} degrees Celsius")
```

---

### Question 5: User Input

**What is user input?**
User input lets your program ask questions and wait for someone to type an answer.

**Task:**
- Ask the user to input their age
- Save the input into a variable called "userAge"
- Add 22 to the user's input
- Print: "Now showing the shop items filtered by age: [result]"

**Solution:**
```python
# Question 5: Common Functions - User Input
userAge = int(input("Enter your age: "))
userAge = userAge + 22

print("Now showing the shop items filtered by age:", userAge)
```

**Explanation:**
- `input("Enter your age: ")` shows a message and waits for the user to type something
- `int(...)` converts what the user typed from text to a whole number
  - Why? Because `input()` always gives us text, and we can't do math with text!
- `userAge + 22` adds 22 to whatever age they entered
- `print()` displays the final message with the calculated age

**Example:** If the user types `0`, then `userAge` becomes `0 + 22 = 22`, and it prints:
"Now showing the shop items filtered by age: 22"

---

## Part 2: Complete Code File (lab1.py)

Here is what your final `lab1.py` file should look like with all questions answered:

```python
# Sample Coding Questions 01 Week 01
# [Your First Name] [Your Last Name]

# Question 2: Defining an array (list)
my_array = [1, 4, 7, 9]

# Question 3: Order of Operations
a = 1
b = 2
c = 3
d = 4

# Fully-Bracketed Version of: e = a - b ** c // d + a % c
e = (a - ((b ** c) // d)) + (a % c)
print("Question 3 result:", e)

# Question 4: Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius".format(temperature))

# Question 5: User Input
userAge = int(input("Enter your age: "))
userAge = userAge + 22
print("Now showing the shop items filtered by age:", userAge)
```

---

## Part 3: Setting Up GitHub

### What is GitHub?
GitHub is a website where programmers store and share their code online. Think of it like Google Drive, but specifically for code!

### Step 1: Create a GitHub Account

1. Go to [github.com](https://github.com)
2. Click the **"Sign up"** button in the top right corner
3. Enter your email address
4. Create a password (make it strong!)
5. Choose a username (pick something professional - others will see it)
6. Complete the verification puzzle
7. Check your email and click the verification link

**Already have an account?** Just sign in!

---

### Step 2: Create a New Repository

A **repository** (or "repo") is like a folder that holds your project files on GitHub.

1. After logging in, click the **"+"** icon in the top right corner
2. Select **"New repository"**
3. Fill in the details:
   - **Repository name**: `Lab1`
   - **Description**: "My first lab assignment" (optional)
   - **Visibility**: Choose **Public** (so your instructor can see it)
   - Check **"Add a README file"** (optional but helpful)
4. Click **"Create repository"**

---

## Part 4: Upload Your Code to GitHub

### Easy Method: Drag and Drop

1. Open your GitHub repository in your web browser
2. Find your `lab1.py` file on your computer
3. **Drag and drop** the file directly onto the GitHub page
4. You will see a message saying "Upload files"
5. Scroll down and click the green **"Commit changes"** button
6. Done! Your file is now on GitHub!

---

## Part 5: Take a Screenshot (gitproof.png)

You need proof that you uploaded your file to GitHub.

### What to capture in your screenshot:
- Your GitHub repository page
- The `lab1.py` file visible in the file list
- Your GitHub username visible on the page

### How to take a screenshot:

**On Windows:**
1. Press `Windows + Shift + S`
2. Select the area you want to capture
3. Open Paint
4. Paste (Ctrl+V)
5. Save as `gitproof.png`

**On Mac:**
1. Press `Cmd + Shift + 4`
2. Select the area you want to capture
3. Find the screenshot on your Desktop
4. Rename it to `gitproof.png`

---

## Part 6: Create the Zip File (lab1submit.zip)

You need to put both files together in a zip file for submission.

### Files you need:
1. `lab1.py` - your Python code
2. `gitproof.png` - your screenshot

### How to create a zip file:

**On Windows:**
1. Put both files in the same folder
2. Select both files (hold Ctrl and click each file)
3. Right-click on the selected files
4. Choose **"Compress to ZIP file"** or **"Send to" > "Compressed (zipped) folder"**
5. Rename the zip file to `lab1submit.zip`

**On Mac:**
1. Put both files in the same folder
2. Select both files (hold Cmd and click each file)
3. Right-click (or Control-click) on the selected files
4. Choose **"Compress 2 Items"**
5. Rename the zip file to `lab1submit.zip`

---

## Part 7: Submit on D2L

1. Log in to your D2L account
2. Go to your course
3. Navigate to **Week 01** > **Lab** > **Submission**
4. Click **"Submit"** or **"Add a File"**
5. Upload your `lab1submit.zip` file
6. Click **"Submit"** to finish

---

## Final Checklist

Before submitting, make sure you have:

- [ ] Created a GitHub account
- [ ] Written your code in `lab1.py` with all 5 questions answered
- [ ] Replaced "[Your First Name] [Your Last Name]" with your actual name
- [ ] Uploaded `lab1.py` to your GitHub repository
- [ ] Taken a screenshot named `gitproof.png`
- [ ] Created a zip file named `lab1submit.zip` containing:
  - [ ] `lab1.py`
  - [ ] `gitproof.png`
- [ ] Submitted `lab1submit.zip` on D2L

---

## Common Mistakes to Avoid

1. **Wrong file names**: Files MUST be named exactly `lab1.py`, `gitproof.png`, and `lab1submit.zip`
2. **Forgetting to save**: Always save your Python file before uploading
3. **Screenshot missing info**: Make sure your username AND the uploaded file are visible
4. **Empty zip file**: Double-check that both files are inside the zip
5. **Forgetting int() with input()**: Remember to convert user input to a number with `int()`
6. **Hardcoding values**: Don't type "32.600" manually - use formatting!

---

## Quick Reference: Python Basics

| Concept | Example | What it does |
|---------|---------|--------------|
| Comment | `# This is a comment` | Note that Python ignores |
| Variable | `x = 5` | Stores the value 5 |
| List/Array | `nums = [1, 2, 3]` | Stores multiple values |
| Print | `print("Hello")` | Shows text on screen |
| Input | `input("Question: ")` | Asks user for input |
| Format | `"{:.2f}".format(3.1)` | Shows "3.10" |
| Power | `2 ** 3` | 2 to the power of 3 = 8 |
| Floor divide | `7 // 2` | Divides and rounds down = 3 |
| Modulo | `7 % 2` | Remainder of division = 1 |

---

## Need Help?

- **GitHub Help**: [docs.github.com](https://docs.github.com)
- **Python Help**: [python.org/doc](https://www.python.org/doc/)
- Ask your instructor or TA during lab hours!

---

Good luck with your first lab! You've got this!
