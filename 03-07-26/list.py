#python collection

print("====python collection====")

#list

list1=[10,20,30,40]

print(type(list1))

print(list1)

print(list[0])

print(list[1])

print(list[2])

print(list[3])

for i in list1:
    print(i)

# Mutability

list1[1] = 200

#append()

list1.append(50)
list1.append(60)

print(list1)

#operations

print("max :",max(list1))
print("min :",min(list1))

list1.append (10)

print(list1)

#remove duplicate value

unique = []

for i in list1:
    if i not in unique:
        unique.append(i)

print(unique)

# Tuple

tuple1 = (1 , 2 , 3 , 4 , 4 , 6 , 4 , 2)

print(tuple1[5])

# count

print("count of 5:", tuple1.count(2))

#swipping using tuple

a , b = 10 , 20

print(a)

a , b = b , a

print(a)
print(a , b)

# SET

data = [1 , 2 , 3 , 4 , 5 , 6 , 6]

set1 = set(data)

print(set1)

# set operations

a = {1 , 2 , 3}
b = {4 , 5 , 6 , 1}

print(a | b)

print(a & b)

set1.add(10)
set1.remove(1)


print(set1)

# Dictionary

dict1 = {
    "name":"sagar",
    "Age":18
    }

print(dict1["name"])
print(dict1.get("Age"))

dict1["name"] = "vatsal "

print(dict1)
