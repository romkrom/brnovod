Brnovod PRD
Status: Předběžný návrh Poslední aktualizace: 2026-05-28

1. Shrnutí
Brnovod je web-first aplikace pro poskytování informací o místech (cílech) v Brně a okolí. Získávání a vyhledávání informací o místech je postaveno na základě AI asistence. Prezentace lokalit je zobrazena ve vektorovém formátu s možností přibližování a filtrování.
První implementační řez se zaměřuje na webovou aplikaci. Mobilní aplikace zůstává plánovanou budoucí distribucí, kde by způsob zobrazení lokalit měl být stejný.

2. Problém
Většina stránek nebo aplikací přistupuje ke zobrazování lokalit buď jako k přehledu článků v blogu, nebo jako k nepřehledné mapě bodů bez snadného zobrazení podstatných informací. Z toho vyplívá, že výsledný UI musí být co nejjednodušší na zobrazení a ovládání.
Dalším problémem je aktualizace informací, kde lidský faktor v podstatě vždy selhává. Agentem získané informace vždy aktuální a přehledné.

3. Cíle
Zobrazení a filtrování zájmových bodů ve webové aplikaci.
Udržet web jako jednu dynamickou stránku (SPA).
Připravit produkt na vlastního Brnovod AI agenta a napojení na externí coding harnessy.
Umožnit pozdější distribuci jako mobilní aplikaci bez změny formátu a vzhledu zobrazení lokalit.
Podporovat znovupoužitelné komponenty a knihovny.
Poskytnout rozumné výchozí rámování zobrazení lokalit, aby se mohl zobrazovat jak ve webové aplikaci tak v mobilní aplikaci na výšku i na šířku bez nutnosti další konfigurace.
Možnost přeposlat vybrané místo zájmu jinému uživateli jak na webu tak v mobilní aplikaci.
Možnost odkázat na externí mapu ve webové aplikaci a spustit navigaci v mobilu.
Součástí je správa účtů, oprávnění, přihlášení uživatele.
Webové rozhraní (frontend) je ve frameworku Svelte v jazyku Typescript, backend ve frameworku Axum v jazyku Rust, databáze je PostgreSQL.

4. Co není cílem (Non-Goals)
Vytvoření dalšího blogu kudyznudy.cz, nebo mapy jako je google.com/maps.
Server-side AI vyhledávání v prvním řezu.
Pokročilé animační nebo 3D frameworky ve zobrazení lokalit a UI.

5. Cílovka
Uživatelé, kteří chtějí rychle (většinou na poslední chvíli) zobrazit možnosti míst (cílů zájmu), které lze navštívit v konkrétním čase.
Uživatelé k tomu buď použijí web nebo mobil.

6. High-Level User Stories
Vyhledávání míst v širokém okolí s AI a Brnovod agentem a jejich ukládání a následné zobrazení uživateli dle jeho filtrů
Jako uživatel si mohu aktuální mista označovat a uvádět čas plánované návštěvy.
Uživateli se budou zobrazovat místa, kdy se blíží jejich čas a možnost návštěvy, jako signální světýlka s barvou a frekvencí blikání dle blížícího se termínu návštěvy nebo časového rámce doby konání akce.
Jako uživatel vidím jen ty body zájmu, které již nezanikly jak z časového nebo fyzického hlediska.
Jako uživatel mohu v mobilní aplikaci provádět to samé jako ve webové aplikaci.
Jako uživatel si mohu zobrazit vybraná místa zájmu i v seznamu.
Jako uživatel mohu zobrazit webovou stránku i v mobilním telefonu bez mobilní aplikace pomocí prohlížeče se zachováním přehledného uživatelského rozhraní.

Obsah vytvořený agenty a coding harnessy
Jako agent a agent harness mohu vyhledávat lokality na webu, hodnotit jejich aktuálnost a výsledky uložit v předem určeném formátu do databáze přes strukturované rozhraní Brnovodu
Jako agent a agent harness (počítá se s lokálním modelem) mohu vytvořit nebo upravit lokality přes budoucí automatizační napojení se stabilními vstupy a výstupy.
Jako agent a agent harness mohu objevovat nové lokality dle předem stanovených podmínek vyhledávání nastavené vývojářem.

