person = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Accessing data
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")

# Adding a new key-value pair
person['job'] = 'Software Engineer'

# Looping through dictionary
for key, value in person.items():
    print(f"{key}: {value}")
