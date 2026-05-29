from core.security import SecurityLayer
from core.actions import ActionScheduler
from core.logger import ReasoningLogger

class EnterpriseAgent:
    def __init__(self):
        self.security = SecurityLayer()
        self.actions = ActionScheduler()
        self.logger = ReasoningLogger()

    def process_command(self, user_prompt):
        # 1. Sanitization
        self.logger.log_thought("Security Check", "Scanning for injections...")
        safe_prompt = self.security.sanitize_input(user_prompt)
        
        # 2. Decision Logic
        if "192.168" in safe_prompt:
            self.logger.log_thought("Threat Mitigation", "Internal IP found, triggering isolation.")
            return self.actions.isolate_node("192.168.x.x")
        
        return "System clear, executing standard operation."
