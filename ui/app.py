from flask import Flask, render_template_string, request, jsonify
from core.agent import EnterpriseAgent # Agent import karo

app = Flask(__name__)

# [BAKI KA HTML_TEMPLATE YAHIN RAKHO - Maine yahan sirf process function update kiya hai]

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    user_prompt = data.get('prompt', '')
    
    # AB YE ASLI AGENT CALL KAREGA
    agent = EnterpriseAgent()
    result = agent.process_command(user_prompt)
    
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
