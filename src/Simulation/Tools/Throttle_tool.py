
##################################################################################################################
"""

"""

# Built-in/Generic Imports
import sys
from math import log10

# Libs

# Own modules

__version__ = '1.1.1'
__author__ = 'Victor Guillet'
__date__ = '31/01/2021'

##################################################################################################################


def throttle(current_iteration, nb_of_iterations, max_value, min_value=1., direction="up", decay_function=0):
    """
    Throttle a value according to the instance in the run time.

    if direction == up: Small to big
    if direction == down: Big to small


    The following decay functions settings can be used:
            0 - Fixed value (returns max value)

            1 - Linear decay

            2 - Logarithmic decay (in development)

    :param current_iteration: Current iteration
    :param nb_of_iterations: Total number of iteration to consider
    :param max_value: Max allowed value
    :param min_value: Min allowed value
    :param direction: "up" or "down", defines throttling direction
    :param decay_function: Decay function setting
    :return: Throttled value
    """

    # TODO: add decay functions (log/exponential etc...)
    if current_iteration <= nb_of_iterations:
        # --> Fixed value decay
        if decay_function == 0:
            return max_value

        # --> Linear decay
        elif decay_function == 1:
            if direction == "up":
                throttled_value = min_value + (max_value - min_value) / nb_of_iterations * current_iteration

                if throttled_value >= max_value:
                    throttled_value = max_value
            else:
                throttled_value = max_value - (max_value - min_value) / nb_of_iterations * current_iteration

                if throttled_value <= min_value:
                    throttled_value = min_value

        # --> Logarithmic decay
        # TODO: Complete log decay
        elif decay_function == 2:
            throttled_value = max_value + log10(-(current_iteration - nb_of_iterations))

        # --> Exit program if incorrect settings used
        else:
            sys.exit("Invalid throttle decay function reference")

    else:
        throttled_value = min_value

    return round(throttled_value, 3)


if __name__ == "__main__":
    for i in range(100):
        print(throttle(current_iteration=i,
                       nb_of_iterations=100,
                       max_value=10,
                       min_value=1,
                       direction="down",
                       decay_function=1))
