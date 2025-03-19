from flask import Flask, request, jsonify
from flask_cors import CORS
from content_handler import ingest_content, answer_question, summarize_content

app = Flask(__name__)
CORS(app)

content_storage = {}

@app.route('/ingest', methods=['POST'])
def ingest():
    urls = request.json.get("urls", [])
    content_storage.update(ingest_content(urls))
    return jsonify({"message": "Content ingested successfully!"})

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get("question")
    if not content_storage:
        return jsonify({"error": "No content available. Please ingest URLs first."})
    
    answer = answer_question(content_storage, question)
    return jsonify({"answer": answer})

@app.route('/summarize', methods=['GET'])
def summarize():
    if not content_storage:
        return jsonify({"error": "No content available to summarize."})
    
    summary = summarize_content(content_storage)
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
