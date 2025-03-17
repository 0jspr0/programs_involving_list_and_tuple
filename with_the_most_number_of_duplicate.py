print("Input a non-number to display the numbers with the most number of duplicates")

number_list = []
with_the_most_number_of_duplicate_list = []

while True:
    try:
        number = int(input("Input a number: "))
        list.append(number)
    except ValueError:
        break

if number_list:
    max_count = 0
    
    for i in number_list:
        count = number_list.count(i)
        
        if count >= max_count:
            max_count = count
            
            if i not in with_the_most_number_of_duplicate_list:
            	with_the_most_number_of_duplicate_list.append(i)

for i in with_the_most_number_of_duplicate_list:
	print(i)