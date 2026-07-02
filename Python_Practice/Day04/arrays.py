#1.Write a Python program to find the maximum element without using max().
numbers = [12, 45, 7, 89, 34]
maximum = numbers[0]
for num in numbers:
    if num>maximum:
        maximum=num
print(maximum)

#2.Find the smallest element in the array.
numbers = [12, 45, 7, 89, 34]
minimum = numbers[0]
for num in numbers:
    if num<minimum:
        minimum=num
print(minimum)

#3.Write the program without using Python's built-in sum() function.
numbers = [12, 45, 7, 89, 34]
total = 0
for num in numbers:
    total +=num 
print(total)

#4.Count Even Numbers
#Write a program to count how many even numbers are in the array.
numbers = [12, 45, 7, 89, 34]
count = 0
for num in numbers:
    if num % 2 == 0:
        count += 1
print(count)

#5.Count Odd Numbers
#Write a program to count how many odd numbers are in the array.
numbers = [12, 45, 7, 89, 34]
count = 0
for num in numbers:
    if num % 2 != 0:
        count += 1
print(count)