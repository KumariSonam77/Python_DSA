#1.Create a function that prints:
def greet():
    print("good morning")

#2.Create a function named square() that returns the square of a number.
def square(num):
    return num * num
print(square(7))

#3.Create a function that adds two numbers.
def add(a,b):
    return a+b
x = add(5,6)
print(x)

#4.Create a function that prints:
def greet(name):
    print("Welcome", name)
greet("Sonam")

#5.Create a function that checks whether a number is even or odd.
def number(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
number(8)
number(5)

#6.Print the first element.
numbers = [5, 10, 15, 20, 25]
print(numbers[0])

#7.Print the last element using negative indexing.
numbers = [5, 10, 15, 20, 25]
print(numbers[-1])

#8.Replace 15 with 100.
numbers = [5, 10, 15, 20, 25]
numbers[2] = 100
print(numbers)

#9.Print the length of the array.
numbers = [5, 10, 15, 20, 25]
print(len(numbers))

#10.Print every element using a for loop.
numbers = [5, 10, 15, 20, 25]
for num in numbers:
    print(num)

#11.Print both the index and the value.
numbers = [5, 10, 15, 20, 25]
for i in range(len(numbers)):
    print(i, numbers[i])

