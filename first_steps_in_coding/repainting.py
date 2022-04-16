needed_nylon = int(input())
needed_paint = int(input())
paint_tinner = int(input())
hours_for_workers = int(input())
all_costs = (needed_nylon+2)*1.5 + needed_paint*1.1*14.5+paint_tinner*5+0.4
sum_for_workers = hours_for_workers*(all_costs*0.3)
total_sum = all_costs + sum_for_workers
print(total_sum)
