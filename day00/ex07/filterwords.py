# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yujo <yujo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/17 10:19:19 by yujo              #+#    #+#              #
#    Updated: 2020/09/17 11:24:23 by yujo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if (len(sys.argv) != 3):
    print("ERROR")
    sys.exit()

try:
    values = sys.argv[1].replace(".", "").replace(",", "").split(' ')
    length = int(sys.argv[2])
except:
    print('ERROR')
    sys.exit()

arr = []

for value in values:
    if (len(value) > length):
        arr.append(value)

print(arr)
sys.exit()
