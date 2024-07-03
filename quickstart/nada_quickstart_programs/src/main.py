from nada_dsl import *

def nada_main():
    # Define the party involved in the computation
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")

    # Define secret inputs from the party
    my_int1 = SecretInteger(Input(name="my_int1", party=party1))
    my_int2 = SecretInteger(Input(name="my_int2", party=party1))
    my_int3 = SecretInteger(Input(name="my_int3", party=party1))
    my_int4 = SecretInteger(Input(name="my_int4", party=party1))

    # Perform a series of operations
    add_result1 = my_int1 + my_int2  # Addition
    multiply_result1 = add_result1 * my_int3  # Multiplication
    subtract_result1 = multiply_result1 - my_int2  # Subtraction

    add_result2 = my_int3 + my_int4  # Addition
    multiply_result2 = add_result2 * my_int1  # Multiplication
    subtract_result2 = multiply_result2 - my_int4  # Subtraction

  


    final_result1 = subtract_result1   
    final_result2 = subtract_result2 

    

    # Output the results to the same party
    return [
        Output(final_result1, "final_result1_output", party1),
        Output(final_result2, "final_result2_output", party1),
        
    ]

# Execute the main function to run the NADA program
nada_main()

