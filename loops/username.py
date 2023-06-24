usernames = ['alvin', 'peter', 'alex', 'benjamin', 'catherine', 'susan']
new_users = ['mwaniki', 'peter', 'marvin', 'joy', 'ivy', 'susan']

for new_user in new_users:
    if new_user in usernames:
        print("Sorry, the username is not available.")
    else:
        print("Username available.")
