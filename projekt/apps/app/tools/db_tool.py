from tools.guardrails import DestructiveActionGuardrail
import os

# Inicializace guardrailu uvnitř backendu (klíč se načítá bezpečně z prostředí)
SECRET_KEY = os.getenv("ADMIN_SECRET_KEY", "provizorni_tajne_heslo")
db_guardrail = DestructiveActionGuardrail(admin_secret_key=SECRET_KEY)

def execute_database_command(llm_payload: dict, admin_token: str = None):
    """
    Tato funkce volá LLM orchestrátor.
    LLM dodává 'llm_payload', ale 'admin_token'
    může přijít pouze z legitimního frontendového formuláře od admina.
    """

    # KROK 1: Kontrola guardrailem
    verification_result = db_guardrail.verify_and_execute(llm_payload, user_confirmation_token=admin_token)

    # Pokud guardrail vrátil chybu (obsahuje slovo CHYBA), nepokračujeme dál k DB
    if "CHYBA" in verification_result:
        return verification_result  # Vrátíme LLM informaci o zablokování

    # KROK 2: Skutečné provedení (pokud guardrail akci schválil)
    # zde by byl reálný kód: db.execute(llm_payload['command'])
    return "Akce byla úspěšně vykonána na databázi."
