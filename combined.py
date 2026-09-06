student1 = {"Python", "SQL", "Java"}
student2 = {"Python", "SQL", "HTML"}

print("Both students:", student1.intersection(student2))
print("Only Student 1:", student1.difference(student2))
print("Only Student 2:", student2.difference(student1))
print("All subjects:", student1.union(student2))