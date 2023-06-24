# Empty list
aliens = []

for i in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show first 7 aliens
for alien in aliens[:8]:
    print(alien)
print('...')

print("Total number of aliens is:", len(aliens))
