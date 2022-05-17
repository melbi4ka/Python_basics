num_of_cargoes = int(input())
price = 0
microbus = 0
truck = 0
train = 0

for num in range(num_of_cargoes):
    tons_per_cargo = int(input())

    if tons_per_cargo <= 3:
        price += tons_per_cargo * 200
        microbus += tons_per_cargo
    elif 3 < tons_per_cargo <= 11:
        price += tons_per_cargo * 175
        truck += tons_per_cargo
    elif tons_per_cargo > 11:
        price += tons_per_cargo * 120
        train += tons_per_cargo

all_cargoes = microbus + truck + train
microbus_percent = microbus / all_cargoes * 100
truck_percent = truck / all_cargoes * 100
train_percent = train / all_cargoes * 100

print(f"{(price/all_cargoes):.2f}")
print(f"{microbus_percent:.2f}%")
print(f"{truck_percent:.2f}%")
print(f"{train_percent:.2f}%")

