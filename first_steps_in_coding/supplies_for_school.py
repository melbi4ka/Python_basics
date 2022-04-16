number_pens = int(input())
number_markers = int(input())
litters_detragent = int(input())
discount_percent = int(input())
sum_before_discount = number_pens * 5.8 + number_markers * 7.2 + litters_detragent * 1.2
sum_after_discount = sum_before_discount - (sum_before_discount * discount_percent / 100)
print(f"{sum_after_discount:.2f}")




