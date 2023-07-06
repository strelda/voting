from flask import Flask, request, jsonify, Response
from collections import Counter
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173", "http://localhost:5000"]}})

votes = Counter()

def stream():
    client = sseclient.SSEClient()
    for event in client:
        yield f"data: {event.data}\n\n"

@app.route('/vote', methods=['POST'])
def vote():
    data = request.get_json()

    if 'option' in data:
        votes[data['option']] += 1
        return {'msg': 'Vote has been recorded.', 'total_votes': dict(votes)}, 200
    return {'msg': 'No option provided in vote.'}, 400

@app.route('/results', methods=['GET'])
def results():
    return jsonify(dict(votes))

@app.route('/clear', methods=['POST'])
def clear_data():
    global votes
    votes = Counter()
    return {'msg': 'Vote data cleared.'}, 200

@app.route('/update')
def updates():
    return Response(stream(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
