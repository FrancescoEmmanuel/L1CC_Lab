
L1cc = []
person1 = {
<<<<<<< HEAD
    "First_name":"Rheynorich",
    "Last_name":"Kalistone",
    "Age":"16",
=======
    "First_name":"Harry",
    "Last_name":"Chiu",
    "Age":"18",
>>>>>>> c2d03833e8194e0e71b40f410b761ebdfa978db2
}

L1cc.append(person1)


i = 1

for person in L1cc:
    print(str(i)+". name: " + person["First_name"],"\nage: " +person["Age"])
    i+=1
