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
        # 1. Zero Trust Ingestion
        safe_prompt = self.security.sanitize_input(user_prompt)
        
        # 2. Reasoning (Multi-step)
        intent = "DATA_RETRIEVAL_PIPELINE" if "fetch" in safe_prompt else "THREAT_MITIGATION_PIPELINE"
        
        # 3. Foundry IQ Grounding (The Intelligence Step)
        context = self.iq.get_grounded_context(intent)
        self.logger.log_thought("Foundry IQ Grounding", f"Retrieved: {context}")
        
        # 4. Final Execution
        return f"Agent Action: {self.actions.run_security_scan(safe_prompt)} | Context: {context}"
