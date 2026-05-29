from core.agent import EnterpriseAgent

def test_harness():
    bot = EnterpriseAgent()
    scenarios = [
        "Fetch server status", 
        "Fix vulnerabilities on 192.168.1.50"
    ]
    for s in scenarios:
        print(f"\n--- TESTING SCENARIO: {s} ---")
        result = bot.process_command(s)
        print(f"AGENT RESPONSE: {result}")

if __name__ == "__main__":
    test_harness()

