""" CS 410/510 Summer 2022

Team Members:
Steven Borrego
Storm Crozier


"""

from ftplib import FTP

from numpy import append, array

class FTP_Client:
    def __init__(self):
        self.ftp = None

    def list_directories_and_files(self):
        self.ftp.dir()

    def get_file(self):
        fileName = input("Enter file name: ")

        localFile = open(fileName, 'wb')
        self.ftp.retrbinary('RETR ' + fileName, localFile.write, 1024)

        localFile.close()

    def get_mul_files(self):
        
        list = input("\nEnter files seperated by space: ")
        
        arr = list.split(" ")

        print(arr)

        files = self.ftp.nlst(arr)

        for file in files:
            self.ftp.retrbinary("RETR "+file, open(file, 'wb').write)
        
        self.ftp.close

    def put_file(self):
        fileName = input("Enter file name: ")
        self.ftp.storbinary('STOR '+fileName, open(fileName, 'rb'))

    def delete_file(self):
        fileName = input("Enter file name: ")
        print(self.ftp.delete(fileName))

    def log_off(self):
        self.ftp.quit()
        print('You are now logged off')

    def menu(self, host='ftp.epizy.com', user='epiz_32073599', password='UMDmFiWWBp'):
        # host = input('Enter hostname: ')
        # user = input('Enter username: ')
        # password = input('Enter password: ')

        options = {'0': self.list_directories_and_files,
                   '1': self.get_file,
                   '2': self.log_off,
                   '3': self.get_mul_files,
                   '5': self.put_file,
                   '7': self.delete_file,}

        with FTP(host) as ftp:
            self.ftp = ftp
            try:
                self.ftp.login(user=user, passwd=password)
                print(self.ftp.getwelcome())

            except:
                print("Please enter valid credentials")

            selection = ''
            while(selection != '2'):
                print('\n========== FTP Client ==========\n')
                print('0: List remote directories and files')
                print('1: Get file from remote server')
                print('2: Log off from remote server')
                print('3: Get multiple files from remote server')
                # print('4: List directories and files on local machine')
                print('5: Put file onto remote server')
                # print('6: Create directory on remote server')
                print('7: Delete file from remote server')
                # print('8: Change permissions on remove server')
                # print('9: Copy directories on remote server')
                # print('10: Delete directories on remote server')
                # print('11: Save connection information')

                selection = input('\nPlease make a selection: ')

                if selection in options.keys():
                    options[selection]()
                else:
                    print('\nPlease make a valid selection')


if __name__ == "__main__":
    print('====================================================')
    print('CS 410/510 Agile - Group  Project')
    print('====================================================')

    ftp = FTP_Client()
    ftp.menu()
