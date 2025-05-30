
# Python-Project

This repository is mainly made for learn Python programming. I made these project from beginner level to more advance level. These project will help _user_ to understand fundamental concepts such as loop, class, function, etc.

## [Application](#apps)

### [API](#api)
1. [Weather API](#weather_api) 
2. [News Aggregator ( with JSON caching)](#news_api)

### [Apps & Tools](#tools)
1. [File Downloader](#file_downloader)
2. [Password Generator](#password_generator)
3. [Simple to do list](#to-do_list) 
4. [Webscrapper](#webscrapper)
5. [Youtube Downloader](#youtube_downloader)
6. JSON Cache Storage

### [Games](#games)
1. Dice roll simulator
2. Rock, paper and scissor Game
3. Guessing Number


## <a id='apps'>App Description

### <a id='api'>API
This folder will teach you how to use API in your program. From simple as weather api to news aggregator.

1. <b><a id='weather_api'>Weather API</b>
	First project to learn how to use api , apply parameters and print output to terminal. Weather API use [VisualCrossing](https://www.visualcrossing.com/) to fetch data. This file is simple implementation of using an api.

2. <b><a id="news_api">News Aggregator</b>
	News aggregator uses [News Api](https://newsapi.org/) where it will fetch the news from. Login an create an API key that later use in development.

	Create environment variables in .env files in the same folder as news_api.py
	
	``API_KEY = '(enter your API Key)'``

	Edit your endpoint refers to : https://newsapi.org/docs/endpoints/everything
	```
	# Examples of parameters in line 13
	
	parameters = {
	'apiKey' : api_key,
	'country' : 'us',
	'category' : 'health',
	'language' : 'en',
	'sortBy' : 'popularity',
	'from' : '2024-09-16',
	'to' : '2025-01-16',
	'language' : 'en',
	'sortBy' : 'popularity'
	'q' : 'ships'
	}
	```

	News aggregator also include JSON caching using JSON library from python. Automatically create json file once the endpoint is established.

### [Apps & Tools](#tools)
This folders contains applications & tools that made using vanilla python. Such as : file downloader, to do list, youtube downloader, etc.

1. <b><a id='file_downloader'>File downloader</b>
	File downloader use urllib python library to make a request. Only work with a link that have extension of the file in the url. E.g :

	``https://ironerozanie.wordpress.com/wp-content/uploads/2013/03/soal-dan-pembahasan-un-matematika-smp-2012.pdf``

2. <b><a id='password_generator'>Password Generator </b>
	Generate password randomly based off parameters using random module. You may not use this program to make password for your email account, game account, etc, it might be unsafe thus the code is crackable and unsafe.

3. <b><a id='to-do_list'>Simple to do list</b>
	Simple to-do list app in your terminal. Your task only accessible in that one instance, hence there is no JSON caching implemented. 

4. <b><a id='web_scrapper'> Web scrapper</b>
	This project is abandoned. <b>This code is break, you may not use it in your code editor<b>
	
5. <b><a id='youtube_downloader'>Youtube Downloader</b>
	Simple apps that allow you to download video, audio, substitle and show metadata info in your terminal. Make sure you install [yt-dlp](https://github.com/yt-dlp/yt-dlp) using PIP and ffmpeg (for audio) in order to run the script.

	You may customize self.options in youtubeVideo() class based on your preferred choices.
	```
		# Check the documentation for clear instruction
		
		self.options = {
            'format' :'best',
            'quiet' : True,
            'outtmpl' : os.path.join(self.file_path, '%(title)s.%(ext)s')
        }
	```


### <a id='games'>Games
This folder contain silly games that can be played in your terminal or GUI. Contructed using vanilla python.


### Note  
---
This project mainly made for learn. Not intended for any sort of business.
