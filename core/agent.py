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
        self.logger.log_thought("Input Parsing", f"Sanitized: {safe_prompt}")
        
        # Foundry IQ Integration (The real deal)
        context = self.iq.get_grounded_context("DATA_RETRIEVAL_PIPELINE")
        self.logger.log_thought("Grounded Intelligence", context)
        
        # Action Logic
        if "patch" in safe_prompt.lower():
            result = self.actions.run_security_scan(safe_prompt)
            return f"REASONING_FINAL: {result} | IQ_STATUS: Verified."
            
        return f"REASONING_FINAL: Executing standard logic with context: {context}"
