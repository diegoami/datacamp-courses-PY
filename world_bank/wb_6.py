
from world_bank.wb_c import *
# Open a connection to the file
with open('world_dev_ind.csv') as file:
    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))
