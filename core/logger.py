import datetime

class ReasoningLogger:
    def log_thought(self, step, decision):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[{timestamp}] [THOUGHT_PROCESS] Step: {step} | Decision: {decision}")
