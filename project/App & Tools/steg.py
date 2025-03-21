# Import library and package
from PIL import Image


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
                print('Continue....')
                break
            else :
                print('Stop.')
                break
        else :
            print('Invalid input.')

if __name__ == '__main__' :
    run = userInterfaces()
    run.ask_user()
