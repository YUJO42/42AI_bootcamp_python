# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whois.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yujo <yujo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/15 20:51:00 by yujo              #+#    #+#              #
#    Updated: 2020/09/15 21:18:30 by yujo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) != 2 :
    sys.exit()

number = int(float(sys.argv[1]))

if (type(number) is not int) :
    print("ERROR")
    sys.exit()

if (number is 0):
    print("I`m Zero.")
    sys.exit()
elif (number % 2 == 0):
    print("I`m Even.")
    sys.exit()
    
print("I`m Odd.")
sys.exit()