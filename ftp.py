""" CS 410/510 Summer 2022

Team Members:
Steven Borrego


"""

from ftplib import FTP

class FTP_Client:
    def __init__(self):
        self.ftp = None

    def login(self, host='ftp.epizy.com', user='epiz_32073599', password='UMDmFiWWBp'):
        with FTP(host) as ftp:
            self.ftp = ftp
            self.ftp.login(user=user, passwd=password)
            print(self.ftp.getwelcome())

    def list_directories_and_files(self):
        pass

    def get_file(self):
        pass



if __name__ == "__main__":
    print('====================================================')
    print('CS 410/510 Agile - Group  Project')
    print('====================================================')

    ftp = FTP_Client()
    ftp.login()


