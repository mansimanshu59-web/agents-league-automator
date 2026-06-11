from flask import Flask, render_template, request, jsonify
import re
import time
import json
import random

app = Flask(__name__)

class SecurityLayer:
    """Zero-Trust Security Layer"""
    def sanitize_input(self, user_input):
        # Mask sensitive patterns
        patterns = {
            'api_key': r'(api[_-]?key|secret|token)[\s:=]+[\'"]?[\w-]+',
            'ip': r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
        }
        for name, pattern in patterns.items():
            user_input = re.sub(pattern, f'[MASKED_{name}]', user_input)
        return user_input

class AgentCore:
    """Enterprise Agent Reasoning Engine"""
    def __init__(self):
        self.knowledge_base = {
            "vulnerabilities": {
                "CVE-2026-1337": {"severity": "CRITICAL", "patch": "KB-2026-001"},
                "CVE-2026-1338": {"severity": "HIGH", "patch": "KB-2026-002"}
            },
            "policies": ["Sec-Ref-04", "Zero-Trust-Mandate", "Compliance-2026"]
        }
    
    def analyze_command(self, command):
        cmd_lower = command.lower()
        
        # Risk assessment
        risk_score = 14
        risk_level = "LOW"
        
        if any(x in cmd_lower for x in ['rm', 'delete', 'drop', 'format', 'del']):
            risk_score = 95
            risk_level = "CRITICAL"
        elif any(x in cmd_lower for x in ['sudo', 'admin', 'root', 'bypass']):
            risk_score = 75
            risk_level = "HIGH"
        elif any(x in cmd_lower for x in ['scan', 'vuln', 'patch', 'audit']):
            risk_score = 30
            risk_level = "MEDIUM"
        
        return risk_score, risk_level
    
    def execute_command(self, command, risk_score):
        cmd_lower = command.lower()
        
        if risk_score > 80:
            return {
                "status": "BLOCKED",
                "message": "Command blocked due to critical risk level",
                "actions": []
            }
        
        actions = []
        if 'scan' in cmd_lower or 'vuln' in cmd_lower:
            actions.append("🔍 Running vulnerability scan")
            actions.append(f"📋 Found: {len(self.knowledge_base['vulnerabilities'])} vulnerabilities")
            actions.append("🛠 Auto-remediation initiated")
        elif 'patch' in cmd_lower:
            actions.append("📦 Deploying security patches")
            actions.append("✅ Patches applied successfully")
        else:
            actions.append("⚙ Executing command through secure pipeline")
            actions.append("✅ Command processed successfully")
        
        return {
            "status": "COMPLETED",
            "message": "Command executed successfully",
            "actions": actions
        }

class FoundryIQ:
    """Microsoft Foundry IQ Integration"""
    def __init__(self):
        self.connected = True
    
    def ground_context(self, command):
        return {
            "grounding_status": "connected",
            "knowledge_graph": {
                "datasets": ["enterprise_assets", "vulnerability_db", "compliance_records"],
                "policies": ["Zero-Trust", "Sec-Compliance", "Data-Protection"]
            },
            "context": f"Query grounded with Foundry IQ: {command[:50]}..."
        }

# Initialize components
security = SecurityLayer()
agent = AgentCore()
foundry = FoundryIQ()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        data = request.get_json()
        user_command = data.get('command', '').strip()
        
        if not user_command:
            return jsonify({'error': 'No command provided'}), 400
        
        # Step 1: Security Sanitization
        sanitized = security.sanitize_input(user_command)
        
        # Step 2: Risk Analysis
        risk_score, risk_level = agent.analyze_command(user_command)
        
        # Step 3: Foundry Grounding
        grounding = foundry.ground_context(user_command)
        
        # Step 4: Execute Command
        result = agent.execute_command(user_command, risk_score)
        
        # Step 5: Generate Response
        response = {
            "command": user_command,
            "sanitized": sanitized,
            "risk": {
                "score": risk_score,
                "level": risk_level,
                "status": "BLOCKED" if risk_score > 80 else "ALLOWED"
            },
            "foundry": grounding,
            "execution": result,
            "trace_id": f"TR-{int(time.time())}",
            "timestamp": time.time()
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "agent": "active",
        "foundry": "connected",
        "timestamp": time.time()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
