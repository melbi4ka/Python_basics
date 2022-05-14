pool_volume_litter = int(input())
debit_first_pipe = int(input())
debit_second_pipe = int(input())
hours_worker_absent = float(input())
pool_volume_level = debit_first_pipe*hours_worker_absent + debit_second_pipe*hours_worker_absent
pool_volume_level_percent = pool_volume_level/pool_volume_litter * 100
more_pool_water = abs(pool_volume_litter - pool_volume_level)
percent_first_pipe = (debit_first_pipe*hours_worker_absent / pool_volume_level) * 100
percent_second_pipe = (debit_second_pipe*hours_worker_absent / pool_volume_level) * 100

if pool_volume_litter >= pool_volume_level:
    print(f"The pool is {pool_volume_level_percent:.2f}% full. "
          f"Pipe 1: {percent_first_pipe:.2f}%. Pipe 2: {percent_second_pipe:.2f}%.")
else:
    print(f"For {hours_worker_absent} hours the pool overflows with {more_pool_water:.2f} liters.")


