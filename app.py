from flask import Flask, render_template, request, jsonify
from core.agent import EnterpriseAgent

app = Flask(__name__)
agent = EnterpriseAgent()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    command = data.get('command', '')
    result = agent.process_command(command)
    return jsonify({"output": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
