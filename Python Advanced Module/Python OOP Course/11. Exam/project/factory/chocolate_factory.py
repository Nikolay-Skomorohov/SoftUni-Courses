from project.factory.factory import Factory


class ChocolateFactory(Factory):
    def __init__(self, name, capacity):
        super().__init__(name, capacity)
        self.recipes = {}
        self.products = {}

    def add_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in ["white chocolate", "dark chocolate", "milk chocolate", "sugar"]:
            if self.can_add(quantity):
                if ingredient_type in self.ingredients.keys():
                    self.ingredients[ingredient_type] += quantity
                else:
                    self.ingredients[ingredient_type] = quantity
            else:
                raise ValueError("Not enough space in factory")
        else:
            raise TypeError(f"Ingredient of type {ingredient_type} not allowed in {self.__class__.__name__}")

    def remove_ingredient(self, ingredient_type: str, quantity: int):
        if ingredient_type in self.ingredients.keys():
            if self.ingredients[ingredient_type] >= quantity:
                self.ingredients[ingredient_type] -= quantity
            else:
                raise ValueError("Ingredient quantity cannot be less than zero")
        else:
            raise KeyError("No such product in the factory")

    def add_recipe(self, recipe_name: str, recipe: dict):
        if recipe_name in self.recipes.keys():
            self.recipes[recipe_name] = recipe[recipe_name]
        else:
            self.recipes[recipe_name] = recipe[recipe_name]

    def make_chocolate(self, recipe_name: str, storage=False):
        if storage:
            if recipe_name in self.recipes.keys():
                if recipe_name in self.products.keys():
                    for ingr, quan in self.recipes[recipe_name].items():
                        self.ingredients[ingr] -= quan
                    return recipe_name, self.recipes[recipe_name]
            else:
                raise TypeError("No such recipe")
        else:
            if recipe_name in self.recipes.keys():
                if recipe_name in self.products.keys():
                    self.products[recipe_name] += self.recipes[recipe_name]
                else:
                    self.products[recipe_name] = self.recipes[recipe_name]
                for ingr, quan in self.recipes[recipe_name].items():
                    self.ingredients[ingr] -= quan
            else:
                raise TypeError("No such recipe")
