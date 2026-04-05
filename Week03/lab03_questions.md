# Lab 03: Python Collections Practice

## Learning Objectives
- Lists: searching, concatenation, removal, sorting
- Tuples: creation, immutability, unpacking
- Sets: operations (union, intersection, difference), uniqueness
- Dictionaries: key-value pairs, accessing, modifying, iterating

---

## Question 1: Student Grades List (Lists - Basic Operations)

**Concepts:** List creation, `append()`, `sort()`, `len()`, indexing

Create a program that manages student grades:

1. Create a list called `grades` with these initial values: `[85, 92, 78, 95, 88]`
2. Use `append()` to add a new grade of `90` to the list
3. Use `sort()` to sort the grades in ascending order
4. Print the sorted list
5. Print the highest grade (last element using negative indexing)
6. Print the lowest grade (first element)
7. Print the total number of grades using `len()`

**Expected Output:**
```
Sorted grades: [78, 85, 88, 90, 92, 95]
Highest grade: 95
Lowest grade: 78
Total number of grades: 6
```

---

test

---

test

---

## Question 2: Shopping Cart (Lists - Searching and Removal)

**Concepts:** `index()`, `count()`, `remove()`, `pop()`, `in` keyword

Create a shopping cart program:

1. Create a list called `cart` with these items: `["apple", "banana", "milk", "bread", "apple", "eggs"]`
2. Use `count()` to find how many times "apple" appears in the cart
3. Use `index()` to find the position of "milk" in the cart
4. Use `remove()` to remove one "apple" from the cart
5. Use `pop()` to remove and print the last item from the cart
6. Check if "banana" is `in` the cart and print the result
7. Print the final cart

**Expected Output:**
```
Number of apples: 2
Position of milk: 2
Removed item using pop: eggs
Is banana in cart? True
Final cart: ['banana', 'milk', 'bread', 'apple']
```

---

## Question 3: Coordinate System (Tuples - Creation and Unpacking)

**Concepts:** Tuple creation, indexing, unpacking, `tuple()` constructor, immutability

Create a program that works with coordinate points:

1. Create a tuple called `point1` with values `(3, 5)`
2. Create a tuple called `point2` with values `(7, 2)`
3. Unpack `point1` into variables `x1` and `y1`
4. Unpack `point2` into variables `x2` and `y2`
5. Calculate the distance between points using the formula: `((x2-x1)**2 + (y2-y1)**2)**0.5`
6. Create a tuple from the string `"PYTHON"` using the `tuple()` constructor
7. Print each character from the tuple using a `for` loop

**Expected Output:**
```
Point 1: (3, 5)
Point 2: (7, 2)
x1 = 3, y1 = 5
x2 = 7, y2 = 2
Distance between points: 5.0
Characters tuple: ('P', 'Y', 'T', 'H', 'O', 'N')
P
Y
T
H
O
N
```

---

## Question 4: Class Attendance (Sets - Uniqueness and Operations)

**Concepts:** Set creation, `add()`, `remove()`, union (`|`), intersection (`&`), difference (`-`)

Create a program to track class attendance:

1. Create a set called `monday_class` with students: `{"Alice", "Bob", "Charlie", "Diana"}`
2. Create a set called `wednesday_class` with students: `{"Bob", "Diana", "Eve", "Frank"}`
3. Use `add()` to add "Grace" to `monday_class`
4. Find students who attended **both** classes using intersection (`&`)
5. Find students who attended **either** class using union (`|`)
6. Find students who attended **only Monday** using difference (`-`)
7. Find students who attended **only one class** (not both) using symmetric difference (`^`)
8. Check if `monday_class` is a subset of the union using `<=`

**Expected Output:**
```
Monday class: {'Alice', 'Bob', 'Charlie', 'Diana', 'Grace'}
Wednesday class: {'Bob', 'Diana', 'Eve', 'Frank'}
Attended both classes: {'Bob', 'Diana'}
Attended either class: {'Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace'}
Only Monday: {'Alice', 'Charlie', 'Grace'}
Only one class (not both): {'Alice', 'Charlie', 'Eve', 'Frank', 'Grace'}
Is Monday subset of all students? True
```

---

## Question 5: Contact Book (Dictionaries - Basic Operations)

