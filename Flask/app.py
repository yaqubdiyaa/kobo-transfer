from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('indextest.html')

@app.route('/run_executable', methods=['POST'])
def run_executable():
    # Get input data from the request
    input_data = request.json['input_data']

    # Run the executable with the input data
    result = subprocess.run(['./test.py', input_data], capture_output=True, text=True)

    # Return the output as JSON
    return jsonify({'output': result.stdout})

if __name__ == '__main__':
    app.run(debug=True)