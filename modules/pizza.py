def make_pizza(size, *toppings):
    """Summarize pizza that is about to be made"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
