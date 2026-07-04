agent_2.pyimport time
import mss
import pyautogui

# Bezpečnostní pojistka: Pokud myší rychle najedeš do levého horního rohu obrazovky (souřadnice 0,0),
# pyautogui okamžitě ukončí program. Skvělé, když se AI zblázní a začne klikat všude možně.
pyautogui.FAILSAFE = True

def agent_loop():
    print("Spouštím agenta... Stiskni Ctrl+C v terminálu pro ukončení.")
    
    with mss.mss() as sct:
        # Získání primárního monitoru (0 je obvykle "all monitors", 1 je první hlavní monitor)
        monitor = sct.monitors[1]
        width = monitor["width"]   # např. 1920
        height = monitor["height"] # např. 1080
        
        while True: # Opravdová smyčka, která běží dokola
            try:
                print("\n--- NOVÝ KROK AGENTA ---")
                
                # 1. OČI: Udělej screenshot
                # sct.shot() ukládá soubor na disk. Pro loop je lepší grab(), 
                # ale pro ukázku sct.shot funguje taky. Vytvoří se soubor 'current_screen.png'.
                sct.shot(output="current_screen.png")
                print(f"Screenshot uložen. Rozlišení obrazovky: {width}x{height}")
                
                # 2. MODEL (Simulace): Tady v budoucnu bude API volání (např. OpenAI/Anthropic)
                # Model dostane obrázek 'current_screen.png', šířku a výšku.
                # Simulujeme, že model vrátil souřadnice v procentech a akci:
                model_pct_x = 0.30  # 30% zleva
                model_pct_y = 0.50  # 50% shora
                action = "right_click"
                
                # Přepočet na pixely (zaokrouhlujeme na celá čísla, pixely nemají desetinná místa)
                target_x = int(width * model_pct_x)
                target_y = int(height * model_pct_y)
                
                print(f"Model se rozhodl provést: {action} na souřadnicích [{target_x}, {target_y}]")
                
                # 3. RUKA: Vykonání příkazu
                if action == "right_click":
                    pyautogui.moveTo(target_x, target_y, duration=0.5) 
                    pyautogui.click(button='right')
                elif action == "click":
                    pyautogui.moveTo(target_x, target_y, duration=0.5)
                    pyautogui.click(button='left')
                    
                # 4. PAUZA: Důležité! Dává systému čas vykreslit to, co se stalo (např. otevření menu)
                # Bez pauzy by další screenshot mohl vzniknout dřív, než se menu stihne objevit.
                time.sleep(2.0)
                
            except KeyboardInterrupt:
                print("\nAgent byl ručně ukončen uživatelem.")
                break
            except Exception as e:
                print(f"Došlo k chybě: {e}")
                break

# Spuštění smyčky
if __name__ == "__main__":
    agent_loop()
