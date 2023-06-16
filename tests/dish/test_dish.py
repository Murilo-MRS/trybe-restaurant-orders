import pytest
from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    with pytest.raises(TypeError):
        Dish("Lasanha", "one")

    with pytest.raises(ValueError):
        Dish("Lasanha", -23.0)

    dish_lasagna = Dish("Lasanha", 23.0)

    assert dish_lasagna.name == "Lasanha"
    assert dish_lasagna.price == 23.0
    assert dish_lasagna.recipe == {}
    assert repr(dish_lasagna) == "Dish('Lasanha', R$23.00)"

    ingredient_1 = Ingredient("massa de lasanha")
    ingredient_2 = Ingredient("queijo mussarela")
    ingredient_3 = Ingredient("carne")

    dish_lasagna.add_ingredient_dependency(ingredient_1, 3)
    dish_lasagna.add_ingredient_dependency(ingredient_2, 20)
    dish_lasagna.add_ingredient_dependency(ingredient_3, 10)

    assert dish_lasagna.get_ingredients() == {
        ingredient_1,
        ingredient_2,
        ingredient_3,
    }
    assert dish_lasagna.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
        Restriction.GLUTEN,
        Restriction.LACTOSE,
    }

    dish_lasagna_2 = Dish("Lasanha", 23.0)
    assert dish_lasagna == dish_lasagna_2
    assert hash(dish_lasagna) == hash(dish_lasagna_2)

    dish_lasagna_3 = Dish("Lasanha", 24.0)
    assert dish_lasagna != dish_lasagna_3
    assert hash(dish_lasagna) != hash(dish_lasagna_3)
