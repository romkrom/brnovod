export interface FeedbackData {
  locationId: string;
  traceId: string;       // ID spojené s konkrétním vyhledáním v Langfuse/DB
  rating: 'up' | 'down'; // Palec nahoru / dolů
  comment?: string;      // Volitelný komentář od uživatele
}

export class FeedbackService {
  private static apiEndpoint = '/api/v1/feedback';

  public static async submitFeedback(data: FeedbackData): Promise<boolean> {
    console.log(`[Feedback] Uživatel hodnotí lokalitu ${data.locationId} jako ${data.rating}`);
    
    try {
      // V produkci se pošle na Axum backend, který data uloží do Postgresu
      // a zároveň je může napárovat do Langfuse pro analýzu špatných odpovědí
      /*
      const response = await fetch(this.apiEndpoint, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
      });
      return response.ok;
      */
      return true;
    } catch (error) {
      console.error("Nepodařilo se odeslat feedback uživatele:", error);
      return false;
    }
  }
}
