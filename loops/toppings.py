available_toppings = ['mushrooms', 'olives', 'pepperoni', 'extra cheese', 'green peppers']

requested_toppings = ['mushrooms', 'extra_cheese']

for topping in requested_toppings:
    if topping in available_toppings:
         print("Adding", topping)
    else:
         print("Topping not available.")

print("\nFinished making the pizza.")
