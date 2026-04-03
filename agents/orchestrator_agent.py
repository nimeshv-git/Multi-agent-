from agents.cuisine_agent import suggest_dishes
from agents.image_agent import generate_image
from agents.price_agent import get_average_price
from agents.menu_builder_agent import create_menu


def build_menu(cuisine, selected_dishes):

    menu_data = []

    for dish in selected_dishes:

        image = generate_image(dish)

        price = get_average_price(dish)

        menu_data.append({
            "name": dish,
            "image": image,
            "price": price
        })

    pdf = create_menu(menu_data)

    return pdf