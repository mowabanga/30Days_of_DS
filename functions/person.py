def person(first_name, last_name):
    """Return a dictionary of info about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = person('bruno', 'mars')
print(musician)
