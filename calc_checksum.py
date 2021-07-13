#!/usr/bin/python
# This script calculates the checksum of a given pin code

pin = 1553778
pin_arr = [int(x) for x in str(pin)] # Result: [1, 5, 5, 3, 7, 7, 8]
sum_odd_pos = pin_arr[1] + pin_arr[3] + pin_arr[5]
sum_even_pos = 3 * (pin_arr[0] + pin_arr[2] + pin_arr[4] + pin_arr[6])
sum_total = sum_odd_pos + sum_even_pos
checksum = 10 - (sum_total % 10)
print('Checksum of {} is {}'.format(pin, 0 if checksum == 10 else checksum)) # Checksum of 1553778 is 2
