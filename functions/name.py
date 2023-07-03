def formatted_name(first_name, second_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + second_name
    return full_name.title()

    #Creating loop to greet person
    while True:
        print("Please tell me your name: ")
	f_name = input("First name: ")
	if f_name == 'q':
	    break
	l_name = input("Last name: ")
	if l_name == 'q':
	    break

	form_name = formatted_name(f_name, l_name)
	print("\nHello, " + form_name + "!")

musician = formatted_name('bob', 'marley')
print(musician)
