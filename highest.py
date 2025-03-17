print("Input a non-number to display the highest number")

number_list = []

while True:
    try:
        number = int(input("Input a number: "))
        number_list.append(number)
    except ValueError:
        if number_list:
            print(max(number_list))
        break