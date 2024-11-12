
from src.run.running import Run

def second_set_of_numbers():
    array_values = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
    step = 2
    values = {
        4: 15,
        8: 3  
    }
    running = Run(array_values, step, values)
    running.step_one()
    running.step_two()
    running.step_three(5)
    running.step_four()
    running.step_five()
    running.quit()
    