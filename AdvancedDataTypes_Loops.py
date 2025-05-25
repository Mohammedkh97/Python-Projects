my_dict = {'name': 'Alice', 'age': 30}
print(my_dict['name'])  # Output: Alice
my_dict['city'] = 'London'
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'London'}
my_dict['age'] = 31
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'London'}
# my_dict.pop('city')
# print(my_dict)  # Output: {'name': 'Alice', 'age': 31}

for key, value in my_dict.items():
    print(key, value)

# List
numbers = [1, 2, 3]
for n in numbers:
    print(n)

# Tuple
coords = (10, 20)
for c in coords:
    print(c)

# Dictionary
person = {'name': 'Max', 'age': 30}
for key, value in person.items():
    # print(f"{key}: {value}")
    print(key, value)

# Set
unique_numbers = {1, 2, 3}
for num in unique_numbers:
    print(num)

