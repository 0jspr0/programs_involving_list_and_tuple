print("Input a non-number to display the highest number")

number_list = []

while True:
    try:
        number = int(input("Input a number: "))
        list.append(number)
    except ValueError:
        break