# Lab 04: Loops and Functions Practice

## Learning Objectives
- **For loops**: Iterating over strings, lists, and ranges
- **Nested loops**: Using loops inside loops for pair comparisons
- **Functions**: Creating reusable code with `def`, parameters, and `return`
- **List slicing**: Extracting portions of lists with `[:n]` and `[n:]`
- **State tracking**: Using variables to track changes during iteration

---

## Question 1: Robot Return to Origin (Loops + State Tracking)

**LeetCode #657** | **Concepts:** `for` loop, conditionals (`if`/`elif`), state tracking with variables

### Problem Statement

A robot starts at position (0, 0) on a 2D grid. Given a sequence of moves, determine if the robot returns to the origin (0, 0) after completing all moves.

Move commands:
- `U` = Up (y + 1)
- `D` = Down (y - 1)
- `L` = Left (x - 1)
- `R` = Right (x + 1)

### Instructions

1. Create a **function** called `robot_returns_to_origin` that takes a `moves` string as a parameter
2. Inside the function:
   - Initialize `x = 0` and `y = 0`
   - Use a `for` loop to iterate through each character in the moves string
   - Use `if`/`elif` statements to update `x` or `y` based on the move
   - Return `True` if both `x == 0` and `y == 0`, otherwise return `False`
3. Test your function with the test cases below
4. Print the results in the format shown

### Starter Code

```python
# Question 1: Robot Return to Origin

def robot_returns_to_origin(moves):
    # Initialize starting position
    x = 0
    y = 0

    # TODO: Loop through each move and update x, y

    # TODO: Return True if back at origin, False otherwise
    pass

# Test cases
test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))
```

### Expected Output

```
Moves 'UD': Returns to origin? True
Moves 'LL': Returns to origin? False
Moves 'UDLR': Returns to origin? True
Moves 'LDRRLRUULR': Returns to origin? False
```

### Hints

1. Use `for move in moves:` to iterate through each character
2. Remember: `U` increases y, `D` decreases y, `R` increases x, `L` decreases x
3. After the loop ends, check if both x and y are zero

---

## Question 2: Two Sum (Nested Loops vs Dictionary)

**LeetCode #1** | **Concepts:** Nested `for` loops, dictionary lookup, `range()`, `len()`

### Problem Statement

Given a list of numbers and a target value, find two numbers that add up to the target. Return their indices (positions in the list).

### Instructions

**Part A: Brute Force (Nested Loops)**

1. Create a function called `two_sum_brute_force` that takes `numbers` (list) and `target` (int) as parameters
2. Use **nested for loops** to check every pair of numbers:
   - Outer loop: `for i in range(len(numbers)):`
   - Inner loop: `for j in range(i + 1, len(numbers)):`
3. If `numbers[i] + numbers[j] == target`, return the indices as a tuple `(i, j)`
4. If no pair found, return `None`

**Part B: Optimized (Dictionary)**

1. Create a function called `two_sum_optimized` that takes `numbers` (list) and `target` (int) as parameters
2. Use a dictionary to store numbers you've seen and their indices
3. For each number, calculate `needed = target - numbers[i]`
4. Check if `needed` exists in your dictionary
5. If found, return the indices; otherwise, add current number to dictionary

**Part C: Compare Both Approaches**

Test both functions with the same inputs and verify they return the same results.

### Starter Code

```python
# Question 2: Two Sum

# Part A: Brute Force with Nested Loops
def two_sum_brute_force(numbers, target):
    # TODO: Use nested loops to find the pair
    # Outer loop: i from 0 to len(numbers)
    # Inner loop: j from i+1 to len(numbers)
    pass

# Part B: Optimized with Dictionary
def two_sum_optimized(numbers, target):
    seen = {}  # Dictionary to store {number: index}
    # TODO: Loop through numbers, check if needed value exists in seen
    pass

# Test cases
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]

print("=== Part A: Brute Force (Nested Loops) ===")
for numbers, target in test_cases:
    result = two_sum_brute_force(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()

print("=== Part B: Optimized (Dictionary) ===")
for numbers, target in test_cases:
    result = two_sum_optimized(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()
```

### Expected Output

```
=== Part A: Brute Force (Nested Loops) ===
Numbers: [2, 7, 11, 15], Target: 9
Result: (0, 1)

Numbers: [3, 2, 4], Target: 6
Result: (1, 2)

Numbers: [3, 3], Target: 6
Result: (0, 1)

Numbers: [1, 5, 3, 8, 2], Target: 10
Result: (1, 3)

=== Part B: Optimized (Dictionary) ===
Numbers: [2, 7, 11, 15], Target: 9
Result: (0, 1)

Numbers: [3, 2, 4], Target: 6
Result: (1, 2)

Numbers: [3, 3], Target: 6
Result: (0, 1)

Numbers: [1, 5, 3, 8, 2], Target: 10
Result: (1, 3)
```

