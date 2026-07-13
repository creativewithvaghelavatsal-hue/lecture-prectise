#sets , dictionary , type coversion , list of dictionary

print("="*50)
print("1.set operations")
print("="*50)

numbers = {1 , 2 , 3 , 4 , 5}

print(type(numbers))

numbers.add(4)

numbers.remove(2)

print("is 2 present ?",  3 in numbers)

print(numbers)

print("="*50)
print("2.union , intersection and difference")
print("="*50)

set_a = {1 , 2 , 3 , 4}

set_b = {3 , 4 , 5 , 6}

print(set_a)

print(set_b)

print("union :", set_a.union(set_b))
print("intersection:" , set_a.intersection(set_b))
print("difference:" , set_b.difference(set_a))
print("difference:" , set_a.difference(set_b))

print("=" * 50)
print("3. dictionary operations")
print("=" * 50)

student = {
    "name":"sagar",
    "age":19,
    "grade":"b"
}

for key in student.keys():
    print(f"{key} : {student[key]}")

for value in student.values():
    print(value)

print(student['name'])

student["city"] = "panjab"

student["age"] = 20

print(student)

del student["grade"]

print(student)

print("=" * 50)
print("4. Dictionary from Lists")
print("=" * 50)


keys = ['id' , 'name' , 'email']
values = [101 , 'sagar' , 'traveler@gmail.com']

user = {}

for i in range(len(keys)):
    user[keys[i]] = values[i]

print(user)

print("=" * 50)
print("5. Type Conversion")
print("=" * 50)

num = '852'

print(type(num))

nums = int(num)

print(type(nums))

list_1 = [1 , 2 , 3 , 4]

tuple_1 = tuple(list_1)

print(tuple_1)

pairs = [(1 , "A") , (2 , "B")]

print(dict(pairs))


