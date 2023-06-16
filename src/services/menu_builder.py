import pandas as pd

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str):
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    def get_main_menu(self, restriction=None) -> pd.DataFrame:
        # "dish_name", "ingredients", "price", "restrictions"
        if restriction:
            filtered_dishes = [
                dish
                for dish in self.menu_data.dishes
                if restriction not in dish.get_restrictions()
            ]
        else:
            filtered_dishes = self.menu_data.dishes

        main_menu_list = []

        for dish in filtered_dishes:
            if (
                restriction is None
                or restriction not in dish.get_restrictions()
            ):
                main_menu_dict = {}
                main_menu_dict["dish_name"] = dish.name
                main_menu_dict["ingredients"] = list(dish.get_ingredients())
                main_menu_dict["price"] = dish.price
                main_menu_dict["restrictions"] = list(dish.get_restrictions())
                main_menu_list.append(main_menu_dict)

        return pd.DataFrame(main_menu_list)
