class FoundryIQ:
    def get_grounded_context(self, intent):
        # Simulation of an Enterprise Graph query
        schema = {
            "INFO": "Schema: v2026.05.29 | Status: Active | Compliance: NIST-800",
            "MITIGATION": "Policy: Auto-patching enabled for segment 192.168.x.x"
        }
        return schema.get(intent, "General enterprise context.")
