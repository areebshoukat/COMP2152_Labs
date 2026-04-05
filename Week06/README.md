# Week 06 -- File I/O, CSV, Binary Files & Persistence

Professor Maziar\
COMP2152 -- Open-Source Development with Python

------------------------------------------------------------------------

## Overview

This week we move from simple scripts to persistent programs ---
programs that save data to files and retrieve it later.

You will progressively learn:

1.  How to read from text files\
2.  How to write to text files\
3.  How to work with CSV files\
4.  How to process and transform structured data\
5.  How to store Python objects in binary format using pickle

------------------------------------------------------------------------

# Example 1 -- Basic Text File Reading

``` python
file = open("students.txt", "r")

for line in file:
    print(line.strip())

file.close()
```

------------------------------------------------------------------------

# Example 2 -- Writing and Reading Back

``` python
courses = []

for i in range(3):
    name = input("Enter course name: ")
    courses.append(name)

with open("courses.txt", "w") as file:
    for course in courses:
        file.write(course + "\n")

print("Saved successfully.\n")

with open("courses.txt", "r") as file:
    for line in file:
        print(line.strip())
```

------------------------------------------------------------------------

# Example 3 -- Working with CSV Files

``` python
import csv

students = [
    ["Alice", 85],
    ["Bob", 92],
    ["Charlie", 78]
]

with open("grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)

with open("grades.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], "->", row[1])
```

------------------------------------------------------------------------

# Example 4 -- CSV Data Transformation

``` python
import csv

with open("payroll.csv") as infile, open("payroll_output.csv", "w", newline="") as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["Salary"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)

    writer.writeheader()

    for row in reader:
        salary = float(row["Hours"]) * float(row["Rate"])
        row["Salary"] = f"{salary:.2f}"
        writer.writerow(row)
```

------------------------------------------------------------------------

# Example 5 -- Persistent Movie Manager (Binary + Exceptions)

``` python
import pickle

FILENAME = "movies.bin"

def load_movies():
    try:
        with open(FILENAME, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def save_movies(movies):
    with open(FILENAME, "wb") as file:
        pickle.dump(movies, file)

def main():
    movies = load_movies()

    while True:
        print("\n1. List\n2. Add\n3. Exit")
        choice = input("Choice: ")

        if choice == "1":
            for i, m in enumerate(movies):
                print(i+1, m)

        elif choice == "2":
            name = input("Movie name: ")
            movies.append(name)
            save_movies(movies)
            print("Saved!")

        elif choice == "3":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
```

------------------------------------------------------------------------

## Conceptual Progression

  Level   Skill                  Core Idea
  ------- ---------------------- ---------------------------
  1       Basic                  Read text file
  2       Fundamental            Write safely using `with`
  3       Structured Data        CSV handling
  4       Data Engineering       Transform & compute
  5       Software Engineering   Persistent object storage

Master this progression --- it is foundational for real-world software
development.
