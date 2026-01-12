def evaluateString(input):
    """
    Recursviely evaluating a expression containing only positive integers
    and '+' to use the correct operand.
    We want to achieve 2+3+4 to equal 9.
    """
    # A Base case is presented where we use an if statement to show '+' in an input
    if '+' not in input:
        return int(input) # we return that input that the user created as an integer of course
    
    # We developr our recursive case here
    index = len(input) - 1  # whatever the user input is it will be subtracted by 1, so we have a pointer that starts at the last character
    while input[index] != '+': # We create a loop and it will continue to move left till '+' is found 
        index -= 1 

    # Overall the loop goes from right to left untill it finds that addition operand and then splits the code into smaller recursive sub problems
    left_part_of_expression = input[:index] # just simple code for everything before the plus sign
    right_number_of_expression = int(input[index + 1:]) # any number that is after the plus sign

    return evaluateString(left_part_of_expression) + right_number_of_expression # Just a return to get that crrect algorithim answer