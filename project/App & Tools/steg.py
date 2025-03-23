# Import library and package
from PIL import Image

class convertText :

    def __init__(self) :
        self.user_secret_text = input('Input your text : ')
        self.convert_to_binary(user_secret_text=self.user_secret_text)

    def convert_to_binary(self, user_secret_text : str) -> bin:
        character_bin = []
        
        for i in user_secret_text :
            char_unicode = ord(i)
            character_bin.append(bin(char_unicode)[2:])
        
        print(character_bin)
        return character_bin

class userInterfaces :

    def __init__(self) :
        print(f"""\n
            {'='*20}
            Welcome to StegAgent :)

            I will be your agent to slip a text between image binaries.
            {'='*20}\n
        """)

    def ask_user(self) :
        users_ans = input('Do you want to continue? (y/n) : ')
        users_ans = users_ans.lower()

        while users_ans in ('y','n') :
            if users_ans == 'y' :
                do_convert = convertText()
                break
            else :
                print('Stop.')
                break
        else :
            print('Invalid input.')

if __name__ == '__main__' :
    run = userInterfaces()
    run.ask_user()
