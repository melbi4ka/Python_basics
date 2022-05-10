number_bitcoins = int(input())
number_chinese_money = float(input())
comission = float(input())

price_bitcoin = 1168 / 1.95
price_chinese_to_dol = 0.15
price_chinese_dol_to_lv = price_chinese_to_dol * 1.76
lev_to_eu = price_chinese_dol_to_lv / 1.95

commision_sum = (number_bitcoins * price_bitcoin + number_chinese_money * lev_to_eu) * comission/100
all_money = number_bitcoins * price_bitcoin + number_chinese_money * lev_to_eu - commision_sum

print(f"{all_money:.2f}")