### Hints

**Part A (Nested Loops):**
- The inner loop starts at `i + 1` to avoid checking the same pair twice
- This approach checks every possible pair: O(n²) comparisons

**Part B (Dictionary):**
- If target is 9 and current number is 2, you need 7 (target - current)
- Store each number with its index: `seen[numbers[i]] = i`
- Dictionary lookup is fast: O(1) per check

### Why Two Approaches?

The nested loop approach is simpler to understand but slower for large lists. The dictionary approach is faster but requires understanding of dictionaries. Both give the same answer!

---

## Question 3: Shuffle the Array (List Slicing + Loops)

**LeetCode #1470** | **Concepts:** List slicing (`[:n]`, `[n:]`), `for` loop, `range()`, `append()`

### Problem Statement

Given an array of the form `[x1, x2, ..., xn, y1, y2, ..., yn]`, return the array in the form `[x1, y1, x2, y2, ..., xn, yn]`.

In other words, **interleave** the first half with the second half.

### Instructions

1. Create a function called `shuffle_array` that takes `nums` (list) and `n` (int) as parameters
2. Inside the function:
   - Use **slicing** to split the array into two halves:
     - `first_half = nums[:n]` (elements from index 0 to n-1)
     - `second_half = nums[n:]` (elements from index n to end)
   - Create an empty result list
   - Use a `for` loop with `range(n)` to interleave elements
   - Return the shuffled result
3. Test with multiple inputs and print intermediate steps

### Starter Code

```python
# Question 3: Shuffle the Array

def shuffle_array(nums, n):
    # Step 1: Split into two halves using slicing
    first_half = nums[:n]    # TODO: slice from start to n
    second_half = nums[n:]   # TODO: slice from n to end

    # Step 2: Create empty result list
    result = []

    # Step 3: Interleave using a for loop
    # TODO: Loop through range(n) and append alternating elements

    return result

# Test cases
test_cases = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

for nums, n in test_cases:
    print("Original: " + str(nums))
    print("n = " + str(n))

    # Show the slices
    print("First half (nums[:" + str(n) + "]): " + str(nums[:n]))
    print("Second half (nums[" + str(n) + ":]): " + str(nums[n:]))

    # Get result
    result = shuffle_array(nums, n)
    print("Shuffled: " + str(result))
    print()
```

### Expected Output

```
Original: [2, 5, 1, 3, 4, 7]
n = 3
First half (nums[:3]): [2, 5, 1]
Second half (nums[3:]): [3, 4, 7]
Shuffled: [2, 3, 5, 4, 1, 7]

Original: [1, 2, 3, 4, 4, 3, 2, 1]
n = 4
First half (nums[:4]): [1, 2, 3, 4]
Second half (nums[4:]): [4, 3, 2, 1]
Shuffled: [1, 4, 2, 3, 3, 2, 4, 1]

Original: [1, 1, 2, 2]
n = 2
First half (nums[:2]): [1, 1]
Second half (nums[2:]): [2, 2]
Shuffled: [1, 2, 1, 2]
```

### Hints

1. **Slicing reminder:**
   - `nums[:3]` = first 3 elements (index 0, 1, 2)
   - `nums[3:]` = everything from index 3 onwards

2. **Interleaving pattern:**
   ```
   i=0: append first_half[0], then second_half[0]
   i=1: append first_half[1], then second_half[1]
   i=2: append first_half[2], then second_half[2]
   ```

3. Inside your loop:
   ```python
   for i in range(n):
       result.append(first_half[i])
       result.append(second_half[i])
   ```

---

## Question 4: First Unique Character (Dictionary + Two-Pass Loop)

**LeetCode #387** | **Concepts:** Dictionary for counting, `for` loop, `range(len())`, two-pass algorithm

### Problem Statement

Given a string, find the **first character that does not repeat**. Return its index. If no unique character exists, return -1.

### Instructions

1. Create a **helper function** called `count_characters` that takes a string and returns a dictionary with character counts
2. Create a **main function** called `first_unique_character` that:
   - Calls `count_characters` to get the counts
   - Loops through the string to find the first character with count == 1
   - Returns the index of that character, or -1 if none found
3. Test with multiple strings

### Starter Code

