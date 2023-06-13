from numbers import Real
from typing import Dict

from models.ingredient import Ingredient

Recipe = Dict[Ingredient, int]


class Dish:
    def __init__(self, name: str, price: float) -> None:
        self.name = name

        if not isinstance(price, Real):
            raise TypeError("Dish price must be float.")
        if price <= 0:
            raise ValueError("Dish price must be greater then zero.")

        self.price = price
        self.recipe: Recipe = {}

    def __repr__(self) -> str:
        return f"Dish('{self.name}', R${self.price:.2f})"

    def __eq__(self, other) -> bool:
        return self.__repr__() == other.__repr__()

    def __hash__(self) -> int:
        return hash(self.__repr__())

    def add_ingredient_dependency(self, ingredient: Ingredient, amount: int):
        self.recipe[ingredient] = amount

    def get_restrictions(self):
        return set(
            restriction
            for ingredient in self.recipe.keys()
            for restriction in ingredient.restrictions
        )

    def get_ingredients(self):
        return set(self.recipe.keys())
