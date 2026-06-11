from graph_logic import langgraph_app

# Tato funkce se volá, když chci poslat data do LangGraphu.
def spustit_ai_agentu(dotaz: str) -> str:
    pocatecni_stav = {"user_query": dotaz}
    vysledek = langgraph_app.invoke(pocatecni_stav)
    return vysledek["ai_response"]

# Rychlý test přímo v příkazové řádce
if __name__ == "__main__":
    print("Testuji LangGraph v podadresáři...")
    odpoved = spustit_ai_agentu("Napiš jedno slovo: Test.")
    print("Odpověď:", odpoved)