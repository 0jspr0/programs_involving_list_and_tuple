print("Input a non-number to display the numbers from highest to lowest")

number_list = []

while True:
    try:
        number = int(input("Input a number: "))
        list.append(number)
    except ValueError:
        break

number_list.sort()

for i in number_list:
    print(i)