# Day 3 Notes - Python Functions & Arrays
## 1. Function
* A function is a block of code that performs a specific task.
* It helps avoid writing the same code again and again.

### Syntax
def function_name():
    # code
Example:
def greet():
    print("Good Morning")
greet()
---

## 2. Parameters and Arguments

* **Parameter:** Variable inside the function.
* **Argument:** Actual value passed to the function.
Example:
def greet(name):
    print("Hello", name)
greet("Sonam")

Output:
Hello Sonam
---

## 3. Return Statement

* `return` sends the result back.
* `print()` only displays the result.
Example:
def add(a, b):
    return a + b
result = add(5, 6)
print(result)

Output:
11
---

## 4. Local Variable

* A variable created inside a function.
* It can only be used inside that function.

Example:
def test():
    x = 10
    print(x)
test()
---

## 5. Global Variable

* A variable created outside a function.
* It can be used inside and outside the function.
Example:
x = 100
def show():
    print(x)
show()
print(x)
---

# Arrays (Python List)
## What is an Array?

* An array is a collection of elements stored in one variable.
* In Python, we use **lists** as arrays.

Example:
numbers = [5, 10, 15, 20, 25]
---

## Indexing
* Python indexing starts from **0**.
| Index | Value |
| ----: | ----: |
|     0 |     5 |
|     1 |    10 |
|     2 |    15 |
|     3 |    20 |
|     4 |    25 |
Example:
print(numbers[0])
Output:
5
---

## Negative Indexing

* `-1` means the last element.

Example:
print(numbers[-1])
Output:
25
---

## Update an Element
Example:
numbers[2] = 100
print(numbers)
Output:
[5, 10, 100, 20, 25]
---

## Length of an Array

Use `len()` to count elements.
Example:
print(len(numbers))
Output:
5
---

## Traverse an Array
### Print only values

for num in numbers:
    print(num)

### Print index and value

for i in range(len(numbers)):
    print(i, numbers[i])
---

# Time Complexity
| Operation         | Complexity |
| ----------------- | ---------- |
| Access an element | O(1)       |
| Traverse an array | O(n)       |
---

# Key Points
* Functions help reuse code.
* Parameters receive values.
* Arguments are actual values passed.
* `return` sends a value back.
* Local variables exist only inside a function.
* Global variables exist outside a function.
* Arrays store multiple values in one variable.
* Python indexing starts from **0**.
* Use `len()` to find the array length.
* Use `for` loops to traverse arrays.
