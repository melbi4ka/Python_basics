days_of_work = int(input())
treated_patience = 0
untreated_patience = 0
doctors = 7

for num in range(1, days_of_work+1):
    num_patience = int(input())

    if num % 3 == 0:
        if untreated_patience > treated_patience:
            doctors += 1

    if doctors - num_patience >= 0:
        treated_patience += num_patience
    else:
        treated_patience += doctors
        untreated_patience += num_patience - doctors



print(f"Treated patients: {treated_patience}.")
print(f"Untreated patients: {untreated_patience}.")