Sdílení
Jako uživatel mohu vybraná místa zájmu přeposílat jinému uživateli. Tyto informace budou viditelné jak ve webové aplikaci, tak v mobilní aplikaci.

Tisk
Jako uživatel si mohu zobrazení lokalit vytisknout.
                                              +
7. Požadavky
Funkční požadavky:
Webová aplikace pro zobrazování, označování a vyhledávání zájmových destinací.
Budoucí mobilní aplikace se stejným produktovým chováním jako webová aplikace.
MVP zatím nepoužívá databázi.
Webová aplikace je spustitelná v běžném prohlížeči.
Přizpůsobitelné rozměry zobrazení lokalit, včetně poměru na výšku.

Prezentační režim:
Automatizační rozhraní pro vyhledání, validaci, uložení a práci s lokalitami v pozdějším řezu.

Nefunkční požadavky:
S nalezeným obsahem o lokalitě musí být zacházeno jako s nedůvěryhodným kódem.
Validace a uložení dat o lokalitách by mělo být deterministické dle předem daných pravidel vytvořených vývojářem.
Automatizační výstupy by tak měly být stabilní a strojově čitelné.

8. UX / User Flow
První spuštění:
Uživatel otevře Brnovod.
Webová aplikace nabídne "zobrazení lokalit" a dostupné možnosti přihlášení/registrace do aplikace.
Uživatel si vybere témata, na základě kterých chce zobrazit lokality. Tyto domény budou předem dané.
Aplikace načte uložená místa zájmu z databáze dle filtrace uživatele.
Aplikace zobrazí aktualizované lokality, když se filtr změní.
Aplikace přidá do zobrazení nové lokality i ve chvíli, kdy se uloží nová místa na základě nálezu pomocí AI. Tyto lokality budou zvýrazněny odlišným signalizačním zobrazením.

Pracovní prostor aplikace:
Vlevo: ovládací prvky pro manipulaci s lokalitami.
Uprostřed: zobrazení lokalit.
Vpravo nahoře: ikony pro přihlášení a registraci.

9. Metriky úspěchu
Uživatel dokáže zobrazit lokality v podstatě okamžitě po zadání předdefinovaných filtrů.
Webová aplikace dokáže zobrazit a vyfiltrovat lokality přes stabilní produktový flow.
Budoucí distribuce mobilní aplikace dokáže nabídnout stejné základní workflow.
Agent dokáže v pozdějším řezu prohledat web, nalézt informace o lokalitě a ty uložit přes automatizační rozhraní.
Tisk zobrazení lokalit funguje v podporovaných prostředích.
Validace zachytí chybějící informace nebo vadný formát informací o lokalitě.

10. Předpoklady a Omezení
Předpoklady:
První implementační řez je web-first.

Omezení:
Pro první řez není vyžadováno server-side AI generování.

11. Klíčová rizika a Otevřené otázky
Rizika:
Pro sdílené odkazy se nesmí používat databázové ID (auto-increment). Odkaz musí obsahovat neuhodnutelný identifikátor (NanoID).
Frontend nikdy nesmí žádat po backendu o všechna data najednou. Vždy je omezen rádiusem nebo tématem.
Tam kde bude dovoleno mazat data, musí být ošetřena všechna související data, které jsou na mazaných datech závislé.
LLM data mazat v žádném případě nemůže. Může je jen označit za neplatné.

Otevřené otázky:
Jaký lokální model použít a jakými daty ho nakrmit?

12. Bezpečnost a legislativa
Ochrana osobních údajů:
Aplikace musí splňovat pravidla GDPR.
Uživatel musí mít možnost trvale smazat svůj účet a všechna svá data (právo na zapomnění).

Řízení přístupu:
Běžný uživatel smí vidět a upravovat pouze svá vlastní data. Neexistuje způsob jak přistupovat k datům cizích uživatelů.
Administrátor systému má přístup do admin panelu, ale nesmí vidět citlivá data uživatelů (např. hesla).

Bezpečnost hesel:
Heslo uživatele musí mít minimálně 8 znaků, obsahovat jedno číslo a jeden speciální znak.
