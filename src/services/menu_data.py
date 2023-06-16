# import csv
from src.models.dish import Dish
import pandas as pd
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.load(source_path)

    def load(self, path):
        data_csv = pd.DataFrame(pd.read_csv(path))
        dishes = {}
        # print(dict(data_csv.iloc[0]))
        for index in range(data_csv.shape[0]):
            # print(data_csv["dish"][index], data_csv["price"][index])
            dish_to_add = Dish(
                data_csv["dish"][index], float(data_csv["price"][index])
            )
            ingredient_to_add = Ingredient(data_csv["ingredient"][index])

            if dish_to_add.name in dishes:
                dishes[dish_to_add.name].add_ingredient_dependency(
                    ingredient_to_add, int(data_csv["recipe_amount"][index])
                )
                continue

            dish_to_add.add_ingredient_dependency(
                ingredient_to_add, int(data_csv["recipe_amount"][index])
            )
            dishes[dish_to_add.name] = dish_to_add

        for dish in dishes.values():
            self.dishes.add(dish)
