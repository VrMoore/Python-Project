from requests import get as get_url
from os import getenv, path, getcwd
import hashlib
import json
from dotenv import load_dotenv

# Make .env file in the same folder and place your API keys
load_dotenv()
api_key = getenv('API_KEY')

# Customize your own parameters, check the link below for more detailed information.
# https://newsapi.org/docs/endpoints/everything
parameters = {
    'apiKey' : api_key,
    'country' : 'us',
    'category' : 'health',
    'language' : 'en',
    'sortBy' : 'popularity'
}

# Load parameter into request
url = "https://newsapi.org/v2/top-headlines"
response = get_url(url, params=parameters)

# Specify your name path
MY_CACHE_PATH = f'api project/news.json'

class newsAggr() :
    
    def __init__(self) :
        self.news_list = []
        self.cache_news_method = cacheNews()

    def get_news(self, news_data : dict) -> None :
        """
            Check if key is present by calling load_cache method,
            If TRUE then load the cache,
            If FALSE then make a request and load it in the cache with new key
        """
        
        articles = news_data.get('articles')

        news_key = self.cache_news_method.create_keys(params=parameters, urls=url)
        cache_news_data = self.cache_news_method.load_cache(news_key)

        if cache_news_data is True :

            with open(file= MY_CACHE_PATH,mode='r') as bar :
                bar_news = json.load(bar)
                print('Fetching from local....')
                
                for article in bar_news['article'] :
                    self.print_output(article)

        elif cache_news_data is False :    

            for article in articles :
                news_dict = {
                    'source': article.get('source', {}).get('name', ''),
                    'author': article.get('author', ''),
                    'title': article.get('title', ''),
                    'description': article.get('description', '')
                }
                self.news_list.append(news_dict)
                self.print_output(news=news_dict)

            self.cache_news_method.save_cache(self.news_list)
                
        return 

    def fetch_news(self) -> None :
        """
            Fetch the news based on request.status_code
            If status is 200 <SUCCESS> then call get_news method
        """
        
        if response.status_code == 200 :
            news_data = response.json()
            self.get_news(news_data)

        else :
            return f"{response.status_code}\nTry again laters"

    def print_output(self, news : dict) :
        
        print(f"=={news['title']}==")
        print(f"{news['description']}")
        print(f"{news['author']} - {news['source']}")

class cacheNews() :
    
    def __init__(self) :
        self.cache = {}

    def create_keys(self, params : dict, urls : str) -> dict:
        """
            Create unique key based of parameters, customize your own parameter in global varible
        """

        news_data = hashlib.md5(json.dumps(params, sort_keys=True).encode()).hexdigest()
        self.cache[urls] = news_data

        return self.cache

    def save_cache(self, news_article : dict) -> None:
        """
            Save the cache to the cache file with unique key and news article
        """

        self.create_keys(params=parameters, urls=url)
        self.cache['article'] = news_article

        with open(file= MY_CACHE_PATH, mode='w') as cn :
            json.dump(self.cache, cn, indent=4)

    def load_cache(self, token : dict) -> bool :
        """
            Check cache file whether the key is present or not , return Boolean
        """
        
        with open(file= MY_CACHE_PATH, mode='r') as foo :
            open_cache = json.load(foo)
            if token[url] == open_cache[url]:
                return True
            else :
                return False

if __name__  == "__main__" :
    my_news = newsAggr()
    my_news.fetch_news()