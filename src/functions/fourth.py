from src.run.running import Run

def fourth_set_of_numbers():
    array_values = [13, 26, 19, 17, 24, 31, 22, 11, 8, 20, 5, 27, 18]
    step = 4
    values = {
        7: 35,
        10: 12  
    }
    running = Run(array_values, step, values)
    running.step_one()
    running.step_two()
    running.step_three()
    running.step_four()
    running.quit()
    