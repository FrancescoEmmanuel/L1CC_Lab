
L1cc = []
person1 = {
    "First_name":"Troy",
    "Last_name":"Prajoga",
    "Age":"16",
}

L1cc.append(person1)



i = 1

for person in L1cc:
    print(str(i)+". name: " + person["First_name"],"\nage: " +person["Age"])
    i+=1
