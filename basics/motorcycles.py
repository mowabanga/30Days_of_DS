motorcycles = ['bmw', 'suzuki', 'yamaha']
print(motorcycles)

# Replacing item in list

motorcycles[0] = 'ducati'
print(motorcycles)

# Adding item in list

motorcycles.append("boxer")
print(motorcycles)

# Inserting element into list at any position
motorcycles.insert(2, 'harleys')
print(motorcycles)

# Deleting item from list using del
del motorcycles[0]
print(motorcycles)

# Deleting last item from list using pop
pop_item = motorcycles.pop()
print(motorcycles)
print(pop_item)

# Deleting any item from list
popped_item = motorcycles.pop(1)
print(motorcycles)
print(popped_item)








