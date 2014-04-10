#!/usr/bin/env python
"""A Python calculator"""
import sys

command = sys.argv[1]
numbers = [float(a) for a in sys.argv[2:]]
a = float(sys.argv[2])
b = float(sys.argv[3])


if command == 'add':
    print sum(numbers)

elif command == 'multiply':
    product = 1
    for num in numbers:
        product *= num
    print product
elif command == 'divide':
    div = 1
    if b != 0: 
        div = a/b
        print div 

