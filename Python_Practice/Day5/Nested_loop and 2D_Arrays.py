#Question 1: Print All Elements
matrix = [
     [2, 4],
     [6, 8]
 ]
for row in matrix:
    for num in row:
        print(num)

#Question 2: Find the Sum of All Elements
matrix2 = [
    [1, 2],
    [3, 4]
]
total = 0
for row in matrix2:
    for num in row:
        total += num
print(total)

#Question 3: Count Even Numbers
matrix3 = [
    [1, 2],
    [4, 7]
]
even_count= 0
for row in matrix3:
   for num in row:
       if num%2==0:
         even_count+=1
print(even_count)   

#Question 4: Find the Maximum Element
matrix4 = [
    [8, 2, 5],
    [10, 3, 6]
]
maximum = matrix4[0][0]
for row in matrix4:
    for num in row:
        if num > maximum:
            maximum=num
print(maximum)

#Question 5: Find the Minimum Element
matrix5 = [
    [8, 2, 5],
    [10, 3, 6]
]
minimum = matrix5[0][0]
for row in matrix5:
    for num in row:
        if num < minimum:
            minimum=num
print(minimum)

#Question 6: Count Odd Numbers
matrix6 = [
    [1, 2, 3],
    [4, 5, 6]
]
odd_count = 0
for row in matrix6:
    for num in row:
        if num % 2 != 0:
            odd_count += 1
print(odd_count)

#Question 7: Print Row Sums
matrix7 = [
    [1, 2, 3],
    [4, 5, 6]
]
for row in matrix7:
    print(sum(row))

#Question 8: Find the Richest Customer
accounts = [
    [1, 5],
    [7, 3],
    [3, 5]
]
maximum = 0
for account in accounts:
    total = sum(account)
    if total > maximum:
        maximum = total
print(maximum)

#Question 9: Print Matrix Row by Row
matrix9 = [
    [10, 20],
    [30, 40]
]
for row in matrix9:
    for num in row:
        print(num, end=" ")
    print()

#Question 10:Find the average of all elements.
matrix10 = [
    [2, 4],
    [6, 8]
]
total = 0
count = 0
for row in matrix10:
    for num in row:
        total += num
        count += 1
average = total / count
print("Average =", average)

