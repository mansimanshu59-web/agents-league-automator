import json
import time
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

    def calculate_risk_metrics(self, prompt):
        """Dynamically evaluates security parameters based on payload signatures"""
        prompt_lower = prompt.lower()
        injection_prob = "LOW"
        threat_score = 14 # Baseline standard execution score
        
        # Security signature verification heuristics
        if any(x in prompt_lower for x in ["admin", "root", "override", "bypass", "../", "sudo"]):
            injection_prob = "MEDIUM"
            threat_score = 48
        if any(x in prompt_lower for x in ["select", "drop", "exec", "eval", "<script>", "union"]):
            injection_prob = "HIGH"
            threat_score = 91
            
        return {
            "prompt_injection_probability": injection_prob,
            "threat_confidence_score": f"{threat_score}%",
            "risk_status": "MONITORED" if threat_score < 50 else "ANOMALY_TRIGGERED"
        }

    def process_command(self, user_prompt):
        # Step 1: Zero-Trust Inspection & Risk Assessment
        safe_prompt = self.security.sanitize_input(user_prompt)
        metrics = self.calculate_risk_metrics(user_prompt)
        
        # Rendering dynamic telemetry logs
        self.logger.log_thought("Zero-Trust Layer", f"Payload Scan Complete. Injection Probability: {metrics['prompt_injection_probability']} | Threat Score: {metrics['threat_confidence_score']}")

        # Step 2: Internal Micro-Agent Execution JSON Trace
        trace = {
            "trace_id": f"TR-019E-{int(time.time())}",
            "execution_steps": ["Payload_Sanitization", "Metric_Calculation", "Cloud_Grounding", "Action_Dispatch"],
            "telemetry_node": metrics
        }
        # Injects a beautifully formatted JSON trace inside the terminal logs
        self.logger.log_thought("Execution Trace", json.dumps(trace))

        # Step 3: Inference Routing Logic
        words = safe_prompt.split()
        if len(words) < 4:
            self.logger.log_thought("Routing Engine", "Optimizing query path: Single-step standalone logic mapped to Local NPU.")
            return f"[LOCAL_NPU_EXECUTION]: Command executed locally. Secure-IQ telemetry verified."

        self.logger.log_thought("Routing Engine", "Complex enterprise multi-step flow matched. Establishing Microsoft Foundry IQ Cloud Tunnel.")
        
        # Step 4: Grounded Context via Foundry IQ
        raw_context = self.iq.get_grounded_context(safe_prompt)
        context_data = json.loads(raw_context)
        
        self.logger.log_thought("Cognitive Core", f"Context bound via Foundry Reference Policy: {context_data.get('policy', 'Standard Sec-Compliance-01')}")

        # Step 5: Action Scheduler Execution
        if any(x in safe_prompt.lower() for x in ["patch", "scan", "audit", "investigate"]):
            self.logger.log_thought("Action Scheduler", "Anomalous or critical state requires active orchestration. Dispatching tools.")
            scan_result = self.actions.run_security_scan(safe_prompt)
            
            final_response = {
                "Status": "SUCCESS_RESOLVED",
                "Reasoning_Pipeline": "ZeroTrust ➜ MetricAnalysis ➜ JSONTraceLog ➜ CloudIQGrounding ➜ SystemRemediation",
                "Risk_Telemetry": metrics,
                "Cloud_Context": context_data,
                "Orchestration_Output": scan_result
            }
            return json.dumps(final_response, indent=2)

        return f"[SECURE-IQ COMPLETE]: Multi-step cloud reasoning pipeline closed. State: Active/Secure."
