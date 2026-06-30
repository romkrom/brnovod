import uuid
import time
import logging

class BackgroundAIPipelineTracker:
    def __init__(self, batch_name: str, model_name: str):
        self.batch_name = batch_name
        self.model_name = model_name
        self.trace_id = str(uuid.uuid4()) # Unikátní ID pro Langfuse a DB
        self.tool_usage = {}
        self.start_time = time.time()

    def track_tool(self, tool_name: str):
        """Sleduje, kolikrát autonomní model použil jaký tool při hledání"""
        self.tool_usage[tool_name] = self.tool_usage.get(tool_name, 0) + 1

    def save_to_db_payload(self, location_data: dict) -> dict:
        """Přibalí k lokalitě metadata pro pozdější kontrolu kvality uživatelem"""
        location_data["ai_model_version"] = self.model_name
        location_data["ai_trace_id"] = self.trace_id
        return location_data

    def flush_pipeline_metrics(self, locations_found: int):
        """Na konci běhu zapíše celkové metriky (např. do Langfuse/Prometheus)"""
        duration = time.time() - self.start_time
        metrics = {
            "trace_id": self.trace_id,
            "batch": self.batch_name,
            "model": self.model_name,
            "duration_seconds": round(duration, 2),
            "locations_found": locations_found,
            "tools_used": self.tool_usage
        }
        # Tady se data odešlou do monitoringu
        logging.info(f"[BATCH DONE] Metriky zapsány: {metrics}")

# Použití na pozadí:
# pipeline = BackgroundAIPipelineTracker("nightly_scan", "mistral-7b-v1")
# ... model hledá ...
# pipeline.track_tool("wikipedia_scrape")
# data_pro_db = pipeline.save_to_db_payload({"name": "Skvělé místo", "tags": ["klid"]})
# ... uložíš do Postgresu ...
# pipeline.flush_pipeline_metrics(locations_found=1)
# Tímto způsobem se oddělí těžkopádný běh AI na pozadí od bleskové odezvy pro uživatele, ale zároveň se neztratí možnost zjistit, který krok modelu na pozadí způsobil, že uživatel dal o tři dny později palec dolů.
