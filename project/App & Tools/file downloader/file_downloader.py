import urllib.request
import os 
import shutil

class downloader() :
    def __init__(self) :
        pass

    def download(self,file_url) :
        """Download the file and move to the new path"""
        file_name = os.path.basename(file_url)
        file = urllib.request.urlretrieve(url=file_url,filename = file_name)
        
        save_path = 'project/test file/' + file_name
        shutil.move(src=file_name,dst=save_path)

if __name__ == '__main__' :
    print('Hi! Welcome to FileDownloader\n')

    print('What file I can download? : ')
    print('1. Image')
    print('2. Text File\n')

    while True :
        ask_user = input('Want to use? (y/n) : ')

        if ask_user == 'y' :
            file_url = input('\nFile url : ')

            run_downloader = downloader()
            run_downloader.download(file_url=file_url)

        else :
            print('\nBye')
            break
            
    else :
        print('\nBye')

# Test File to Download
# {
#   https://cdn.idntimes.com/content-documents/bank-soal-ujian-cpns.pdf,
#   https://ironerozanie.wordpress.com/wp-content/uploads/2013/03/soal-dan-pembahasan-un-matematika-smp-2012.pdf
# }

# Test Image to Download
# {
    # https://www.freepik.com/free-photo/high-angle-couple-hiking-trip_41012576.htm
# }