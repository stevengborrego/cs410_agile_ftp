""" CS 410/510 Summer 2022

Team Members:
Steven Borrego


"""

from ftplib import FTP
import pyftpdlib

class FTP_Client:
    def __init__(self):
        pass



    def connect(self, host='ftpupload.net', user='epiz_32073599', password='UMDmFiWWBp'):
        with FTP(host) as ftp:
            ftp.login(user=user, passwd=password)
            print(ftp.getwelcome())



if __name__ == "__main__":
    print('====================================================')
    print('CS 410/510 Agile - Group  Project')
    print('====================================================')

    ftp = FTP_Client()
    ftp.connect()


