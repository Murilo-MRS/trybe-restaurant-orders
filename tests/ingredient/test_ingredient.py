from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_meat = Ingredient("carne")
    ingredient_1 = Ingredient("carne")
    ingredient_2 = Ingredient("carne")
    ingredient_3 = Ingredient("ovo")

    assert ingredient_meat.name == "carne"
    assert ingredient_meat.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
    assert repr(ingredient_meat) == "Ingredient('carne')"
    assert ingredient_1 == ingredient_2
    assert ingredient_1 != ingredient_3
    assert hash(ingredient_1) == hash(ingredient_2)
    assert hash(ingredient_1) != hash(ingredient_3)
