
L1cc = []
person1 = {
    "First_name":"Marcelinus",
    "Last_name":"Luviandanu",
    "Age":"20",
    "Hobby":"Wanker",
    }

L1cc.append(person1)



i = 1

for person in L1cc:
    print(str(i)+". name: " + person["First_name"],"\nage: " +person["Age"],"\nhobby: " +person["Hobby"])
    i+=1
