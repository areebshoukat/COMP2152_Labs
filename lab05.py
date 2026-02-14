# Lab 05: Recursion & Functions
# Student Name: Areeb Shoukat

# ============================================
# Question 1: Fibonacci (Recursion)
# ============================================

def fib(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursive case
    return fib(n - 1) + fib(n - 2)

print("=== Question 1: Fibonacci (0 to 10) ===")
for i in range(0, 11):
    print("fib(" + str(i) + ") = " + str(fib(i)))
print()


# ============================================
# Question 2: FizzBuzz (Functions + Loops)
# ============================================

def fizz_buzz(n):
    result = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))

    return result

print("=== Question 2: FizzBuzz ===")
print("n = 3  ->", fizz_buzz(3))
print("n = 5  ->", fizz_buzz(5))
print("n = 15 ->", fizz_buzz(15))
print()


# ============================================
# Question 3: Binary Search (Iterative + Recursive)
# ============================================

def binary_search_iterative(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def binary_search_recursive(nums, target, left, right):
    # Base case
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid
    elif target < nums[mid]:
        return binary_search_recursive(nums, target, left, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, right)

print("=== Question 3: Binary Search ===")
test_cases = [
    ([-1, 0, 3, 5, 9, 12], 9),
    ([-1, 0, 3, 5, 9, 12], 2),
    ([1], 1),
    ([1, 2, 3, 4, 5], 1),
    ([1, 2, 3, 4, 5], 5)
]

for nums, target in test_cases:
    it_result = binary_search_iterative(nums, target)
    rec_result = binary_search_recursive(nums, target, 0, len(nums) - 1)

    print("Nums:", nums, "Target:", target)
    print("  Iterative result:", it_result)
    print("  Recursive result:", rec_result)
    print()
