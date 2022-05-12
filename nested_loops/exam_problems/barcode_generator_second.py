start = int(input())
end = int(input())

first_start = int(start/1000)
second_start = int((start/100) % 10)
third_start = int((start/10) % 10)
forth_start = int(start % 10)

first_end = int(end/1000)
second_end = int((end/100) % 10)
third_end = int((end/10) % 10)
forth_end = int(end % 10)

for num_one in range(first_start, first_end + 1):
    for num_two in range(second_start, second_end + 1):
        for num_tree in range(third_start, third_end + 1):
            for num_four in range(forth_start, forth_end + 1):
                if num_one % 2 != 0 and num_two % 2 != 0 and num_tree % 2 != 0 and num_four % 2 != 0:
                    print(f"{num_one}{num_two}{num_tree}{num_four}", end= " ")


