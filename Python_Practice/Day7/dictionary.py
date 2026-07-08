#I have created a dictionary with two key-value pairs and printed the value associated with the key "name".
student = {
    "name": "Sonam",
    "age": 21
}
print(student["name"])

#printed the value associated with the key "age".
student = {
    "name": "Sonam",
    "age": 21
}
student["city"] = "Patna"
print(student)

#updated the value associated with the key "age" to 22, then printed the updated value.
student = {
    "name": "Sonam",
    "age": 21
}
student["age"] = 22
print(student["age"])

#removed the key-value pair with the key "city" from the dictionary and printed the updated dictionary.
student = {
    "name": "Sonam",
    "age": 21,
    "city": "Patna"
}
student.pop("city")
print(student)

#printed all the keys in the dictionary.
student = {
    "name": "Sonam",
    "age": 21
}
print(student.keys())

## Printed all the keys in the dictionary.
student = {
    "name": "Sonam",
    "city": "Patna"
}
for key in student:
    print(key)

#printed all the key-value pairs in the dictionary.
student = {
    "name": "Sonam",
    "city": "Patna"
}
for value in student.values():
    print(value)

#printed all the key-value pairs in the dictionary.
student = {
    "name": "Sonam",
    "city": "Patna"
}
for key, value in student.items():
    print(key, value)