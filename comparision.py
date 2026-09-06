customer1 = {"Rice", "Milk", "Bread", "Eggs"}
customer2 = {"Milk", "Bread", "Sugar", "Tea"}

print("Items both bought:", customer1.intersection(customer2))

print("Only Customer 1:", customer1.difference(customer2))

print("Only Customer 2:", customer2.difference(customer1))

print("Total unique items:", len(customer1.union(customer2)))