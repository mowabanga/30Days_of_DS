prompt = "Please enter the name of the city you have visited: "
prompt += "\n(Enter 'q' when you are finished)\n"

while True:
    city = input(prompt)

    if city == 'q':
        break
    else:
        print("I'd love to go to,", city, '\n')
