comand = input()
prime_sum = 0
non_prime_sum = 0

while comand != "stop":
    current_number = int(comand)
    if current_number < 0:
        print("Number is negative.")
    else:
        prime_number = True
        for number in range(2, current_number):
            if current_number % number == 0:
                prime_number = False
                break
        if prime_number:
            prime_sum += current_number
        else:
            non_prime_sum += current_number
    comand = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {non_prime_sum}")


