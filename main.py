# main.py
import json
from core.agent import AgentsLeagueCore

def main():
    print("=== [AGENT LEAGUE HACKATHON] CORE AGENT CORE ENGINE INTERNALS ===")
    bot = AgentsLeagueCore()
    
    # Validation test case (Internal IP leakage check)
    test_prompt = "Fetch server schema updates for internal machine 192.168.1.50"
    print(f"\n[+] Processing Prompt: {test_prompt}")
    
    result = bot.execute_workflow(test_prompt)
    print(f"\n[+] Multi-Step Pipeline Traces:\n{json.dumps(result, indent=4)}")

if __name__ == "__main__":
    main()

