from yt_dlp import YoutubeDL
import os
import json

# Change your download path
MAIN_PATH = os.getcwd()
print(MAIN_PATH)

class youtubeVideo() :
    
    def __init__(self) :
        pass

    def downloadVideos(self, urls : str) :

        self.options = {
            'format' :'best',
            'outtmpl' : '%(title)s.%(ext)s'
            # 'outtmpl' : os.path.join(f'{MAIN_PATH}/Downloaded','%(title)s.%(ext)s')
        }

        with YoutubeDL(self.options) as yt :
            yt.download(urls)
    
    def downloadAudios(self, urls : str) :
        
        self.options = {
            'format' : 'best',
            'extract_audio' : True,
            'audio_format' : 'mp3',
            'audio_quality' : '192',
            'outtmpl' :'%(title)s.%(ext)s'
            # 'outtmpl' : os.path.join(f'{MAIN_PATH}/Downloaded','%(title)s.%(ext)s')
        }

        with YoutubeDL(self.options) as yt :
            yt.download(urls)
    
    def downloadSubtitle(self, urls : str) :
        self.options = {
            'writesubtitles' : True,
            'format' :'best',
            'subtitleslangs' : ['en'],
            'skip_download' : True,
            'quiet' : True,
            'substitlesformat' : 'srt'
        }

        with YoutubeDL(self.options) as yt :
            yt.download(urls)
    

class showInfo() :
    
    def __init__(self) :
        self.options = {
            'quiet' : True,
            'extract_flat' : True,
            'Force_generic_extractor' : True
        }

    def getMetaData(self, urls : str) :
        with YoutubeDL(self.options) as yt :
            data = yt.extract_info(url=urls, download=False)
            self.printMetaData(data=data)

        os.makedirs(f"{MAIN_PATH}/cache", exist_ok=True)

        youtube_video = {
                'id' : data.get('id'),
                'channel' : data.get('channel'),
                'channel_url' : data.get('uploader_url'),
                'video' : [
                    {
                        'video_title' : data.get('fulltitle'),
                        'video_description' : data.get('description'),
                        'video_language' : data.get('language'),
                        'video_url' : data.get('original_url')
                    }
                ]
        }

        # if there is a file but empty
        if os.path.getsize(f"{MAIN_PATH}/cache/dump.json") == 0 :
            with open(f"{MAIN_PATH}/cache/dump.json", mode='w') as file :
                youtube_cache = []
                youtube_cache.append(youtube_video)
                json.dump(youtube_cache, file, indent=4)

        # if there is file but have data
        else :   

            with open(f"{MAIN_PATH}/cache/dump.json", mode='r') as file :
                cache_data = json.load(file)
                cache_data.append(youtube_video)

                self.saveCache(youtube_cache_data=cache_data)
            

    def saveCache(self, youtube_cache_data : dict) :

        with open(f"{MAIN_PATH}/cache/dump.json", mode='w') as file :
            json.dump(youtube_cache_data, file, indent=4)

    def printMetaData(self, data : dict) : 
        print(f'ID : {data.get("id")}' )
        print(f'Channel : {data.get("channel")}\n')
        print(f'Title : {data.get("fulltitle")}')
        print(f'Description : {data.get("description")}')


class handler() :
    
    def __init__(self) :
        pass

    def commandMessage(self) :
        """
            List of all possible action user can do.
        """

        print(f"""
            Select actions :
            1. Download Youtube Video
            2. Download Youtube Audio
            3. Show Info
            4. Write Substitle
            5. Manage file (coming soon...)
            
            X. Exit 
        """)

        user_choice : str = input("I choose : ")
        user_urls : str = input('Urls : ')
        myYoutube = youtubeVideo()
        myInfo = showInfo()

        if user_choice.lower() == 'x' :
            exit()
        
        if user_choice.lower() == '1' :
            myYoutube.downloadVideos(user_urls)
        elif user_choice.lower() == '2' :
            myYoutube.downloadAudios(user_urls)
        elif user_choice.lower() == '3' :
            myInfo.getMetaData(user_urls)
        elif user_choice.lower() == '4' :
            myYoutube.downloadSubtitle(user_urls)
        else :
            print('Invalid Input')

class welcome() :

    def __init__(self) :
        """
            Show greeting to user, user have to answer Y/N in question to proceed the program.
        """

        print(f"""
        Hi ! Welcome to MYoutube Downloader :)

        Anything can I help for you?
        From downloading video , audio even managing them.
        """)

        ask_user : str = input('(y/n) : ')
        self.userInput(ask_user)
        
    def userInput(self, user_answer : str) :
        """
            Take an arguments from ask_user in which user answer will be used to determine what it will do.
            if user input n , exit the program,
            if user input y, run commandMessage()
        """

        if user_answer.lower() == 'n' :
            print('Good Bye ..... :)')
            exit()
        elif user_answer.lower() == 'y' :
            user_handler = handler()
            user_handler.commandMessage()
            
        else :
            print('You entered wrong one.')


if __name__ == "__main__" :
    welcome()

# https://www.youtube.com/watch?v=WIyTZDHuarQ&t=15ss (Veritasium)
# https://youtube.com/watch?v=Z_xJ40QXu7Q&t=46s (XKCD What's if)