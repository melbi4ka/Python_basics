student_ticket_counter = 0
standart_ticket_counter = 0
kid_ticket_counter = 0
total_ticket_counter = 0
comand = input()
while comand != "Finish":
    seats = int(input())
    total_seats = seats
    sold_tickets = 0
    while seats > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_ticket_counter += 1
        elif ticket_type == "standard":
            standart_ticket_counter += 1
        elif ticket_type == "kid":
            kid_ticket_counter += 1
        seats -= 1
        sold_tickets += 1
        total_ticket_counter += 1
    print(f"{comand} - {sold_tickets/total_seats * 100:.2f}% full.")
    comand = input()

print(f"Total tickets: {total_ticket_counter}")
print(f"{student_ticket_counter/total_ticket_counter * 100:.2f}% student tickets.")
print(f"{standart_ticket_counter/total_ticket_counter * 100:.2f}% standard tickets.")
print(f"{kid_ticket_counter/total_ticket_counter * 100:.2f}% kids tickets.")
