from src.run.running import Run

def third_set_of_numbers():
    array_values = [50, 40, 30, 20, 10, 5, 3]
    step = 3
    values = {
        2: 60,
        5: 1  
    }
    running = Run(array_values, step, values)
    running.step_one()
    running.step_two()
    running.step_three()
    running.step_four()
    running.quit()