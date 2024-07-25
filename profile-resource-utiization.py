# This script basically does one simple thing ...
# Generates meaningless synthetic data and keeps it the memory. 


# We should expect to see while profiling the resource utilization/
# 1 processor (core) utilization of Compute power 
# 1GiB utilization of Memory Power


#with open('a.log', 'w') as file_des:
#    for item in range(1024 * 1024):
#        file_des.write('c' * 1024 + '\n')

import time

# Drives memory utilization
#synthetic_data = [ 'c' * 1022 + '\n' for item in range(1024 * 1024) ]
data = bytearray(1024 * 100)


# Drives CPU Utilization
counter = 0

while True:
    counter += 1

    # Drives FileSystem Utilization by writing lot of lines to STDOUT
    print(f'Entered infinite loop ... Counter is at: {counter}')
