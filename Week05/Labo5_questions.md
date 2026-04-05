# Week 05 Lab: Recursion & Functions

## Learning Objectives
- **Recursion**: Understanding base case and recursive case
- **Function Design**: Creating reusable functions with parameters and return values
- **Divide & Conquer**: Breaking problems into smaller subproblems

---

## Question 1: Fibonacci Number (LeetCode #509)

**Difficulty:** Easy | **Concepts:** Recursion, base cases, recursive case

### Problem Statement

The **Fibonacci numbers**, commonly denoted `F(n)`, form a sequence where each number is the sum of the two preceding ones, starting from 0 and 1.

```
F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1
```

Given `n`, calculate `F(n)`.

### Examples

```
Input: n = 0
Output: 0

Input: n = 1
Output: 1

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3

Input: n = 10
Output: 55
```

### Instructions

1. Create a function called `fib` that takes an integer `n` as a parameter
2. Implement **two base cases**:
   - If `n == 0`, return `0`
   - If `n == 1`, return `1`
3. Implement the **recursive case**:
   - Return `fib(n - 1) + fib(n - 2)`
4. Test your function with values from 0 to 10

### Hints

1. Every recursive function needs base case(s) to stop the recursion
2. The recursive case must move toward the base case (n gets smaller each call)
3. This is the classic example from your Week 6 Recursion lecture!

### Visual: Call Stack for fib(4)

```
fib(4)
├── fib(3)
│   ├── fib(2)
│   │   ├── fib(1) → returns 1
│   │   └── fib(0) → returns 0
│   │   → returns 1
│   └── fib(1) → returns 1
│   → returns 2
└── fib(2)
    ├── fib(1) → returns 1
    └── fib(0) → returns 0
    → returns 1
→ returns 3
```

---

## Question 2: FizzBuzz (LeetCode #412)

**Difficulty:** Easy | **Concepts:** Functions, conditionals, list building

### Problem Statement

Given an integer `n`, return a list of strings where for each number from 1 to n:

- If the number is divisible by 3, the string is `"Fizz"`
- If the number is divisible by 5, the string is `"Buzz"`
- If the number is divisible by both 3 and 5, the string is `"FizzBuzz"`
- Otherwise, the string is the number itself (as a string)

### Examples

```
Input: n = 3
Output: ["1", "2", "Fizz"]

Input: n = 5
Output: ["1", "2", "Fizz", "4", "Buzz"]

Input: n = 15
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
         "11", "Fizz", "13", "14", "FizzBuzz"]
```

### Instructions

1. Create a function called `fizz_buzz` that takes an integer `n` as a parameter
2. Create an empty result list
3. Loop from 1 to n (inclusive)
4. For each number, check the conditions **in the right order**:
   - Check divisible by BOTH 3 and 5 first (otherwise you'll never hit this case!)
   - Then check divisible by 3
   - Then check divisible by 5
   - Otherwise, convert the number to a string
5. Append the appropriate string to the result list
6. Return the result list

### Hints

1. Use `%` (modulo) to check divisibility: `n % 3 == 0` means divisible by 3
2. Check "FizzBuzz" (divisible by both) BEFORE checking "Fizz" or "Buzz" individually
3. Convert number to string: `str(i)`
4. This is a classic programming interview question!

### Why Order Matters

```python
# WRONG ORDER - will never print FizzBuzz!
if i % 3 == 0:
    print("Fizz")
elif i % 5 == 0:
    print("Buzz")
elif i % 3 == 0 and i % 5 == 0:  # Never reached!
    print("FizzBuzz")

# CORRECT ORDER
if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
elif i % 3 == 0:
    print("Fizz")
elif i % 5 == 0:
    print("Buzz")
```

---

## Question 3: Binary Search (LeetCode #704)

**Difficulty:** Easy | **Concepts:** Divide & Conquer, Recursion OR Iteration

### Problem Statement

Given a **sorted** array of integers `nums` and an integer `target`, write a function to search for `target` in `nums`.

- If `target` exists, return its index
- If `target` does not exist, return `-1`

You must write an algorithm with **O(log n)** runtime complexity.

### Examples

```
Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
Output: -1
Explanation: 2 does not exist in nums

Input: nums = [1], target = 1
Output: 0

Input: nums = [1, 2, 3, 4, 5], target = 1
Output: 0

Input: nums = [1, 2, 3, 4, 5], target = 5
Output: 4
```

### Instructions

Implement **BOTH** approaches:

**Part A: Iterative (while loop)**

1. Create a function `binary_search_iterative(nums, target)`
2. Set `left = 0` and `right = len(nums) - 1`
3. While `left <= right`:
   - Calculate `mid = (left + right) // 2`
   - If `nums[mid] == target`, return `mid`
   - If `target < nums[mid]`, search left half: `right = mid - 1`
   - If `target > nums[mid]`, search right half: `left = mid + 1`
4. Return `-1` if not found

**Part B: Recursive**

1. Create a function `binary_search_recursive(nums, target, left, right)`
2. Base case: If `left > right`, return `-1`
3. Calculate `mid = (left + right) // 2`
4. If `nums[mid] == target`, return `mid`
5. If `target < nums[mid]`, recurse on left half
6. If `target > nums[mid]`, recurse on right half

### Hints

1. The array MUST be sorted for binary search to work
2. Each step eliminates half of the remaining elements
3. This is from **Chapter 1 of Grokking Algorithms**!
4. Time complexity: O(log n) - for 1 billion elements, only ~30 comparisons needed!

### Visual: Binary Search for target = 9

```
Array: [-1, 0, 3, 5, 9, 12]
        0   1  2  3  4   5

Step 1: left=0, right=5, mid=2
        nums[2] = 3 < 9, search right half

Step 2: left=3, right=5, mid=4
        nums[4] = 9 == 9, FOUND! Return 4
```

---

## Grading Rubric

| Question | Points | Concepts Tested |
|----------|--------|-----------------|
| Q1: Fibonacci | 30 | Recursion, base case, recursive case |
| Q2: FizzBuzz | 30 | Functions, conditionals, loops, list building |
| Q3: Binary Search | 40 | Divide & conquer, both iterative and recursive |
| **Total** | **100** | |

### Q3 Breakdown:
- Part A (Iterative): 20 points
- Part B (Recursive): 20 points

---

## Connection to Course Materials

| Question | Connection |
|----------|------------|
| Fibonacci | Week 6 Recursion lecture - exact example! |
| FizzBuzz | Week 4 Functions + Conditionals |
| Binary Search | Grokking Algorithms Chapter 1, Week 6 Recursion |

---

## Tips for Success

1. **Fibonacci**: Draw the call stack to understand how recursion works
2. **FizzBuzz**: Check the "both" condition FIRST
3. **Binary Search**: Remember the array must be sorted!
4. **Test edge cases**: n=0, n=1, empty arrays, target not found