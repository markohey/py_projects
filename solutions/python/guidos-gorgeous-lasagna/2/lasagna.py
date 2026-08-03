"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40 # minutes

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the time needed to prepare layers.
    
    :param number of layers: int - number of layers to prepare.
    :return: int - time required to prepare previously specified number of lasagna layers.
    
    Function that calculates the amount of time needed to prepare a certain number of
    layers for a lasagna."""
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed time in minutes of baking a lasagna.
    
    :param number_of_layers: int - number of layers to prepare.
    :param elapsed_bake_time: int - number of minutes passed by in baking the lasagna.
    :return: int - time passed since start of prepping to bake the lasagna.
    
    Function that calculates the elapsed time since preparation started."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
