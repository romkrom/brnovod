import os
import secrets
import hmac
import hashlib
from typing import Dict, Any

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

