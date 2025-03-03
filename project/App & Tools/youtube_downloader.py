import os
import json
from yt_dlp import YoutubeDL

# Change your download path
MAIN_PATH = os.getcwd()

class youtubeVideo() :
    
    def __init__(self) :
        self.metadata_youtube = showInfo()
        self.file_path = (f"{MAIN_PATH}/downloaded")
        os.makedirs(f"{MAIN_PATH}/downloaded", exist_ok=True) # Immediately create downloaded folder if doesn't exist

    def downloadVideos(self, urls : str) :
        """
            Download Videos, Audios, or even Subtitles with given url. Automatically saved in /downloader folder
        """

        self.options = {
            'format' :'best',
            'quiet' : True,
            'outtmpl' : os.path.join(self.file_path, '%(title)s.%(ext)s')
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
            'outtmpl' : os.path.join(self.file_path, '%(title)s.%(ext)s')
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
            'outtmpl' : os.path.join(self.file_path, '%(title)s.%(ext)s')
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
        os.makedirs(f"{MAIN_PATH}/cache", exist_ok=True) # Immediately create cache folder if doesn't exist

    def getMetaData(self, urls : str) -> None:
        """
            Extract metadata from given url and save the cache in dump.json.
            Return None.
        """
        with YoutubeDL(self.options) as yt :
            data = yt.extract_info(url=urls, download=False)
            self.printMetaData(data=data)


        # youtube_video : dict, only store some of the data from metadata
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


                save_youtube_cache = cacheManager()
                save_youtube_cache.saveCache(youtube_cache_data=cache_data, cache_video=youtube_video)
            
    def printMetaData(self, data : dict) : 
        """
            Take an argument from metadata, and print it on the terminal. Called by showInfo().\n
            Print (id, channel, fulltitle, description). You may modify print statement as well as youtube_video (video's metadata).
        """
        print("=" * 40)
        print(f'\nID : {data.get("id")}' )
        print(f'Channel : {data.get("channel")}\n')
        print(f'Title : \n{data.get("fulltitle")}\n')
        print(f'Description : \n{data.get("description")}')
        print("=" * 40)

class cacheManager() :
    """
        Manage all cache operations. From display, looking spesific video even delete cache.
    """

    def __init__(self) :
        self.CACHE_PATH = f"{MAIN_PATH}/cache/dump.json"

    def doesExist(self) -> bool : 
        """
            Check whether dump.json containt data or not. Return boolean.
        """

        if os.path.getsize(self.CACHE_PATH) != 0 :
            return True

        return False

    def saveCache(self, youtube_cache_data : list , cache_video : dict) :
        """
            save metadata into json.
        """

        cache_video_id = cache_video.get('id')
        existing_data = self.lookCache(videos_id=cache_video_id)

        if existing_data == False :
            with open(self.CACHE_PATH, mode='w') as file :
                json.dump(youtube_cache_data, file, indent=4)
            
            print('Append new data')

        else : 
            return print(f"There is already {cache_video_id} in cache")

    def lookCache(self, videos_id : str) -> bool :
        """
            look an id from youtube_video (video's metadata) to search it in existing json data.
        """

        # Check wheter file does exist or not
        if self.doesExist() is False :
            print('No data shown')
            exit()

        # Use r+ mode to read data.
        with open(self.CACHE_PATH, mode='r+') as file :
            youtube_cache = json.load(file)

            list_video : list = [x for x in youtube_cache if x['id'] == videos_id]

            if len(list_video) == 0 :
                print(f'There is no {videos_id} found -------')
                return False
            
            dict_video : dict = list_video[0]

            if videos_id == dict_video.get('id') :
                print(f'``````Found {videos_id} on cache.``````')
                return True
        
    def lookId(self, videos_id : str) :
        """
            Look for spesific videos id and print to the terminal
        """

        # Check wheter file does exist or not
        if self.doesExist() is False :
            return print('No data shown')

        with open(self.CACHE_PATH, mode='r') as file :
            youtube_cache = json.load(file)

        list_video = next((x for x in youtube_cache if x['id'] == videos_id), None)

        if list_video is None:
            print(f'There is no {videos_id} found -------')
            return False
            
        self.displaySpesific(cache=list_video)

    def deleteCache(self, videos_id_del : str) :
        """
            delete json cache from given id.
        """

        look_cache_data = self.lookCache(videos_id=videos_id_del)

        if look_cache_data == False :
            return print(f"There is no {videos_id_del} available in cache data.\nUnable to delete.")

        with open(self.CACHE_PATH, mode='r+') as file :
            youtube_cache_del = json.load(file)

            len_youtube_cache = (len(youtube_cache_del) - 1 )
            for cache in range(len_youtube_cache) :
                if youtube_cache_del[cache]['id'] == videos_id_del :
                    del youtube_cache_del[cache]

            file.seek(0) #position cursor to the beginning
            file.truncate() #clear exisisting data
            json.dump(youtube_cache_del, file, indent=4)

        return print(f"{videos_id_del} cache have been deleted.")

    def displayAllCache(self) :
        """
            Display all cache in dump.json.\n
            Print(ID, channel, video title, video language , and video url)
        """
        
        # Check wheter file does exist or not
        if self.doesExist() is False :
            return print(f"There is no cache")

        # Load cache data in dump.json which is list type
        with open(self.CACHE_PATH, mode='r') as file :
            cache_data : list = json.load(file)

        # Loop through list of cache_data and display only necessary part to the terminal
        for item in cache_data :
            video_id = item['id']
            video_channel = item['channel']
            video_details = item['video'][0]
            video_title = video_details['video_title']
            video_url = video_details['video_url']

            print("="*30)
            print(f"ID      :       {video_id}")
            print(f"Channel :       {video_channel}")
            print(f"Title   :       {video_title}")
            print(f"URL     :       {video_url}")
            print("="*30, '\n')

    def displaySpesific(self, cache : dict = {}) :
        """
            display spesific cache with given id
        """

        # Check wheter file does exist or not
        if self.doesExist() is False :
            return print(f"There is no cache")
        
        # Run code when len(cache) not equal to zero
        if len(cache) != 0 :
           
            print('\n') 

            # Loop throught dictionaries and retrieve all data.
            for key, value in cache.items() :
                if key == 'video' :
                    videos_details = value[0] # Access only dictionary , in this case value is list type.
                    videos_title = videos_details.get('video_title')
                    videos_language = videos_details.get('video_language')
                    videos_url = videos_details.get('video_url')
                    videos_description = videos_details.get('video_description')
                    
                    # Print all data to the terminal
                    print("="*40)
                    print(f"Title           :   {videos_title}")
                    print(f"Language        :   {videos_language}")
                    print(f"URL             :   {videos_url}")
                    print(f"Description     :   \n{videos_description}")
                    print("="*40)
                        
                # Print other value to the screen
                else :
                    print(value)

        # return such print statement to the terminal
        else :
            return print(f"There is no such data in cache.")

class manageFile() :

    def __init__(self) :
        """
            Display welcome message all possible action users can do.
        """
        print(f"""
            1. Display Cache
            2. Look Spesific Cache
            3. Delete Cache

            X. Quit
        """)

    def userAction(self) -> None :
        """
            Take an input from user and run code within a statement
        """
        my_cache = cacheManager()
        ask_user : str = input('Do : ')

        if ask_user == '1' :
            my_cache.displayAllCache()
        elif ask_user == '2' :
            user_video_id = input("Video ID : ")
            my_cache.lookId(videos_id=user_video_id)
        elif ask_user == '3' :
            user_video_del = input("Video ID : ")
            my_cache.deleteCache(videos_id_del=user_video_del)
        elif ask_user.lower() == 'x' :
            exit()
        else :
            print('Invaid Input')


class userInterface() :
    """
        Handle all user interactions.
    """
    
    def __init__(self) :
        """
            Display list of action user can do.
        """
        print(f"""
            Select actions :
            1. Download Youtube Video
            2. Download Youtube Audio
            3. Download Youtube Substitle
            4. Show Video Info
            5. Manage file (only cache data)
            
            X. Exit 
        """)

        self.commandMessage()

    def commandMessage(self) -> None:
        """
            List of all possible action user can do. From downloading youtube video, youtube audio, get metadata, write substitle, to managing files.
        """

        user_choice : str = input("I choose : ")
        myInfo = showInfo()

        if user_choice.lower() == 'x' :
            exit()
        
        if user_choice.lower() == '1' :
            user_urls : str = input('Urls : ')
            myYoutube = youtubeVideo()
            myYoutube.downloadVideos(user_urls)

        elif user_choice.lower() == '2' :
            user_urls : str = input('Urls : ')
            myYoutube = youtubeVideo()
            myYoutube.downloadAudios(user_urls)

        elif user_choice.lower() == '3' :
            user_urls : str = input('Urls : ')
            myYoutube = youtubeVideo()
            myYoutube.downloadSubtitle(user_urls)

        elif user_choice.lower() == '4' :
            user_urls : str = input('Urls : ')
            myInfo.getMetaData(user_urls)

        elif user_choice.lower() == '5' :
            myFile = manageFile()
            myFile.userAction()

        else :
            print('Invalid Input')

class welcome() :

    def __init__(self) :
        """
            Show welcome message to user, user have to answer Y/N in question to proceed the program.
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

        while user_answer.lower != 'n' or user_answer.lower() == 'n': 
            if user_answer.lower() == 'n' :
                print('Good Bye ..... :)')
                break
            elif user_answer.lower() == 'y' :
                 userInterface()
        else :
            print('You entered wrong one.')


if __name__ == "__main__" :
    welcome()

# Youtube Links for testing purpose
# https://www.youtube.com/watch?v=WIyTZDHuarQ&t=15ss (Veritasium)
# https://youtube.com/watch?v=Z_xJ40QXu7Q&t=46s (XKCD What's if)
# https://www.youtube.com/watch?v=Qewt66Yu7jE (One Minute Earth)
# https://www.youtube.com/watch?v=KdoaiGTIBY4 (Mults)