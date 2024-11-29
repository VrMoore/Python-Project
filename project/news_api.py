from requests import get as get_url
from os import getenv, path
import hashlib
import json
from dotenv import load_dotenv

load_dotenv()
api_key = getenv('API_KEY')

parameters = {
    'apiKey' : api_key,
    'country' : 'us',
    'category' : 'health',
    'language' : 'en',
    'sortBy' : 'popularity'
}

url = "https://newsapi.org/v2/top-headlines"
response = get_url(url, params=parameters)

class newsAggr() :
    
    def __init__(self) :
        self.news_list = []

    def get_news(self, news_data : dict) :
        
        articles = news_data.get('articles')
        
        for article in articles :
            news_dict = {
                'source': article.get('source', {}).get('name', ''),
                'author': article.get('author', ''),
                'title': article.get('title', ''),
                'description': article.get('description', '')
            }
            self.news_list.append(news_dict)
            self.print_output(news=news_dict)

    def fetch_news(self) :
        
        if response.status_code == 200 :
            news_data = response.json()
            self.get_news(news_data)
            self.write_to_local()

        else :
            return f"{response.status_code}\nTry again laters"

    def write_to_local(self) :
        
        object_news = json.dumps(self.news_list, indent=4)

        with open(file="api project/news.json", mode="w") as file:
            file.write(object_news)

    def print_output(self, news : dict) :
        
        print(f"=={news['title']}==")
        print(f"{news['description']}")
        print(f"{news['author']} - {news['source']}")

class cacheNews() :
    
    def __init__(self) :
        self.cache = {}

    def create_keys(self, params : dict, urls : str) :

        news_data = hashlib.md5(json.dumps(params, sort_keys=True).encode()).hexdigest()
        self.cache[urls] = news_data

        return self.cache

    def load_cache(self) :
        pass

    def save_cache(self) :
        pass

if __name__  == "__main__" :
    my_news = newsAggr()
    my_news.fetch_news()

    # my_cache = cacheNews()
    # my_cache.create_keys(params=parameters, urls=url)
    # my_cache.save_cache()