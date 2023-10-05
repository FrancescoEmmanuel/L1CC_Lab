L1cc = []
person1 = {
    "First_name":"Ahmad",
    "Last_name":"Zaydan",
    "Age":"18",
    "Hobby":"wacthing pornhub",
}

L1cc.append(person1)

person2 = {
    "First_name":"Haniif",
    "Last_name":"Wardana",
    "Age":"17",
}

L1cc.append(person2)

i = 1

for person in L1cc:
    print(str(i)+". name: " + person["First_name"],"\nage: " +person["Age"])
    i+=1
