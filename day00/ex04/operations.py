# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yujo <yujo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/16 11:21:10 by yujo              #+#    #+#              #
#    Updated: 2020/09/16 20:45:54 by yujo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def error_msg():
    print('Usage: python operations.py <number1> <number2>')
    print('Example:')
    print('     python operations.py 10 3')


if len(sys.argv) < 3:
    error_msg()
    sys.exit()

if len(sys.argv) > 3:
    print('InputError: too many arguments')
    error_msg()
    sys.exit()

try:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
except:
    print('InputError : only numbers')
    error_msg()
    sys.exit()

print("Sum        :", a + b)
print('Difference :', a - b)
print('Product    :', a * b)

if (b == 0):
    print('Quotient   : ERROR (div by zero)')
    print('Remainder  : ERROR (modulo by zero)')
else:
    print('Quotient   :',  a / b)
    print('Remainder  :',  a % b)
