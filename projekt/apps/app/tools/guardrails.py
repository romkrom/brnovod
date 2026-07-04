import os
import secrets
import hmac
import hashlib
from typing import Dict, Any
import pyautogui

class DestructiveActionGuardrail:
    def __init__(self, admin_secret_key: str):
        self.secret_key = admin_secret_key.encode('utf-8')
        # Seznam explicitně zakázaných destruktivních klíčových slov v SQL/příkazech
        self.blacklist = ["DROP TABLE", "DELETE FROM", "rm -rf", "FLUSHALL"]

    def _generate_approval_token(self, action_id: str) -> str:
        """Vygeneruje bezpečný HMAC token pro ověření lidského schválení."""
        return hmac.new(self.secret_key, action_id.encode('utf-8'), hashlib.sha256).hexdigest()

    def verify_and_execute(self, tool_input: Dict[str, Any], user_confirmation_token: str = None) -> str:
        action = tool_input.get("action", "")
        target = tool_input.get("target", "")
        command = tool_input.get("command", "")

        # 1. Analýza rizikovosti (Heuristická kontrola + Blacklist)
        is_destructive = (
            action in ["DELETE", "DROP", "PURGE"] or 
            any(bad_word in command for bad_word in self.blacklist)
        )

        if is_destructive:
            # Generuje unikátní ID akce
            action_id = f"{action}:{target}:{secrets.token_hex(4)}"
            expected_token = self._generate_approval_token(action_id)

            # 2. Pokud chybí token schválení od člověka, akci zablokuje a vyžádá si ho
            if not user_confirmation_token or user_confirmation_token != expected_token:
                # zde bude byl trigger na Slack/Email pro admina
                print(f"[GUARDRAIL ALERT] Detekována destruktivní akce! ID: {action_id}")
                print(f"[ADMIN POTVRZENÍ] Pro schválení použijte token: {expected_token}")
                
                return (
                    f"CHYBA: Akce '{action}' na cíl '{target}' byla zablokována bezpečnostním guardrailem. "
                    f"Jedná se o destruktivní operaci. Vyžaduje se potvrzení administrátora. "
                    f"Zadejte příkaz znovu s platným 'user_confirmation_token' pro Action ID: {action_id}."
                )
            
            # 3. Pokud je token správný, akce projde
            return f"ÚSPĚCH: Destruktivní akce '{action}' byla bezpečně ověřena člověkem a provedena na {target}."
        
        # Bezpečné akce (např. SELECT, READ) projdou bez guardrailu
        return f"ÚSPĚCH: Standardní akce '{action}' byla provedena."


class ToolsGuardrails:
    def __init__(self):
        # Inicializace základního nastavení PyAutoGUI
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0.1
        
        # Paměť pro detekci zacyklení
        self.last_x = None
        self.last_y = None
        self.loop_counter = 0

    def validate_coordinates(self, x, y):
        """Kontrola, zda jsou procentuální souřadnice v rozmezí 0.0 až 1.0."""
        if x is None or y is None:
            print("[GUARDRAIL] Chyba: Souřadnice jsou prázdné (None).")
            return False
            
        try:
            x_val = float(x)
            y_val = float(y)
            if 0.0 <= x_val <= 1.0 and 0.0 <= y_val <= 1.0:
                return True
            print(f"[GUARDRAIL] Varování: Souřadnice [{x_val}, {y_val}] jsou mimo obrazovku (0-1).")
            return False
        except (ValueError, TypeError):
            print(f"[GUARDRAIL] Chyba: Souřadnice mají neplatný datový typ: {x}, {y}")
            return False

    def is_system_zone_clash(self, y_pct):
        """Zabrání klikání do spodních 10 % obrazovky (hlavní panel OS)."""
        if float(y_pct) > 0.90:
            print(f"[GUARDRAIL] Blokováno: Pokus o kliknutí do systémové lišty (y={y_pct}).")
            return True
        return False

    def is_agent_looping(self, current_x_px, current_y_px):
        """Detekuje, zda model nekliká stále na stejné pixelové souřadnice."""
        if current_x_px == self.last_x and current_y_px == self.last_y:
            self.loop_counter += 1
            if self.loop_counter >= 3:
                print(f"[GUARDRAIL] KRIZE: Detekována nekonečná smyčka na pixelu [{current_x_px}, {current_y_px}]!")
                return True
        else:
            # Model kliknul jinam -> resetujeme počítadlo
            self.last_x = current_x_px
            self.last_y = current_y_px
            self.loop_counter = 0

