
L1cc = []
person1 = {
    "First_name":"Vammy",
    "Last_name":"Jiang",
    "Age":"17",
}

L1cc.append(person1)



i = 1

for person in L1cc:
    print(str(i)+". name: " + person["First_name"],"\nage: " +person["Age"])
    i+=1
