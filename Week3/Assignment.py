
L1cc = []
person1 = {
    "First_name":"Samuel",
    "Last_name":"James Setiadi",
    "Age":"18",
}

L1cc.append(person1)



i = 1

for person in L1cc:
    print(str(i)+". name: " + person["First_name"],"\nage: " +person["Age"])
    i+=1
