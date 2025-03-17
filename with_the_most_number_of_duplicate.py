print("Input a non-number to display the numbers with the most number of duplicates")

number_list = []
with_the_most_number_of_duplicate_list = []

while True:
    try:
        number = int(input("Input a number: "))
        list.append(number)
    except ValueError:
        break