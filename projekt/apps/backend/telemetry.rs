use tracing_subscriber::{layer::SubscriberExt, util::SubscriberInitExt};
use std::time::Instant;
use axum::{middleware::Next, response::Response, extract::Request};

/// Inicializace logování a tracingu
pub fn init_telemetry() {
    tracing_subscriber::registry()
        .with(
            tracing_subscriber::EnvFilter::try_from_default_env()
                .unwrap_or_else(|_| "info,axum_backend=debug".into()),
        )
        .with(tracing_subscriber::fmt::layer().json()) // JSON formát
        .init();
}

/// Struktura pro držení aplikačních metrik (např. pro Prometheus)
#[derive(Clone)]
pub struct MetricsCollector {
    // Zde bys měl např. prometheus::Counter nebo u64 atomické proměnné
}

impl MetricsCollector {
    pub fn new() -> Self {
        Self {}
    }

    pub fn track_db_connection_pool(&self, active: u32, idle: u32) {
        tracing::info!(active_connections = active, idle_connections = idle, "DB Pool Status");
    }
}

/// Middleware pro měření RED metod (Rate, Errors, Duration)
pub async fn track_api_performance(req: Request, next: Next) -> Response {
    let start = Instant::now();
    let path = req.uri().path().to_string();
    let method = req.method().to_string();

    let response = next.run(req).await;

    let duration = start.elapsed().as_secs_f64();
    let status = response.status().as_u16();

    // Zalogování s užitečnými strukturovanými daty
    tracing::info!(
        path = %path,
        method = %method,
        status = status,
        duration_sec = duration,
        "API Request processed"
    );

    response
}
