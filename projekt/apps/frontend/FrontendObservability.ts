export class FrontendObservability {
    private static instance: FrontendObservability;
    private backendUrl: string = '/api/v1/telemetry'; // Upraví se dle potřeby

    private constructor() {
        this.setupGlobalErrorHandling();
    }

    public static getInstance(): FrontendObservability {
        if (!FrontendObservability.instance) {
            FrontendObservability.instance = new FrontendObservability();
        }
        return FrontendObservability.instance;
    }

    // Měření rychlosti akcí (např. načtení lokalit)
    public trackPerformance(metricName: string, durationMs: number, tags: Record<string, string> = {}) {
        const payload = { metricName, durationMs, tags, timestamp: new Date().toISOString() };
        this.sendTelemetry('metric', payload);
    }

    // Logování chyb
    public logError(message: string, error?: any, context: Record<string, string> = {}) {
        cost payload = {
            message,
            error: error?.toString() || 'Unknown Error',
            stack: error?.stack,
            context,
            timestamp: new Date().toISOString()
        };
        this.sendTelemetry('error', payload);
    }

    private setupGlobalErrorHandling() {
        window.addEventListener('error', (event) => {
            this.logError('Unhandle Exception', event.error);
        });

        window.addEventListener('unhandledrejection', (event) => {
            this.logError('Unhandled Promise Rejection', event.reason);
        });
    }

    private async sendTelemetry(type: 'metric' | 'error', data: any) {
        // V produkci odesílat dávkově (batching) nebo přes navigator.sendBeacon
        try {
            await fetch(`${this.backendUrl}/${type}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data),
            });
        } catch (e) {
            console.error('Failed to send telemetry:', e);
        }
    }
}
