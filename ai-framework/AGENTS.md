# AI Framework (Cursor + Claude)
Jednotný sdílený vstupní bod pro pracovní postupy s podporou umělé inteligence.

## Adresářová struktura
- **`.claude/`**: Zdroj pravdy pro konfiguraci AI (`rules`, `skills`, `agents`, `commands`, `hooks`).
- **`knowledge-base/`**: Referenční dokumentace.
- **`projekty/`**: Adresáře aktivních projektů.
- **`workspace/`**: Přechodné výstupy a předávky mezi agenty.

## Základní pravidla
- **Dodržuj omezení**: Vždy se řiď souborem `.claude/rules/IMPORTANT.md`.
- **Upřednostňuj dovednosti (skills)**: Vždy zkontroluj `.claude/skills/` před improvizací vlastního řešení.
- **Uchovávej předávky**: Ukládej výstupy mezi kroky nebo agenty do `workspace/`.