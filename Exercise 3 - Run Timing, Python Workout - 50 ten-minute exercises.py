# For this exercise, then, we’ll assume that you run 10 km each day
# as part of your exercise regime. You want to know how long, on average,
# that run takes. Write a function (run_timing) that asks how long
# it took for you to run 10 km. The function continues to ask how long
# (in minutes) it took for additional runs, until the user presses Enter.
# At that point, the function exits--but only after calculating and
# displaying the average time that the 10 km runs took.

def run_timing():
    runs = 0
    time = 0
    run = True
    while run:
        one_run = input("How long did it take to run 10 km? ")
        if not one_run:
            break
        runs += 1
        time += float(one_run)
        average_time = time / runs
    print(f'Average of {average_time}, over {runs} runs')



run_timing()