from google.genai import Client

client = Client()

def suggest_dishes(cuisine):

    prompt = f"""
    Suggest 20 popular dishes from {cuisine} cuisine.
    Only return a list of dish names.
    """

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt
    )

    dishes = response.text.split("\n")

    return dishes