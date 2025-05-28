from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        return jsonify({'result': num1 + num2})
    except (TypeError, ValueError):
        return jsonify({'error': 'Invalid input, please provide two numbers'}), 400

if __name__ == '__main__':
    app.run(debug=True)
