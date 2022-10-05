#########################################################################################################
#
# SOL - Sorren's Orbital Library 
#
# Author:  Sorren Chandra 
# Date:    10/02/2022
# Contact: sorrenchandra@gmail.com
#
#########################################################################################################

########################################## Exceptions ###################################################
#
# Module to handle custom exceptions
#
#########################################################################################################


# Define Custom Exceptions
class NOT_NUMPY_ARRAY(Exception):
    # raised whenerver a supplied input is not a numpy array
    pass

class MAX_ITERATIONS_REACHED(Exception):
    # raised whenever maximum iteration counter is reached
    pass

class BAD_INPUT(Exception):
    # Raised whenever a function recieves an incorrect input
    pass