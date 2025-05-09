import json

class Recipe:
    def __init__(self, name):
        self.name = name

        found = False
        with open('./Data/recipes.json', 'r') as fin:
            all_recipes = json.loads(fin.read())
            for recipe in all_recipes:
                if recipe != self.name:
                    continue
                self.ingredients = all_recipes[recipe]['Ingredients']
                self.time = all_recipes[recipe]['Time']
        if not found:
            self.new_recipe()

    def new_recipe(self):
        new_recipe = {
            "Ingredients": [],
            "Time": 0
        }
        for x in range(int(input('How many ingredients are in this recipe? '))):
            ingredient = input('Ingredient Name: ')
            amount = input('Ingredient Amount: ')
            new_recipe['Ingredients'].append({
                "Name": ingredient,
                "Amount": amount
            })
        new_recipe['Time'] = int(input('Crafting Time: '))
    
        with open('./Data/recipes.json', 'r') as fin:
            all_recipes = json.loads(fin.read())
        
        all_recipes[self.name] = new_recipe
        
        with open('./Data/recipes.json', 'w') as fout:
            fout.write(json.dumps(all_recipes, indent=4))

