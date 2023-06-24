alien_0 = {'color': 'blue', 'points': 4, 'x_position': 0, 'y_posiiton': 25, 'speed': 'medium'}

print("Original x position:", alien_0['x_position'])

# Move the alien to the right
# Determine how far to move the alien relative to its speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# The new position is the old position plus increment
alien_0['x_position'] += x_increment

print("\nNew x position:", alien_0['x_position'])
