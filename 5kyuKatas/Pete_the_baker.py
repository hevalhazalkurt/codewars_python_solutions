
def cakes(recipe, available):
    return min([available[i] // recipe[i] if i in available else 0 for i in recipe])
