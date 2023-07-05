print("Give me two numbers and I'll print them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("Second Number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except:
        print("You can't divide by 0!")
    else:
        print(answer)
