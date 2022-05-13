from math import floor

w = float(input()) * 100
h = float(input()) * 100
row_buroes = floor((h - 100) / 70)
colomn_buroes = floor(w / 120)
number_buroes = row_buroes * colomn_buroes - 3
print(floor(number_buroes))
