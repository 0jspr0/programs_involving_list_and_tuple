print("Input a non-number to display the numbers with the most number of duplicates")

number_list = []

while True:
    try:
        number = int(input("Input a number: "))
        list.append(number)
    except ValueError:
        break