# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yujo <yujo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/17 13:18:19 by yujo              #+#    #+#              #
#    Updated: 2020/09/17 13:21:22 by yujo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
import sys
from decimal import Decimal


def ft_progress(lst):
    barLength = 20
    block = int(round(barLength*lst))
    x = Decimal.from_float(lst * 100)
    text = "\rPercent: [{0}] ".format(""*block + " "*(barLength-block))
    sys.stdout.write(text + "%d" % x)
    sys.stdout.write("%")
    sys.stdout.flush()


for i in range(100):
    ft_progress(i/100)
    time.sleep(0.1)
