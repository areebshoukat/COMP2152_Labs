# Week 02 Lab - Rock, Paper, Scissors Game

## Objective
Create a simple Rock, Paper, Scissors game using arrays, user input, and conditional statements.

---

## Instructions

### Step 1: Define the Choices Array
Define a new array called `choices` and add 3 game options: Rock, Paper, Scissors.

### Step 2: Get Player Input
Ask the player to enter their choice using the `input()` function.
Save the input in a variable called `playerChoice`.
The input should be a number (1=Rock, 2=Paper, 3=Scissors).

### Step 3: Convert to Integer
Convert `playerChoice` to an integer data type using `int()`.

### Step 4: Error Handling
Add error handling using conditional if statements.
Check that `playerChoice` is within the valid range (1-3).
If not valid, print out "Error: Choice must be between 1 and 3."

### Step 5: Get Computer's Choice
Ask for the computer's choice (simulated input for now).
Save it in a variable called `computerChoice`.
Convert it to an integer and validate the range (1-3).

### Step 6: Array Indexing
Use `playerChoice` and `computerChoice` as indices into the `choices` array.
Remember: Arrays are 0-indexed, so subtract 1 from the choice.
Print out both the player's and computer's choice names.

### Step 7: Determine the Winner
Define the following conditions using if/elif/else:
- If both choices are equal, print out "It's a tie!"
- If player chose Rock (1) and computer chose Scissors (3), print out "Rock beats Scissors - You win!"
- If player chose Paper (2) and computer chose Rock (1), print out "Paper beats Rock - You win!"
- If player chose Scissors (3) and computer chose Paper (2), print out "Scissors beats Paper - You win!"
- Else, print out "You lose!"

### Step 8: String Comparison
If the player's choice is not "Rock", print out "You didn't pick the classic Rock..."

---

## Expected Output Example

```
Enter your choice (1=Rock, 2=Paper, 3=Scissors): 2
Enter computer's choice (1-3): 1
You chose: Paper
Computer chose: Rock
Paper beats Rock - You win!
You didn't pick the classic Rock...
```

---

## Summary of Techniques Used

| Technique | Description |
|-----------|-------------|
| Arrays | Store multiple values in a list |
| User Input | Get data from user with `input()` |
| Type Conversion | Convert string to integer with `int()` |
| Error Handling | Validate input with if statements |
| Array Indexing | Access array elements by index |
| Conditionals | if/elif/else for game logic |
| String Comparison | Compare strings with `!=` |

---

## Optional Enhancements
- Optional: Add a scoring system to track wins and losses.
- Optional: Use a loop to play multiple rounds.
- Optional: Generate a random computer choice using the `random` module.

Note: It is too early to use try-except-finally blocks. Use simple if statements for error handling. If you use try-except-finally blocks, no marks will be deducted.
