from fastapi import FastAPI, HTTPException, Query, status

from models.ingredient import Restriction
from services.menu_builder import MenuBuilder

app = FastAPI(title="Restaurante Chapa Quente")
menu_builder = MenuBuilder()


restriction_options = {k: {"value": k} for k in Restriction._member_names_}


@app.get("/", tags=["menu"])
def get_menu(
    restriction: str = Query(default="", examples=restriction_options)
):
    return menu_builder.get_main_menu(
        restriction=Restriction._member_map_.get(restriction)
    ).to_dict(orient="records")


@app.post("/order", tags=["menu"], status_code=status.HTTP_201_CREATED)
def make_dish_order(dish_name: str):
    try:
        menu_builder.make_order(dish_name)
    except ValueError as err:
        if str(err) == "Dish does not exist":
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(err),
            )
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Dish can't be prepared due to missing ingredients",
        )
