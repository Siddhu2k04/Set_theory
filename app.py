from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/operate', methods=['POST'])
def operate():
    data = request.get_json()
    set1_input = data.get('set1', '')
    set2_input = data.get('set2', '')
    operation = data.get('operation', '')

    # Convert strings to Python sets
    set1 = set(map(str.strip, set1_input.split(','))) if set1_input else set()
    set2 = set(map(str.strip, set2_input.split(','))) if set2_input else set()

    result = set()
    if operation == 'union':
        result = set1.union(set2)
    elif operation == 'intersection':
        result = set1.intersection(set2)
    elif operation == 'difference':
        result = set1.difference(set2)
    elif operation == 'symmetric_difference':
        result = set1.symmetric_difference(set2)

    return jsonify({
        'set1': list(set1),
        'set2': list(set2),
        'operation': operation.replace('_', ' ').title(),
        'result': list(result)
    })

if __name__ == '__main__':
    app.run(debug=True)
