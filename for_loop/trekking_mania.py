group_climbers = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k_two = 0
everest = 0

for numbers in range(group_climbers):
    people_in_group = int(input())
    if people_in_group <= 5:
        musala += people_in_group
    elif people_in_group <= 12:
        monblan += people_in_group
    elif people_in_group <= 25:
        kilimandjaro += people_in_group
    elif people_in_group <= 40:
        k_two += people_in_group
    else:
        everest += people_in_group
all_climbers = musala + monblan + kilimandjaro + k_two + everest
percent_musala = musala/all_climbers * 100
percent_monblan = monblan/all_climbers * 100
percent_kilimanjaro = kilimandjaro/all_climbers * 100
percent_k_two = k_two/all_climbers * 100
percent_everest = everest/all_climbers * 100
print(f"{percent_musala:.2f}%")
print(f"{percent_monblan:.2f}%")
print(f"{percent_kilimanjaro:.2f}%")
print(f"{percent_k_two:.2f}%")
print(f"{percent_everest:.2f}%")


