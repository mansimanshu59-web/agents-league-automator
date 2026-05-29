import requests

class FoundryIQ:
    def get_grounded_context(self, intent):
        # Real-time API hit to get simulated enterprise telemetry
        try:
            # Using a reliable mock endpoint for demonstration
            response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
            data = response.json()
            return f"FOUNDRY_IQ_GROUNDED_DATA: [Title: {data['title'][:20]}]"
        except:
            return "FOUNDRY_IQ_OFFLINE: Using fallback static schema."
