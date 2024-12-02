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
    'category' : 'science',
    'language' : 'en',
    'sortBy' : 'popularity'
}

url = "https://newsapi.org/v2/top-headlines"
response = get_url(url, params=parameters)

class newsAggr() :
    
    def __init__(self) :
        self.news_list = []
        self.cache_news_method = cacheNews()

    def get_news(self, news_data : dict) :
        
        articles = news_data.get('articles')

        # Generate key dulu
        # Lalu panggil cache_load
        # Jika ada maka buka news.json

        news_key = self.cache_news_method.create_keys(params=parameters, urls=url)
        cache_news_data = self.cache_news_method.load_cache(news_key)

        if cache_news_data is not None :

            with open('api project/news.json',mode='r') as bar :
                bar_news = json.load(bar)
                print('Fetching from local....')
                print(bar_news['article'])
                
        for article in articles :
            news_dict = {
                'source': article.get('source', {}).get('name', ''),
                'author': article.get('author', ''),
                'title': article.get('title', ''),
                'description': article.get('description', '')
            }
            self.news_list.append(news_dict)
            self.print_output(news=news_dict)
            
        return self.news_list

    def fetch_news(self) :
        
        if response.status_code == 200 :
            news_data = response.json()
            self.get_news(news_data)
            self.write_to_local(self.news_list)
            self.cache_news_method.save_cache(self.news_list)

        else :
            return f"{response.status_code}\nTry again laters"

    def write_to_local(self, news_list : dict) :

        with open(file="api project/news.json", mode="w") as file:
            json.dump(news_list, file, indent=4)

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

    def save_cache(self, news_article : dict) :

        self.create_keys(params=parameters, urls=url)
        self.cache['article'] = news_article

        with open('api project/news.json', mode='w') as cn :
            json.dump(self.cache, cn, indent=4)

    def load_cache(self, token : dict) :
        
        with open(file='api project/news.json', mode='r') as foo :
            open_cache = json.load(foo)
            if token[url] == open_cache[url]:
                return open_cache['article']
            else :
                return False

if __name__  == "__main__" :
    my_news = newsAggr()
    my_news.fetch_news()

    # my_cache = cacheNews()
    # my_cache.create_keys(params=parameters, urls=url)
    # my_cache.load_cache()