from core.security import SecurityLayer
from core.actions import ActionScheduler

class EnterpriseAgent:
    def __init__(self):
        self.security = SecurityLayer()
        self.actions = ActionScheduler()

    def process_command(self, user_prompt):
        # 1. Zero Trust Ingestion
        safe_prompt = self.security.sanitize_input(user_prompt)
        
        # 2. Reasoning (Multi-step Logic)
        if "192.168" in safe_prompt:
            action_result = self.actions.isolate_node("192.168.x.x")
            return f"CRITICAL: {action_result}"
        
        return "Command executed successfully in Enterprise Fabric."
