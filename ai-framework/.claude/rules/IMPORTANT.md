---
description: hlavní pravidla pro práci s AI frameworkem
alwaysApply: true
---

# Práce se soubory
- **Ověřuj cesty**: Před vytvářením/přesouváním souborů vždy použij `ls`/`dir` v kořenovém adresáři repozitáře
- **Znovu načti před úpravou**: Před úpravou soubor vždy bezprostředně znovu načti, abys zachytil případné ruční změny od uživatele.
- **Pracovní prostor (Workspace)**: Pro všechny dočasné soubory a předávky s dalšími agenty používej výhradně adresář `workspace/`.
- **Relativní odkazy**: V markdownu používej relativní cesty. Zcela se vyhni absolutním cestám a odkazům typu `file:///`.

# Kontext a rozsah
- **Primární kontext**: Řiď se primárně kontextem v AGENTS.md, MY_CONTEXT.md, `projekty/` a `knowledge-base/`.

# Komunikace
- **Ptej se na upřesnění**: Pokud jsou požadavky nejednoznačné nebo si nejsi jistý, jak pokračovat, okamžitě se zastav a zeptej se uživatele. Nikdy nehádej a nedomýšlej si zadání.
- **Podstata před chválou**: Zcela vynech komplimenty a zdvořilostní fráze. Přistupuj k řešení kriticky, zpochybňuj předpoklady a neboj se nabídnout protiargumenty nebo poukázat na rizika.
- **Informační hustota**: Udržuj odpovědi co nejstručnější a maximálně informačně hutné. Vyhýbej se konverzační vatě.