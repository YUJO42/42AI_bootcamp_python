# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yujo <yujo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/16 13:27:46 by yujo              #+#    #+#              #
#    Updated: 2020/09/16 20:45:48 by yujo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for key in languages.keys():
    print(key, "was created by", languages[key])


# Expected answer

# Python was created by Guido van Rossum
# Ruby was created by Yukihiro Matsumoto
# PHP was created by Rasmus Lerdorf
