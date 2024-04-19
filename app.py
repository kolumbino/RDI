from flask import Flask, request, render_template
from newsapi import NewsApiClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("NEWS_API_KEY")
newsapi = NewsApiClient(api_key=API_KEY)


@app.route('/')
def index():
    top_headlines = newsapi.get_top_headlines(country='us')
    articles = top_headlines.get('articles', [])
    return render_template('index.html', articles=articles)


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form.get('query', '')
    if query:
        all_articles = newsapi.get_everything(q=query)
        articles = all_articles.get('articles', [])
    else:
        articles = []
    return render_template('search.html', articles=articles, query=query)


if __name__ == '__main__':
    app.run(debug=True)
