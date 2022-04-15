number_chicken_menus = int(input())
number_fish_menus = int(input())
number_veggie_menus = int(input())
menu_costs = number_chicken_menus*10.35 + number_fish_menus*12.4 + number_veggie_menus*8.15
desert = menu_costs*0.2
total_sum = menu_costs + desert + 2.5
print(total_sum)

