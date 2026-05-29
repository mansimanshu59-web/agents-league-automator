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
        # Step 1: Sanitization
        safe_prompt = self.security.sanitize_input(user_prompt)
        
        # Step 2: Intent Classification (Reasoning logic)
        intent = "MITIGATION" if "patch" in safe_prompt.lower() or "fix" in safe_prompt.lower() else "INFO"
        self.logger.log_thought("Intent Analysis", intent)

        # Step 3: Grounded Context (Foundry IQ)
        context = self.iq.get_grounded_context(intent)
        self.logger.log_thought("Grounded Intelligence", context)

        # Step 4: Multi-Step Execution
        if intent == "MITIGATION":
            action_res = self.actions.run_security_scan(safe_prompt)
            return f"ACTION_TAKEN: {action_res} | CONTEXT: {context}"
            
        return f"REASONING_COMPLETE: Status {context}"
