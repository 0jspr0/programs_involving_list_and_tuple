print("Input 10 numbers to display the numbers with duplicates")

unique_list = []
duplicate_list = []

for i in range(10):
    number = int(input(f"Input number {i + 1}: "))
    if number not in unique_list:
        unique_list.append(number)
    else:
        duplicate_list.append(number)