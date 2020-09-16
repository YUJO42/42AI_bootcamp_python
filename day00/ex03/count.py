# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yujo <yujo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/16 10:56:19 by yujo              #+#    #+#              #
#    Updated: 2020/09/16 11:19:26 by yujo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def text_analyzer(str):
    total_count = 0
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    
    for char in str:
        if (char.isupper()):
            upper_count += 1
        elif (char.islower()):
            lower_count += 1
        elif (char == '.'):
            punctuation_count += 1
        elif (char == ' '):
            space_count += 1
        total_count += 1
    print('The text contains', total_count, 'characters:')
    print('-', upper_count, 'upper letters')
    print('-', lower_count, 'lower letters')
    print('-', punctuation_count, 'punctuation marks')
    print('-', space_count, 'spaces')
    


