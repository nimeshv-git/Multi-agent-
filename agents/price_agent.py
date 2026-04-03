from pipelines.rag_pipeline import run_rag

def get_average_price(dish):

    question = f"What is the average price of {dish}?"

    answer = run_rag(question)

    return answer