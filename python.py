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

list = ["Car", "Fruit", "Cities", "Examples"]
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



