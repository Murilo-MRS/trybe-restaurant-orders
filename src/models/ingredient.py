from enum import Enum


class Restriction(Enum):
    ANIMAL_DERIVED = "ANIMAL_DERIVED"
    ANIMAL_MEAT = "ANIMAL_MEAT"
    SEAFOOD = "SEAFOOD"
    LACTOSE = "LACTOSE"
    GLUTEN = "GLUTEN"

    def __eq__(self, __o: object) -> bool:
        return repr(self) == repr(__o)

    def __hash__(self) -> int:
        return hash(repr(self))


def restriction_map():
    return {
        "queijo mussarela": {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED},
        "farinha": {Restriction.GLUTEN},
        "bacon": {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED},
        "manteiga": {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED},
        "caldo de carne": {Restriction.ANIMAL_DERIVED},
        "camarão": {
            Restriction.ANIMAL_MEAT,
            Restriction.SEAFOOD,
            Restriction.ANIMAL_DERIVED,
        },
        "carne": {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED},
        "creme de leite": {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED},
        "frango": {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED},
        "ovo": {Restriction.ANIMAL_DERIVED},
        "queijo gorgonzola": {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED},
        "salmão": {
            Restriction.ANIMAL_MEAT,
            Restriction.SEAFOOD,
            Restriction.ANIMAL_DERIVED,
        },
        "presunto": {
            Restriction.ANIMAL_MEAT,
            Restriction.ANIMAL_DERIVED,
        },
        "queijo parmesão": {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED},
        "queijo provolone": {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED},
        "massa de lasanha": {Restriction.LACTOSE, Restriction.GLUTEN},
        "massa de ravioli": {Restriction.LACTOSE, Restriction.GLUTEN},
    }


class Ingredient:
    def __init__(self, name: str) -> None:
        self.name = name
        self.restrictions = restriction_map().get(name, set())

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other: object) -> bool:
        return repr(self) == repr(other)

    def __repr__(self) -> str:
        return f"Ingredient('{self.name}')"
