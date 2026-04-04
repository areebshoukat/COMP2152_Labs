# Lab 04: Loops and Functions Practice
# Student Name: Areeb Shoukat
# Date: Week 4

# ============================================
# Question 1: Robot Return to Origin
# ============================================

def robot_returns_to_origin(moves):
    x = 0
    y = 0

    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'L':
            x -= 1
        elif move == 'R':
            x += 1

    return x == 0 and y == 0


test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))


# ============================================
# Question 2: Two Sum
# ============================================

def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None


def two_sum_optimized(numbers, target):
    seen = {}

    for i in range(len(numbers)):
        needed = target - numbers[i]
        if needed in seen:
            return (seen[needed], i)
        seen[numbers[i]] = i

    return None


test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]

print("=== Part A: Brute Force (Nested Loops) ===")
for numbers, target in test_cases:
    print("Numbers:", numbers, "Target:", target)
    print("Result:", two_sum_brute_force(numbers, target))
    print()

print("=== Part B: Optimized (Dictionary) ===")
for numbers, target in test_cases:
    print("Numbers:", numbers, "Target:", target)
    print("Result:", two_sum_optimized(numbers, target))
    print()


# ============================================
# Question 3: Shuffle the Array
# ============================================

def shuffle_array(nums, n):
    first_half = nums[:n]
    second_half = nums[n:]

    result = []

    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])

    return result


test_cases = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

for nums, n in test_cases:
    print("Original:", nums)
    print("n =", n)
    print("First half:", nums[:n])
    print("Second half:", nums[n:])
    print("Shuffled:", shuffle_array(nums, n))
    print()


# ============================================
# Question 4: First Unique Character
# ============================================

def count_characters(s):
    counts = {}

    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    return counts


def first_unique_character(s):
    char_counts = count_characters(s)

    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i

    return -1


test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]

for s in test_strings:
    index = first_unique_character(s)

    if index != -1:
        print("First unique character in '" + s + "': index " + str(index) +
              " (character: '" + s[index] + "')")
    else:
        print("First unique character in '" + s + "': index -1 (no unique character)")

    print("  Character counts:", count_characters(s))
    print()
