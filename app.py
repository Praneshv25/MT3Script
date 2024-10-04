from flask import Flask, jsonify, request
import subprocess

app = Flask(__name__)


@app.route('/run_job', methods=['POST'])
def run_job():
    data = request.get_json()
    model_name = data.get('model_name')

    if model_name:
        try:
            result = subprocess.run(['python', 'click_commands.py', 'run', model_name], check=True, capture_output=True,
                                    text=True)
            return jsonify({"status": "success", "output": result.stdout}), 200
        except subprocess.CalledProcessError as e:
            return jsonify({"status": "error", "output": e.stderr}), 500
    else:
        return jsonify({"status": "error", "message": "Model name is required"}), 400

c 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