```python
# Question 4: First Unique Character

# Helper function: Count all characters in a string
def count_characters(s):
    counts = {}
    # TODO: Loop through string and count each character
    # If character exists in counts, increment it
    # If not, set it to 1
    return counts

# Main function: Find first unique character
def first_unique_character(s):
    # Step 1: Get character counts using helper function
    char_counts = count_characters(s)

    # Step 2: Loop through string with index to find first unique
    # TODO: Use for i in range(len(s)) to check each character
    # Return i if char_counts[s[i]] == 1

    # Step 3: Return -1 if no unique character found
    return -1

# Test cases
test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]

for s in test_strings:
    index = first_unique_character(s)

    if index != -1:
        print("First unique character in '" + s + "': index " + str(index) + " (character: '" + s[index] + "')")
    else:
        print("First unique character in '" + s + "': index -1 (no unique character)")

    # Show the character counts for understanding
    counts = count_characters(s)
    print("  Character counts: " + str(counts))
    print()
```

### Expected Output

```
First unique character in 'leetcode': index 0 (character: 'l')
  Character counts: {'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}

First unique character in 'loveleetcode': index 2 (character: 'v')
  Character counts: {'l': 2, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1}

First unique character in 'aabb': index -1 (no unique character)
  Character counts: {'a': 2, 'b': 2}

First unique character in 'python': index 0 (character: 'p')
  Character counts: {'p': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1}

First unique character in 'aabbcc': index -1 (no unique character)
  Character counts: {'a': 2, 'b': 2, 'c': 2}
```

### Hints

**For count_characters function:**
```python
for char in s:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1
```

**For first_unique_character function:**
```python
for i in range(len(s)):
    if char_counts[s[i]] == 1:
        return i
```

### Why Use Two Functions?

Breaking the problem into two functions makes the code:
1. **Easier to read**: Each function has one clear job
2. **Easier to test**: You can test counting separately from finding
3. **Reusable**: The `count_characters` function could be used for other problems

---

## Submission Requirements

1. Create a single Python file named `lab04_solutions.py` containing all four questions
2. Each question should have clear comments separating it
3. Include all test cases provided and verify your output matches
4. Submit to D2L by the deadline

## File Structure

```python
# Lab 04: Loops and Functions Practice
# Student Name: [Your Name]
# Date: [Date]

# ============================================
# Question 1: Robot Return to Origin
# ============================================

def robot_returns_to_origin(moves):
    # Your code here
    pass

# Test cases for Q1...

# ============================================
# Question 2: Two Sum
# ============================================

def two_sum_brute_force(numbers, target):
    # Your code here
    pass

def two_sum_optimized(numbers, target):
    # Your code here
    pass

# Test cases for Q2...

# ============================================
# Question 3: Shuffle the Array
# ============================================

def shuffle_array(nums, n):
    # Your code here
    pass

# Test cases for Q3...

# ============================================
# Question 4: First Unique Character
# ============================================

def count_characters(s):
    # Your code here
    pass

def first_unique_character(s):
    # Your code here
    pass

# Test cases for Q4...
```

---

## Grading Rubric

| Question | Points | Concepts Tested |
|----------|--------|-----------------|
| Q1: Robot Return to Origin | 20 | `for` loop, `if`/`elif`, function with return |
| Q2: Two Sum (Both Parts) | 35 | Nested loops, dictionary, function design |
| Q3: Shuffle the Array | 20 | List slicing, `for` loop with `range()` |
| Q4: First Unique Character | 25 | Dictionary counting, helper functions, two-pass |
| **Total** | **100** | |

### Breakdown:
- **Q2 Part A (Nested Loops):** 15 points
- **Q2 Part B (Dictionary):** 20 points

---

## Tips for Success

### Loops
- `for item in collection:` — iterate directly over items
- `for i in range(n):` — iterate with index from 0 to n-1
- `for i in range(len(list)):` — iterate with index over a list

### Functions
- Always use `def function_name(parameters):` to define
- Use `return` to send back a value
- Call functions by name: `result = function_name(arguments)`

### Slicing
- `list[:n]` — first n elements
- `list[n:]` — from index n to end
- `list[start:end]` — from start to end-1

### Dictionaries for Counting
```python
counts = {}
for item in collection:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1
```

---

## Concept Summary

| Concept | Q1 | Q2 | Q3 | Q4 |
|---------|----|----|----|----|
| `for` loop | ✓ | ✓ | ✓ | ✓ |
| Nested loops | | ✓ | | |
| `if`/`elif`/`else` | ✓ | ✓ | | ✓ |
| Functions (`def`) | ✓ | ✓ | ✓ | ✓ |
| `return` statement | ✓ | ✓ | ✓ | ✓ |
| List slicing | | | ✓ | |
| Dictionary | | ✓ | | ✓ |
| `range()` | | ✓ | ✓ | ✓ |
| String iteration | ✓ | | | ✓ |