from core.security import SecurityLayer
from core.actions import ActionScheduler
from core.logger import ReasoningLogger
from core.foundry import FoundryIQ

class EnterpriseAgent:
    def __init__(self):
        self.security = SecurityLayer()
        self.actions = ActionScheduler()
        self.logger = ReasoningLogger()
        self.iq = FoundryIQ()

    def process_command(self, user_prompt):
        safe_prompt = self.security.sanitize_input(user_prompt)
        
        # Inference Routing Logic
        # Agar query mein keywords kam hain, toh local simple logic
        if len(safe_prompt.split()) < 5:
            self.logger.log_thought("Routing", "Local/Simple Processing")
            return f"AGENT_LOCAL: {safe_prompt} - Executed without IQ grounding."
        
        # Agar query complex hai, toh Foundry IQ call karo
        else:
            self.logger.log_thought("Routing", "Foundry IQ Grounding Required")
            context = self.iq.get_grounded_context("COMPLEX_ENTERPRISE_QUERY")
            
            if "patch" in safe_prompt.lower():
                result = self.actions.run_security_scan(safe_prompt)
                return f"REASONING_FINAL: {result} | IQ_STATUS: {context}"
                
            return f"REASONING_COMPLETE: {context}"
