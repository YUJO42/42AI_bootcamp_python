# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: yujo <yujo@student.42seoul.kr>             +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/09/16 19:08:07 by yujo              #+#    #+#              #
#    Updated: 2020/09/16 22:53:49 by yujo             ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

sandwich = {
    'ingredients': 'ham, bread, cheese, tomatoes',
    'meal': 'lunch',
    'prep_time': 10,
}
cake = {
    'ingredients': 'flour, sugar, eggs',
    'meal': 'dessert',
    'prep_time': 60,
}
salad = {
    'ingredients': 'avocado, arugula, tomatoes, spinach',
    'meal': 'lunch',
    'prep_time': 15,
}
cookbook = {
    "sandwich": sandwich,
    "cake": cake,
    "salad": salad,
}


def print_recipe(name):
    if name in cookbook:
        print("\nRecipe for", name.lower())
        print("Ingredients: [" + cookbook[name]['ingredients'] + "]")
        print("To be eaten for", cookbook[name]['meal'])
        print("take", cookbook[name]['prep_time'], "minutes of cooking")
    else:
        print("This recipe is not registered in the Cookbook.")


def add_recipe(name, ingredients, meal, prep_time):
    print('\n')
    recipe = {name: {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }}
    cookbook.update(recipe)
    print('success add', name, 'recipe.')


def remove_recipe(name):
    print('\n')
    if name in cookbook:
        cookbook.pop(name)
        print(name + "`s recipe removed.")
    else:
        print("This recipe is not registered in the Cookbook.")


def print_all_recipe():
    for key in cookbook.keys():
        print_recipe(key)


while (1):
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")
    number = input()
    if number == '1':
        print('Please enter the recipe\'s name : ')
        name = input()
        print('Please enter the recipe\'s Ingredients list : ')
        ingredients = input()
        print('Please enter the recipe\'s meal : ')
        meal = input()
        print('Please enter the recipe\'s prep time : ')
        prep_time = input()
        add_recipe(name, ingredients, meal, prep_time)
        print('\n')
    elif number == '2':
        print('Please enter the recipe\'s name to remove : ')
        name = input()
        remove_recipe(name)
        print('\n')
    elif number == '3':
        print('Please enter the recipe\'s name to get its details : ')
        name = input()
        print_recipe(name)
        print('\n')
    elif number == '4':
        print_all_recipe()
        print('\n')
    elif number == '5':
        print('Cookbook closed.')
        sys.exit()
    else:
        print('This option does not exist, please type the corresponding number.')
        print('To exit, enter 5')
