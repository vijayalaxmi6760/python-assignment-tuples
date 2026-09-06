person1 = {"A", "B", "C", "D"}
person2 = {"C", "D", "E", "F"}

print("Common friends:", person1.intersection(person2))
print("Friends not in common:", person1.symmetric_difference(person2))