from src.run.running import Run

def first_set_of_numbers():
    array_values = [10, 5, 20, 1, 15, 30, 25]
    step = 1
    values = {
        3: 50,
        1: 8  
    }
    running = Run(array_values, step, values)
    running.step_one()
    running.step_two()
    running.step_three(3)
    running.step_four()
    running.step_five()
    running.quit()