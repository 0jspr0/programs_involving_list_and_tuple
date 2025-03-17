print("Input a non-number to display the average of the numbers")

number_list = []

while True:
    try:
        number = int(input("Input a number: "))
        number_list.append(number)
    except ValueError:
        break

if number_list:
    average = sum(number_list) / len(number_list)
    print(average)