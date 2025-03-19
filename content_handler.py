import requests
from bs4 import BeautifulSoup

def scrape_url(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        main_content = soup.find(['main', 'article', 'div.entry-content']) or soup.body
        
        for element in main_content(['script', 'style', 'aside', 'nav', 'footer']):
            element.decompose()
            
        text = ' '.join([p.get_text() for p in main_content.find_all(['p', 'h1', 'h2', 'h3']) if p.get_text().strip()])
        return text.strip()[:10000] 
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return ''
