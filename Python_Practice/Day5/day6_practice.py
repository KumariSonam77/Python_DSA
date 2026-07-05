#Question 1: Print First Character. Print the first character.
name = "Python"
print(name[0])

#Question 2: Print Last Character
name = "Software"
print(name[-1])

#Question 3: Print Length.
text = "Programming"
print(len(text)) 

#Question 4: Convert to Uppercase
text = "python"
print(text.upper())

#Question 5: Convert to Lowercase
text = "HELLO"
print(text.lower())

#Question 6: Count the Letter 'a
text = "banana"
print(text.count('a'))

#Question 7: Find the Letter
text = "Programming"
print(text.find('g'))

#Question 8: Replace a Word
text = "I love Python"
print(text.replace("Python", "Java"))

#Question 9: Split the String
text = "Python is easy"
print(text.split())

#Question 10: Count Vowels
text = "education"
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(count)

#Question 11: Reverse a String
text = "Python"
print(text[::-1])

#Question 12: Count Spaces
text = "I love Python programming"
print(text.count(" "))