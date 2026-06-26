use serde::{Deserialize, Serialize};
use uuid::Uuid;

// Pevně definovaný tvar lokality z LLM pro validaci schématu (Serde)
#[derive(Debug, Serialize, Deserialize)]
pub struct LlmLocationInput {
    pub title: String,
    pub description: String,
    pub latitude: f64,
    pub longitude: f64,
    pub theme: String,
}

pub struct InputGuardrail;

impl InputGuardrail {
    /// Hlavní metoda, která spustí všechny vstupní kontroly.
    /// Pokud data projdou, vrátí true.
    pub fn validate_incoming_location(&self, location: &LlmLocationInput) -> bool {
        if !self.validate_schema(location) { return false; }
        if !self.check_geofencing(location.latitude, location.longitude) { return false; }
        if !self.sanitize_content(&location.description) { return false; }
        
        true
    }

    /// Kontrola, zda jsou přítomna všechna povinná pole a mají správný formát
    fn validate_schema(&self, _location: &LlmLocationInput) -> bool {
        // Serde řeší základy automaticky při deserializaci JSONu, 
        // zde můžete přidat extra logiku (např. minimální délka řetězce).
        todo!("Implementovat dodatečnou validaci délky textů")
    }

    /// Geofencing - Kontrola, zda souřadnice spadají do cílové oblasti (např. ČR/Evropa)
    fn check_geofencing(&self, _lat: f64, _lng: f64) -> bool {
        todo!("Implementovat kontrolu polygonu (např. zda je bod uvnitř ČR)")
    }

    /// Sanitizace - Kontrola škodlivého obsahu (HTML, spam) v textu od LLM
    fn sanitize_content(&self, _text: &str) -> bool {
        todo!("Implementovat detekci HTML tagů nebo zakázaných slov")
    }
}

