def greet_users(names):
    """Greet each user in list"""
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)

usernames = ["henry", "mercy", "victor"]
greet_users(usernames)
