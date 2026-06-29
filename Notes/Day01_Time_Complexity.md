Day 1 - Time & Space Complexity
**Date:** 29 June 2026

# What is Time Complexity?

Time Complexity tells us how much time an algorithm takes as the input size increases.
It does not measure actual seconds.
It measures how the running time grows with the input.
---

# Types of Time Complexity

## 1. O(1) - Constant Time
The execution time does not change even if the input size increases.

Example:
```python
print("Hello")
```
---

## 2. O(n) - Linear Time

The program runs once for every input element.

Example:
```python
for i in range(n):
    print(i)
```
---

## 3. O(n²) - Quadratic Time

Two nested loops depend on n.

Example:
```python
for i in range(n):
    for j in range(n):
        print(i, j)
```
---

# Important Rules

✅ Ignore constants.

Example:
O(5) → O(1)
O(100n) → O(n)
O(2n) → O(n)
---

# What is Space Complexity?

Space Complexity tells us how much extra memory an algorithm uses.
Only extra memory is counted.
The input array is not counted.

---

## O(1) Space

Only a few variables are used.
Example:

```python
count = 0
largest = 0
```
---

## O(n) Space

Extra list, dictionary or set is created.
Example:

```python
new = []
for i in range(n):
    new.append(i)
```
---

# Difference

| Time Complexity | Space Complexity |
|-----------------|------------------|
| Measures execution time | Measures extra memory |
| Related to loops | Related to extra variables and data structures |
---

# Today's Learning

✔ Learned Time Complexity
✔ Learned Space Complexity
✔ Learned O(1)
✔ Learned O(n)
✔ Learned O(n²)
--

# Mistakes I Made Today

1. I confused constant loops with n loops.
2. I thought every nested loop gives O(n²), but if the inner loop is constant, the answer is O(n).
3. I confused Time Complexity with Space Complexity.
---

# Placement Tip
Always ask yourself:

1. How many times does the code execute?
2. How much extra memory is being used?
Then decide the Time and Space Complexity.