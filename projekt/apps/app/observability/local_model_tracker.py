import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("LocalLLMOps")

class LocalModelTracker:
    def __init__(self, request_id: str, model_name: str):
        self.request_id = request_id
        self.model_name = model_name
        self.start_time = None
        self.iteration_count = 0
        self.max_iterations = 5  # Ochrana proti zacyklení lokálního modelu

    def increment_iteration(self, tool_name: str = None):
        """Sleduje kroky agenta a chrání před zacyklením"""
        self.iteration_count += 1
        if tool_name:
            logger.info(f"[{self.request_id}] Iterace {self.iteration_count}: Model volá nástroj '{tool_name}'")
        
        if self.iteration_count > self.max_iterations:
            logger.error(f"[{self.request_id}] DETEKCE ZACYKLENÍ! Model překročil limit {self.max_iterations} iterací.")
            raise RuntimeError("Agent loop detected and terminated.")

    def log_generation_speed(self, total_tokens: int, duration_seconds: float):
        """Měří klíčovou metriku lokálních modelů: Tokeny za sekundu (TFT / TPS)"""
        if duration_seconds <= 0: return
        tokens_per_second = total_tokens / duration_seconds
        
        logger.info(
            f"[METRIKA KAPACITY] Model: {self.model_name} | "
            f"Vygenerováno: {total_tokens} tokenů | "
            f"Čas: {round(duration_seconds, 2)}s | "
            f"Rychlost: {round(tokens_per_second, 2)} tok/s"
        )
        
        # Pokud rychlost klesne (např. pod 10 tok/s), dochází VRAM na GPU a systém začal swapovat do běžné RAM, což je bottleneck.

# Příklad použití pipeline:
# tracker = LocalModelTracker("req_001", "llama3-8b-instruct")
# try:
#     tracker.increment_iteration("postgres_search")
#     # ... nějaká práce modelu ...
#     tracker.log_generation_speed(total_tokens=150, duration_seconds=4.2)
# except RuntimeError:
#     # Bezpečné ukončení zaseknutého modelu
