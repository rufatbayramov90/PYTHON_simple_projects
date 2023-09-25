'''number = 0
while number<8:
    print(number)
    number = number + 1
    print("Transaction completed")
'''

'''number = 0 

while number <10:
    if number % 2 == 0:
        print(number)
    number += 1 
'''

'''num = 0
while num < 10:
    num = num + 1
    if num % 2 != 0:
        continue
print(num)
'''

'''while True:
    name = input("Add your Name")
    if name == "Rufo":
        break
    print(name)
'''

'''list = ["Car", "Fruit", "Cities", "Examples"]
print(list[-1])
print(list[2])
list.append("People")
print(list)

list_Two = ["Melas", "Programmers"]
list_All = list + list_Two
print(list_All)

list_Filter1 = list_All[1:3]
list_Filter2 = list_All[1:]
list_Filter3 = list_All[:3]

print(list_Filter1)
print(list_Filter2)
print(list_Filter3)
'''

'''
#range
listRange = list(range(10))
print(listRange)
#remove 
listRange.remove(2)
print(listRange)
#reverse
listRange.reverse()
print(listRange)
#for
for item in range(14):
    if item % 2 == 0:
        print(item)
'''

person = {
    'name' : "Rufo",
    'surname' : "Bayram",
    'age': 32
}
'''
#Add height 
person['height'] = 1.76
print(person)
#...
print(person['name'])

#If person has name, it prints its value
if "Alex" in person:
    print(person["Alex"])
else:
    print("There is no such name")

#If Alex isn't there returns an error
print(person.get("Alex",False))


for key, value in person.items():
    print(key,"=",value)
'''
'''#writes the values
for value in person.keys():
    print(person[value])
#writes the key
for key in person.keys():
    print(key)
'''


basket = set()
basket.add("Alis")
basket.add("Kevin")
print(basket)

#remove Kevin
basket.remove("Kevin")
print(basket)

#clear basket
basket.clear()

#sort from less to more  (does not take the same values)
odd_number = set([1,3,5,7])
even_number = set([2,4,6])
print(odd_number.union(even_number))

#received the same values
prime_number =set ([2,5,4,9,11])
print(odd_number.intersection(prime_number))










