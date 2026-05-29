# Secure-IQ Automator (Reasoning Agent Core)

An advanced, multi-step reasoning agent architecture engineered for the **Microsoft Agents League Hackathon 2026**. This system implements deep security sanitization layers combined with sequential logic execution, designed to integrate seamlessly with the **Microsoft Foundry IQ** intelligence layer.

## 🏗️ System Architecture & Workflow
The agent processes user prompts through a strict zero-trust ingestion pipeline:

1. **Ingestion & Sanitization Layer:** Filters malicious prompt injections, system override attempts, and masks sensitive credentials.
2. **Contextual Grounding (Foundry IQ):** Connects to verified enterprise knowledge graphs to fetch cited, verified telemetry, drastically reducing LLM hallucinations.
3. **Multi-Step Execution Engine:** Runs the sanitized query through structured functional execution chains (State Management) to generate verifiable outputs.

## 🛡️ Security & Compliance
Our agent utilizes a **Zero-Trust Sanitization Layer**:
- **Credential Masking:** Automatically detects and masks API tokens, passwords, and internal IP addresses.
- **Outbound Audit:** Every response is verified to ensure no sensitive structural anomalies leak.
- **Hardened Logic:** Built-in regex-based filtering prevents system-override attempts.

## 🧠 Agent Reasoning Workflow
The agent operates on a multi-stage cognitive pipeline designed for high-stakes enterprise telemetry:
`User Input` ➡️ `Security Sanitization` ➡️ `Intent Analysis` ➡️ `Foundry IQ Grounding` ➡️ `Execution Engine` ➡️ `Outbound Audit` ➡️ `Final Response`

## 🛠️ Tech Stack & Dependencies
- **Runtime:** Python 3.10+ / Termux POSIX Sandbox
- **Intelligence Layer:** Microsoft Foundry IQ (Grounding Engine)
- **Web Interface:** Flask (Real-time telemetry streaming)
- **Version Control:** Git / GitHub Infrastructure

## 🚀 Local Installation & Deployment
```bash
git clone [https://github.com/mansimanshu59-web/agents-league-automator.git](https://github.com/mansimanshu59-web/agents-league-automator.git)
cd agents-league-automator
pip install -r requirements.txt
python main.py
