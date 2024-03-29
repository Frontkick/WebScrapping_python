import requests
from flask import Flask, jsonify

app = Flask(__name__)

def search_articles(query, num_results=10):
    api_key = "AIzaSyDdgsglrtocaYOcA8V1s4Ad0Te9bsAwIYs"
    search_engine_id = "d5e0315085b194afb"
    url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={search_engine_id}&q={query}&num={num_results}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        items = data.get('items', [])
        
        articles = []  # Store articles in a list
        for item in items:
            article_title = item.get('title')
            article_url = item.get('link')
            articles.append({'title': article_title, 'url': article_url})  # Append each article to the list
        
        return articles  # Return the list of articles
    else:
        return None  # Return None if request failed

@app.route('/api/<string:param>', methods=['GET'])
def get_request(param):
    articles = search_articles( param)
    if articles:
        response = {
            'articles': articles
        }
    else:
        response = {
            'message': 'Failed to fetch search results.'
        }
    return jsonify(response)

if __name__ == '__main__':
    
    app.run(debug=True)
