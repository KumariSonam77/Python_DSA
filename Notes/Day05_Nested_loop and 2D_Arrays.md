# Day 5 - Nested Loops & 2D Arrays
## Nested Loop
A nested loop is a loop inside another loop.

Example:
for i in range(2):
    for j in range(2):
        print(i, j)
Output:
0 0
0 1
1 0
1 1
---

## 2D Array
A 2D array is a list of lists.
Example:

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
Rows = 2
Columns = 3
---

## Accessing Elements
matrix[row][column]

Examples:
matrix[0][0] = 1
matrix[0][2] = 3
matrix[1][1] = 5
---

## Traversing a Matrix
Method 1
for row in matrix:
    for num in row:
        print(num)

Method 2
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j])
---

## Important Points
- Outer loop works on rows.
- Inner loop works on columns.
- matrix[row][column]
- print() inside a loop prints every iteration.
- print() outside a loop prints only once after the loop finishes.
---