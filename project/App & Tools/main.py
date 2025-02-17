from yt_dlp import YoutubeDL
import os

# Change your download path
MAIN_PATH = os.getcwd()
print(MAIN_PATH)

class youtubeVideo() :
    
    def __init__(self) :
        pass

    def downloadVideos(self, urls) :

        self.options = {
            'format' :'best',
            'outtmpl' : '%(title)s.%(ext)s'
        }

        with YoutubeDL(self.options) as yt :
            yt.download(urls)
            # videos = yt.download(urls)

        # self.save(videos)
    
    def downloadAudios(self, urls) :
        print('Download Audio....')
    
    def downloadSubtitle(self, urls) :
        self.options = {
            'writesubtitles' : True,
            'format' :'best',
            'subtitleslangs' : ['en'],
            'skip_download' : True,
            'quiet' : True
        }

        with YoutubeDL(self.options) as yt :
            yt.download(urls)

    # def save(self, videos) :
        
    #     if not os.path.exists(f"{MAIN_PATH}/MyDownload") :
    #         download_path = os.makedirs('MyDownload')

    #     os.rename(MAIN_PATH, f"{MAIN_PATH}/Downloads")
    

class showInfo() :
    
    def __init__(self) :
        self.options = {
            'quiet' : True,
            'extract_flat' : True,
            'Force_generic_extractor' : True
        }

    def getMetaData(self, urls) :
        with YoutubeDL(self.options) as yt :
            data = yt.extract_info(url=urls, download=False)

        print('Title', data.get('title'))
        print('Descrition', data.get('description'))


class handler() :
    
    def __init__(self) :
        pass

    def commandMessage(self) :
        print(f"""
            Select actions :
            1. Download Youtube Video
            2. Download Youtube Audio
            3. Show Info
            4. Manage file (coming soon...)
            
            X. Exit 
        """)

        user_choice = input("I choose : ")
        user_urls = input('Urls : ')
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

        print(f"""
        Hi ! Welcome to MYoutube Downloader :)

        Anything can I help for you?
        From downloading video , audio even managing them.
        """)

        ask_user = input('(y/n) : ')
        self.userInput(ask_user)
        
    
    def userInput(self, user_answer) :

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