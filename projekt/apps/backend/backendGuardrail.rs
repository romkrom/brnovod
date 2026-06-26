use axum::http::StatusCode;
use uuid::Uuid;

pub struct BackendGuardrail;

impl BackendGuardrail {
    /// Ochrana proti scrapování databáze (Rate Limiting)
    /// Vrací StatusCode::TOO_MANY_REQUESTS, pokud IP překročila limit
    pub async fn check_rate_limit(&self, _client_ip: &str) -> Result<(), StatusCode> {
        // Zde by se typicky kontrolovala Redis databáze na počet požadavků za minutu
        todo!("Implementovat kontrolu počtu požadavků v Redis pro danou IP")
    }

    /// Kontrola přístupových práv ke sdílenému seznamu (Access Control)
    /// Vrací anonymní NOT_FOUND, pokud uživatel nemá právo seznam vidět
    pub async fn verify_list_access(
        &self, 
        _list_id: Uuid, 
        _requesting_user_id: Option<Uuid>
    ) -> Result<(), StatusCode> {
        // 1. Načíst seznam z DB
        // 2. Pokud is_public == true -> OK
        // 3. Pokud is_public == false a requesting_user_id odpovídá autorovi -> OK
        // 4. V opačném případě -> StatusCode::NOT_FOUND (anonymní odmítnutí)
        todo!("Implementovat DB dotaz a verifikaci vlastníka seznamu")
    }

    /// Kontrola maximálních limitů zdrojů (Resource Limits)
    /// Zabrání uživateli vytvořit obrovské množství seznamů nebo položek
    pub async fn check_resource_limits(&self, _user_id: Uuid) -> Result<(), StatusCode> {
        // Zde by se spočítal aktuální počet seznamů uživatele v DB
        // Pokud count >= 10, vrátí StatusCode::BAD_REQUEST
        todo!("Implementovat kontrolu maximálního počtu seznamů (max 10)")
    }
}
