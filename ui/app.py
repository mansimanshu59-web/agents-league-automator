import os
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# Ultra-Premium Yellow & Black Cyber-Grid UI Template
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure-IQ Automator Console</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
        body { background-color: #0b0c10; color: #fff; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        
        /* Main Container matching the dashboard layout */
        .dashboard-container { 
            width: 100%; max-width: 1100px; height: 650px; 
            background: linear-gradient(135deg, #121317 0%, #1a1b20 35%, #f4c430 35%, #f4c430 100%);
            border-radius: 16px; overflow: hidden; display: flex; position: relative;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5); border: 1px solid rgba(244, 196, 48, 0.2);
        }

        /* Left Black Control Panel */
        .left-panel { width: 40%; height: 100%; background: #121317; padding: 40px; display: flex; flex-direction: column; justify-content: space-between; z-index: 2; }
        .logo-section { display: flex; align-items: center; gap: 10px; color: #f4c430; font-weight: bold; letter-spacing: 1px; }
        .logo-icon { width: 20px; height: 20px; background: #f4c430; transform: skewX(-15deg); }
        
        .command-header h1 { font-size: 2.2rem; font-weight: 800; line-height: 1.2; margin-bottom: 20px; color: #ffffff; text-transform: uppercase; }
        .input-group { background: #1a1b20; border-radius: 8px; padding: 15px; border-left: 4px solid #f4c430; margin-top: 20px; }
        .input-group label { display: block; font-size: 0.8rem; color: #888; margin-bottom: 8px; text-transform: uppercase; }
        .input-group textarea { width: 100%; background: transparent; border: none; color: #fff; resize: none; outline: none; font-size: 0.95rem; height: 80px; }
        
        .btn-trigger { background: #f4c430; color: #121317; border: none; padding: 14px 24px; font-weight: bold; border-radius: 25px; cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 10px; text-transform: uppercase; transition: all 0.3s ease; width: 100%; margin-top: 15px; }
        .btn-trigger:hover { background: #ffffff; transform: translateY(-2px); }

        .status-badge { background: rgba(255,255,255,0.05); padding: 10px 15px; border-radius: 30px; display: inline-flex; align-items: center; gap: 8px; font-size: 0.85rem; color: #a0a0a0; width: fit-content; }
        .status-dot { width: 8px; height: 8px; background: #00ff66; border-radius: 50%; box-shadow: 0 0 10px #00ff66; }

        /* Right Yellow/White Analytics Panel */
        .right-panel { width: 60%; height: 100%; padding: 40px; display: flex; flex-direction: column; justify-content: space-between; align-items: flex-end; position: relative; z-index: 1; }
        .nav-links { display: flex; gap: 25px; font-size: 0.8rem; font-weight: bold; color: #121317; text-transform: uppercase; }
        
        /* Execution Log Terminal Box */
        .terminal-box { width: 100%; max-width: 550px; background: #121317; border-radius: 12px; padding: 25px; box-shadow: 0 15px 35px rgba(0,0,0,0.3); border: 1px solid rgba(255,255,255,0.1); margin-top: 40px; }
        .terminal-header { font-size: 1.5rem; font-weight: 700; color: #ffffff; margin-bottom: 15px; text-transform: uppercase; letter-spacing: 0.5px; }
        .log-stream { background: #0b0c10; border-radius: 6px; padding: 15px; font-family: 'Courier New', Courier, monospace; font-size: 0.85rem; height: 180px; overflow-y: auto; color: #00ff66; line-height: 1.5; border-left: 2px solid #f4c430; }
        
        /* Microsoft IQ Node Badges at Bottom Right */
        .iq-nodes { display: flex; gap: 20px; color: #121317; font-weight: 700; font-size: 0.85rem; }
        .iq-node { display: flex; align-items: center; gap: 6px; background: rgba(18, 19, 23, 0.08); padding: 6px 12px; border-radius: 6px; }
        
        /* Custom Scrollbar for Logs */
        .log-stream::-webkit-scrollbar { width: 6px; }
        .log-stream::-webkit-scrollbar-thumb { background: #333; border-radius: 4px; }
    </style>
</head>
<body>

    <div class="dashboard-container">
        <div class="left-panel">
            <div class="logo-section">
                <div class="logo-icon"></div>
                <span>SECURE-IQ</span>
            </div>
            
            <div class="command-header">
                <h1>Agent<br>Command<br>Interface</h1>
                
                <div class="input-group">
                    <label>⚡ Enter Enterprise Command Prompt</label>
                    <textarea id="promptInput" placeholder="e.g., Fetch server schema updates for internal machine 192.168.1.50..."></textarea>
                </div>
                
                <button class="btn-trigger" onclick="runWorkflow()">🚀 Trigger Agent Workflow</button>
            </div>
            
            <div class="status-badge">
                <div class="status-dot"></div>
                <span>STATUS: <strong style="color: #fff;">SECURE // ACTIVE</strong></span>
            </div>
        </div>

        <div class="right-panel">
            <div class="nav-links">
                <span>About Overview</span>
                <span>Process Workflow Viewer</span>
                <span>Get In Touch Configuration</span>
            </div>
            
            <div class="terminal-box">
                <div class="terminal-header">Intelligence Node Logs</div>
                <div class="log-stream" id="logStream">
                    [16:04:12] [INFO] System Initialized.<br>
                    [16:04:15] [INFO] Connection established to MS_FOUNDRY_IQ.<br>
                    [16:04:18] [AUDIT] Standby mode active. Awaiting user input pipeline dispatch...
                </div>
            </div>
            
            <div class="iq-nodes">
                <div class="iq-node">🛡️ FOUNDRY IQ</div>
                <div class="iq-node">📇 WORK IQ</div>
                <div class="iq-node">🔀 FABRIC IQ</div>
            </div>
        </div>
    </div>

    <script>
        function runWorkflow() {
            const promptValue = document.getElementById('promptInput').value;
            if(!promptValue.trim()) return;
            
            const logBox = document.getElementById('logStream');
            logBox.innerHTML += `<br><span style="color: #f4c430;">[${new Date().toLocaleTimeString()}] [USER] Dispatching Custom Command...</span>`;
            
            fetch('/process', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ prompt: promptValue })
            })
            .then(res => res.json())
            .then(data => {
                logBox.innerHTML += `<br><span style="color: #ff3333;">[${new Date().toLocaleTimeString()}] [SECURITY] Sanitizing incoming payload structural nodes...</span>`;
                setTimeout(() => {
                    logBox.innerHTML += `<br><span style="color: #00ff66;">[${new Date().toLocaleTimeString()}] [FOUNDRY_IQ] Grounded Context: ${data.result}</span>`;
                    logBox.scrollTop = logBox.scrollHeight;
                }, 800);
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json() or {}
    user_prompt = data.get('prompt', '')
    
    # Simple simulation mapping back to core/security logic
    if "192.168" in user_prompt or "api" in user_prompt.lower():
        return jsonify({"result": "Context secured. Malicious raw variables masked successfully."})
    return jsonify({"result": "Query parsed via Multi-Step Core Engine node successfully."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

