export class FrontendGuardrail {
    /**
     * Zajišťuje, že se na mapě nebude vykreslovat příliš mnoho bodů najednou.
     * Seskupí blízké body do shluků (clusterů).
     */
    public static clusterMapPoints(points: any[], zoomLevel: number): any[] {
        // V praxi zde zavoláte knihovnu jako supercluster
        // Vstup: 1000 samostatných bodů
        // Výstup: 5 clusterů a 10 samostatných bodů (podle zoomu)
        throw new Error("Metoda clusterMapPoints není implementována.");
    }

    /**
     * Striktní sanitizace HTML. Zamezuje XSS útoku, pokud by popis lokality
     * z DB obsahoval škodlivý <script>.
     */
    public static sanitizeHtmlContent(rawHtml: string): string {
        // V praxi: return DOMPurify.sanitize(rawHtml);
        throw new Error("Metoda sanitizeHtmlContent není implementována.");
    }
}
