import json
from core.agent import AgentsLeagueCore

def main():
    print("--- SECURE-IQ: ENTERPRISE ENGINE ACTIVE ---")
    bot = AgentsLeagueCore()
    
    # Ye simulation hai 'Foundry IQ' grounding ke liye
    test_prompts = [
        "Fetch server schema for 192.168.1.1",
        "Analyze security logs for unauthorized access"
    ]
    
    for prompt in test_prompts:
        print(f"\n[ANALYZING]: {prompt}")
        result = bot.execute_workflow(prompt)
        print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
