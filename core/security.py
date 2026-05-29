# core/security.py
import re

class SecurityLayer:
    def __init__(self):
        # Professional regex matching for hard security compliance
        self.leak_patterns = {
            "api_key": r"(?i)(api[_-]?key|secret|password|passwd|token|bearer|credential)[\s:=]+['\"]?[a-zA-Z0-9_\-]{16,}['\"]?",
            "ipv4_internal": r"\b(?:10|172\.(?:1[6-9]|2[0-9]|3[0-1])|192\.168)\.[0-9]{1,3}\.[0-9]{1,3}\b",
            "source_code_leak": r"(?i)(db_password|config\.json|client_secret|\.env|ssh-rsa)"
        }

    def sanitize_input(self, user_prompt: str) -> str:
        sanitized = user_prompt
        for label, pattern in self.leak_patterns.items():
            if re.search(pattern, sanitized):
                sanitized = re.sub(pattern, f"[SECURE_MASKED_{label.upper()}]", sanitized)
        return sanitized

    def verify_output(self, agent_response: str) -> bool:
        for label, pattern in self.leak_patterns.items():
            if re.search(pattern, agent_response):
                return False # Immediate Block if any pattern leaks into outbound data
        return True

