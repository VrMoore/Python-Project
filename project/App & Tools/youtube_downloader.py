from yt_dlp import YoutubeDL
import os
import json

# Change your download path
MAIN_PATH = os.getcwd()
print(MAIN_PATH)

class youtubeVideo() :
    
    def __init__(self) :
        self.metadata_youtube = showInfo()
        self.file_path = (f"{MAIN_PATH}/downloaded")

    os.makedirs(f"{MAIN_PATH}/downloaded", exist_ok=True)

    def downloadVideos(self, urls : str) :

        self.options = {
            'format' :'best',
            'outtmpl' : os.path.join(f"{self.file_path}",'%(title)s.%(ext)s')
        }

        with YoutubeDL(self.options) as yt :
            yt.download(urls)
            self.metadata_youtube.getMetaData(urls=urls)
    
    def downloadAudios(self, urls : str) :
        
        self.options = {
            'format' : 'best',
            'extract_audio' : True,
            'audio_format' : 'mp3',
            'audio_quality' : '192',
            'outtmpl' : os.path.join(f"{self.file_path}",'%(title)s.%(ext)s')
        }

        with YoutubeDL(self.options) as yt :
            yt.download(urls)
            self.metadata_youtube.getMetaData(urls=urls)

    
    def downloadSubtitle(self, urls : str) :
        self.options = {
            'writesubtitles' : True,
            'format' :'best',
            'subtitleslangs' : ['en'],
            'skip_download' : True,
            'quiet' : True,
            'substitlesformat' : 'srt',
            'outtmpl' : os.path.join(f"{self.file_path}", '%(title)s.%(ext)s')
        }

        with YoutubeDL(self.options) as yt :
            yt.download(urls)
            self.metadata_youtube.getMetaData(urls=urls)

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

        # Immediately create cache folder if does not exist
        os.makedirs(f"{MAIN_PATH}/cache", exist_ok=True)

        # youtube_video : dict, only store some of data from metadata
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

        # Check whether if the file is exist or not, if it's not : immediately made dump.json with empty list in it.
        if not os.path.exists(f"{MAIN_PATH}/cache/dump.json") :
            with open(f'{MAIN_PATH}/cache/dump.json' , mode='w') as file :
                youtube_cache = []
                json.dump(youtube_cache, file)

        # if there is a file but empty, immediately make empty list and append metadata
        if os.path.getsize(f"{MAIN_PATH}/cache/dump.json") == 0 :
            with open(f"{MAIN_PATH}/cache/dump.json", mode='w') as file :
                youtube_cache = []
                youtube_cache.append(youtube_video)
                json.dump(youtube_cache, file, indent=4)

        # if there is file but have data, load the file first and append it after. Overwrite existing one with a new one.
        else :   

            with open(f"{MAIN_PATH}/cache/dump.json", mode='r') as file :
                cache_data = json.load(file)
                cache_data.append(youtube_video)


                save_youtube_cache = myCache()
                save_youtube_cache.saveCache(youtube_cache_data=cache_data, cache_video=youtube_video)
            
    def printMetaData(self, data : dict) : 
        """
            Take an argument from metadata, and print it on the terminal.
            Print (id, channel, fulltitle, description). You may modify print statement as well as youtube_video (video's metadata).
        """
        print("=" * 40)
        print(f'\nID : {data.get("id")}' )
        print(f'Channel : {data.get("channel")}\n')
        print(f'Title : \n{data.get("fulltitle")}\n')
        print(f'Description : \n{data.get("description")}')
        print("=" * 40)

class myCache() :

    def __init__(self) :
        self.CACHE_PATH = f"{MAIN_PATH}/cache/dump.json"

    def saveCache(self, youtube_cache_data : list, cache_video : dict) :
        """
            save metadata into json.
        """

        cache_video_id = cache_video.get('id')
        existing_data = self.lookCache(videos_id=cache_video_id)
        print(existing_data, '---------------------')

        if existing_data is False :
            with open(self.CACHE_PATH, mode='w') as file :
                json.dump(youtube_cache_data, file, indent=4)
            
            print('Append new data')

        return print(f"There is already data")

    def lookCache(self, videos_id : str)  :
        """
            look an id from youtube_video (video's metadata) to search it in existing json data.
        """
        
        if os.path.getsize(f"{MAIN_PATH}/cache/dump.json") == 0 :
            return print('No data shown')

        with open(self.CACHE_PATH, mode='r') as file :
            youtube_cache = json.load(file)

        list_video : list = [x for x in youtube_cache if x['id'] == videos_id]
        dict_video : dict = list_video[0]

        if videos_id == dict_video.get('id') :
            print('Found it!!')
            return True
        else :
            print(f'There is no {videos_id} found -------')
            return False
        

    def deleteCache(self, videos_id : str) :
        """
            delete json cache from given id.
        """

        pass
        

class handler() :
    """
        Handle all user interactions.
    """
    
    def __init__(self) :
        pass

    def commandMessage(self) :
        """
            List of all possible action user can do. From downloading youtube video, youtube audio, get metadata, write substitle, to managing files.
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
    # tes = myCache()
    # tes.lookCache("Qewt66Yu7jE")


# Youtube Links for testing purpose
# https://www.youtube.com/watch?v=WIyTZDHuarQ&t=15ss (Veritasium)
# https://youtube.com/watch?v=Z_xJ40QXu7Q&t=46s (XKCD What's if)
# https://www.youtube.com/watch?v=Qewt66Yu7jE (One Minute Earth)
# https://www.youtube.com/watch?v=KdoaiGTIBY4 (Mults)