from flask import Flask, request, jsonify
from flask_cors import CORS
from scraper import scrape_url
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy
import numpy as np
import requests
import re

app = Flask(__name__)
CORS(app)


nlp = spacy.load("en_core_web_sm")
vectorizer = TfidfVectorizer(stop_words='english')
text_chunks = []
tfidf_matrix = None

def chunk_text(text, max_words=200):
    words = re.findall(r'\b\w+\b', text)
    return [' '.join(words[i:i+max_words]) for i in range(0, len(words), max_words)]

@app.route('/ingest', methods=['POST'])
def ingest_url():
    global tfidf_matrix
    data = request.json
    urls = data.get('urls', [])
    
    for url in urls:
        text = scrape_url(url)
        if text:
            chunks = chunk_text(text)
            text_chunks.extend(chunks)
    
    if text_chunks:
        tfidf_matrix = vectorizer.fit_transform(text_chunks)
    
    return jsonify({"message": f"Processed {len(urls)} URLs, {len(text_chunks)} chunks stored"})


@app.route('/ask', methods=['POST'])
def answer_question():
    data = request.json
    question = data.get('question', '')
    
    if not text_chunks:
        return jsonify({"answer": "No content available. Please ingest URLs first."})
    

    question_vec = vectorizer.transform([question])
    similarities = cosine_similarity(question_vec, tfidf_matrix)
    top_indices = np.argsort(similarities[0])[-3:][::-1]
    context = ' '.join([text_chunks[i] for i in top_indices])

    doc = nlp(context)
    question_doc = nlp(question.lower())

    answer = ""
    for sent in doc.sents:
        sent_text = sent.text
        if any([
            'is a' in sent_text.lower(),
            'is an' in sent_text.lower(),
            'refers to' in sent_text.lower(),
            'is designed' in sent_text.lower()
        ]) and any(token.text in sent_text for token in question_doc if token.pos_ in ['NOUN', 'PROPN']):
            answer = sent_text
            break

    if not answer:
        sentences = [sent.text for sent in doc.sents]
        sentence_vectors = vectorizer.transform(sentences)
        sentence_similarities = cosine_similarity(question_vec, sentence_vectors)
        answer = sentences[np.argmax(sentence_similarities)]
    
    return jsonify({"answer": answer.strip()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
