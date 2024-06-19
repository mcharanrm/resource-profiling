# This script basically does one simple thing ...
# Generates meaningless synthetic data and keeps it the memory. 


# We should expect to see while profiling the resource utilization/
# 1 processor (core) utilization of Compute power 
# 1GiB utilization of Memory Power


#with open('a.log', 'w') as file_des:
#    for item in range(1024 * 1024):
#        file_des.write('c' * 1024 + '\n')

import time

synthetic_data = [ 'c' * 10000 + '\n' for item in range(1024 * 1024) ]
counter = 0

while True:
    counter += 1
    print(f'Entered infinite loop ... Seconds elapsed {counter}')
