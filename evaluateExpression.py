import unittest

def evaluteString(input):
    """
    Recursviely evaluating a expression containing only positive integers
    and '+' to use the correct operand.
    We want to achieve 2+3+4 to equal 9.
    """
    # A Base case is presented where we use an if statement to show '+' in an input
    if '+' not in input:
        return int(input) # we return that input that the user created as an integer of course
    
    # We developr our recursive case here
    index = len(input) - 1  # whatever the user input is it will be subtracted by 1
    while input[input] != '+': # We create a loop 
        index -= 1 

    left_part_of_expression = input[:index]
    right_number_of_expression = int(input[:index + 1:])

