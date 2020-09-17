# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yujo <yujo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/17 12:54:29 by yujo              #+#    #+#              #
#    Updated: 2020/09/17 13:18:23 by yujo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
from random import randint

print('This is an interactive guessing game!')
print('You have to enter a number between 1 and 99 to find out the secret number.')
print('Type "exit" to end the game.')
print('Good luck!\n')

answer = randint(1, 99)

count = 0
while (1):
    print("What's your guess between 1 and 99?")
    count += 1
    user_input = input()

    if user_input == '':
        print('Good Bye!')
        sys.exit()

    try:
        user_input = int(user_input)
    except:
        print("That's not a number.")
        continue

    if (user_input > answer):
        print('Too high!')
    elif (user_input < answer):
        print('Too low!')
    elif (user_input == answer):
        if (answer == 42):
            print(
                'The answer to the ultimate question of life, the universe and everything is 42.')
        if (count == 1):
            print('Congratulations! You got it on your first try!')
        print('Congratulations, you\'ve got it!')
        print('You won in', count, 'attepts!')
        sys.exit()
