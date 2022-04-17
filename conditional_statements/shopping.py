budget = float(input())
number_videocards = int(input())
number_processors = int(input())
number_ram_cards = int(input())
price_videocards = number_videocards * 250
price_processors = price_videocards * 0.35
price_ram_cards = price_videocards * 0.10
total_sum = price_videocards + price_processors * number_processors + price_ram_cards * number_ram_cards
if number_videocards > number_processors:
    total_sum = total_sum * 0.85
final_sum = abs(total_sum - budget)
if total_sum <= budget:
    print(f"You have {final_sum:.2f} leva left!")
else:
    print(f"Not enough money! You need {final_sum:.2f} leva more!")



