"""A Python calculator"""
import sys

command = sys.argv[1]
numbers = [float(a) for a in sys.argv[2:]]

if command == 'add':
    print sum(numbers)

elif command == 'multiply':
    product = 1
    for num in numbers:
        product *= num
    print product
