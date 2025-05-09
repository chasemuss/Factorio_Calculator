import toml

with open('./Data/recipes.toml', 'r') as tomlin:
    all_recipes = toml.loads(tomlin.read())

print(all_recipes)