import unittest

def evaluteString(input):
    # A Base case is presented where we use an if statement to show '+' in an input
    if '+' not in input:
        return int(input) # we return that input that the user created as an integer of course
    
    # We developr our recursive case here
