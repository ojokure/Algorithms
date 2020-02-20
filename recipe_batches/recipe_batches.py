#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):

  # set our minimum ratio to infinity
    min_ratio = math.inf
    print(min_ratio)

  # use a for loop to extract the ingredients from the recipe
    for ingredient, amount in recipe.items():
        print(ingredient, amount)
        # and check if its ingredients is/is not in ingredients(2nd arg)
        if ingredient not in ingredients:
            # return 0 if not in
            return 0
  # ratio should be ingredients[i]/amout (of recipe)
        ratio = math.floor(ingredients[ingredient] / amount)
        print(ratio, ingredients[ingredient])

  # compare min_ratio to the ingredient/amount ratio if ratio is less than min_ratio
        if ratio < min_ratio:
            # set min_ratio to current ratio
            min_ratio = ratio
            print(min_ratio)

 # return min_ratio
    return min_ratio


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
