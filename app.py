from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data.get("expression", "")

        # Validate input to prevent code injection
        if not re.match(r"^[0-9+\-*/%. ]+$", expression):
            return jsonify({"result": "Error: Invalid input"}), 400

        # Safely evaluate the expression
        result = eval(expression)
        return jsonify({"result": result})

    except Exception as e:
        return jsonify({"result": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
