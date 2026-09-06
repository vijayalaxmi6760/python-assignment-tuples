t = (10, 20, 10, 30, 20, 40, 10)

unique = set(t)

print("Unique numbers:", unique)

print("Duplicate numbers:")
for x in unique:
    if t.count(x) > 1:
        print(x)