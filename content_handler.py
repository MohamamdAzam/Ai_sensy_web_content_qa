import requests
from bs4 import BeautifulSoup
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def ingest_content(urls):
    content_data = {}
    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            main_content = soup.find('main') or soup.find('div', {'class': 'content'})
            text = ' '.join([p.get_text() for p in main_content.find_all('p')]) if main_content else ""
            
            content_data[url] = text.strip() or "No content available"
        except Exception as e:
            content_data[url] = f"Error fetching content: {str(e)}"
    return content_data

def answer_question(content, question):
    combined_text = ' '.join(content.values())
    results = qa_pipeline(
        question=question,
        context=combined_text,
        max_answer_len=200,
        top_k=3
    )

    answers = [
        f"{result['answer']} (Confidence: {round(result['score'] * 100, 2)}%)"
        for result in results
    ]
    
    return '\n'.join(answers)

def summarize_content(content):
    combined_text = ' '.join(content.values())[:2000] 
    result = summarizer(combined_text, max_length=300, min_length=100, do_sample=False)
    return result[0]['summary_text']
