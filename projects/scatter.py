import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c='red', edgecolor='none', s=20)

#set chart title and label axes
plt.title("Square Numbers", fontsize=20)
plt.xlabel("Value", fontsize=12)
plt.ylabel("Square of value", fontsize=12)

#set range for each axis
plt.axis([0, 1100, 0, 1100000])

#set size of tick labels
plt.tick_params(axis='both', which='major', labelsize=12)

plt.show()