**Concepts:** Dictionary creation, accessing values, adding/modifying entries, `del`, `keys()`, `values()`

Create a simple contact book:

1. Create a dictionary called `contacts` with:
   - "Alice": "555-1234"
   - "Bob": "555-5678"
   - "Charlie": "555-9999"
2. Print Alice's phone number by accessing the dictionary
3. Add a new contact: "Diana" with number "555-4321"
4. Update Bob's number to "555-0000"
5. Delete Charlie's contact using `del`
6. Print all contact names using `keys()`
7. Print all phone numbers using `values()`
8. Print the total number of contacts

**Expected Output:**
```
Alice's number: 555-1234
Contacts after adding Diana: {'Alice': '555-1234', 'Bob': '555-5678', 'Charlie': '555-9999', 'Diana': '555-4321'}
Contacts after updating Bob: {'Alice': '555-1234', 'Bob': '555-0000', 'Charlie': '555-9999', 'Diana': '555-4321'}
Contacts after deleting Charlie: {'Alice': '555-1234', 'Bob': '555-0000', 'Diana': '555-4321'}
All names: dict_keys(['Alice', 'Bob', 'Diana'])
All numbers: dict_values(['555-1234', '555-0000', '555-4321'])
Total contacts: 3
```

---

## Question 6: Inventory Management System (Combined - All Collections)

**Concepts:** Lists, Tuples, Sets, Dictionaries working together

Create an inventory management system for a small store:

1. **Products Dictionary:** Create a dictionary called `inventory` with product names as keys and tuples of (price, quantity) as values:
   - "Laptop": (999.99, 5)
   - "Mouse": (29.99, 15)
   - "Keyboard": (79.99, 10)
   - "Monitor": (299.99, 8)

2. **Print Inventory:** Use a `for` loop with `.items()` to print each product with its price and quantity

3. **Categories Set:** Create two sets:
   - `electronics` = {"Laptop", "Monitor"}
   - `accessories` = {"Mouse", "Keyboard"}

4. **Find all products:** Use union to combine both category sets

5. **Price List:** Create a list of all prices from the inventory (extract from tuples)

6. **Sort Prices:** Sort the price list and print lowest and highest prices

7. **Add New Product:** Add "Headphones": (49.99, 20) to the inventory

8. **Update Quantity:** Update "Mouse" quantity to 12 (keep same price)

9. **Remove Product:** Remove "Monitor" from inventory using `del`

10. **Final Report:** Print the final inventory with formatted output

**Expected Output:**
```
=== Current Inventory ===
Laptop - Price: $999.99, Quantity: 5
Mouse - Price: $29.99, Quantity: 15
Keyboard - Price: $79.99, Quantity: 10
Monitor - Price: $299.99, Quantity: 8

All product categories: {'Laptop', 'Monitor', 'Mouse', 'Keyboard'}

Price list: [999.99, 29.99, 79.99, 299.99]
Sorted prices: [29.99, 79.99, 299.99, 999.99]
Lowest price: $29.99
Highest price: $999.99

=== Final Inventory ===
Laptop - Price: $999.99, Quantity: 5
Mouse - Price: $29.99, Quantity: 12
Keyboard - Price: $79.99, Quantity: 10
Headphones - Price: $49.99, Quantity: 20
```

---

## Submission Requirements

1. Create a Python file for each question (or one combined file)
2. Include comments explaining your code
3. Test your code with the expected outputs
4. Submit to D2L by the deadline

## Grading Rubric

| Question | Points | Concepts Tested |
|----------|--------|-----------------|
| Q1 | 15 | Lists: append, sort, indexing, len |
| Q2 | 15 | Lists: index, count, remove, pop, in |
| Q3 | 15 | Tuples: creation, unpacking, tuple() |
| Q4 | 20 | Sets: operations, add, remove |
| Q5 | 15 | Dictionaries: CRUD, keys, values |
| Q6 | 20 | Combined: all collections |
| **Total** | **100** | |

---

## Tips

- **Lists** are mutable and ordered - use when order matters and you need to modify
- **Tuples** are immutable - use for fixed data like coordinates or records
- **Sets** have no duplicates - use for membership testing and set operations
- **Dictionaries** map keys to values - use for lookups and structured data
- Remember: `set()` creates an empty set, `{}` creates an empty dictionary!
