""" CS 410/510 Summer 2022

Team Members:
Steven Borrego
Storm Crozier
Lakshmi Yalamarthi


"""

from ftplib import FTP

from numpy import append, array

import os
import  socket
import psutil

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
        try:
            list = input("\nEnter files' name separated by space: ")

            files = list.split(" ")

            for file in files:
                self.ftp.retrbinary("RETR "+file, open(file, 'wb').write)
            self.ftp.close
        except:
            print('Please enter valid file paths.')

    def local_dir_and_files(self):
        files = os.listdir(os.curdir)
        print (files)

    def put_file(self):
        try:
            fileName = input("Enter file name: ")
            self.ftp.storbinary('STOR '+fileName, open(fileName, 'rb'))
        except:
            print('Please enter a valid file path.')

    def create_dir(self):
        try:
            dir = input("\nEnter directory name to create: ")
            path = self.ftp.pwd()

            self.ftp.mkd(path + dir)
        except:
            print('Please enter a valid directory path.')

    def delete_dir(self):
        try:
            dir = input("\nEnter directory name to delete: ")
            path = self.ftp.pwd()

            self.ftp.rmd(path + dir)
        except:
            print('Please enter a valid directory path.')

    def copy_dir(self, dir:str):
        try:
            local_path = os.getcwd()
            remote_path = self.ftp.pwd()

<<<<<<< HEAD
            #dir = input("\nEnter directory name to copy: ")
=======

        #dir = input("\nEnter directory name to copy: ")
>>>>>>> a758ca6dcfb69362b1971cf00b240bd37c141041

            #cd to dir on remote server
            self.ftp.cwd(remote_path + dir)

            #create dir with same name on local machine and cd into it
            new_local_path = os.path.join(local_path, dir)
            os.mkdir(new_local_path)
            os.chdir(new_local_path)


            files = self.ftp.nlst()
            for file in files:
                self.ftp.retrbinary("RETR "+file, open(file[1:], 'wb').write)
            self.ftp.close
        except:
            print('error')

    def copy_directories(self):
        try:
            self.list_directories_and_files()
            list = input("\nEnter directories' name seperated by space: ")

            directories = list.split(" ")

            for dir in directories:
                self.copy_dir(dir)
            self.ftp.close
        except:
            print('Please enter valid directory paths.')

    def rename_file_remote(self):
        try:
            fromName = input("Enter name of file you want to change: ")
            toName = input("Enter new name of file: ")
            self.ftp.rename(fromName, toName)
        except:
            print('Please enter valid file paths.')

    def rename_file_local(self):
        try:
            fromName = input("Enter name of file you want to change: ")
            toName = input("Enter new name of file: ")
            os.rename(fromName, toName)
        except:
            print('Please enter valid file paths.')

    def upload_multiple_files(self):
        try:
            dir = input("Enter Directory path for files you want to upload : ")
            files = os.listdir(dir)
            print(files)
            for filename in files:
                opened_file = open(dir + filename, 'rb')
                self.ftp.storbinary('STOR '+ filename, opened_file)
                opened_file.close()
        except:
            print('Please enter valid file paths.')

    def session_details_for_update(self):
        file = "session.txt"
        f = open(file, "w")
        count = 0
        files = ""
        for file in self.ftp.nlst():
            files = files + ", " + file
            count += 1
        ip = socket.gethostbyname("ftp.epizy.com")
        session = self.ftp.getwelcome()
        user = session.split("user number ")[1].split(" ")[0]
        port = session.split("Server port:")[1].split(".")[0]
        localtime = session.split("is now")[1].split(".")[0]
        mem = round((psutil.virtual_memory()[1] / (1024.0 ** 3)), 2)
        f.write("Update in session, stats before the update : \n" + "IP address : " + ip + "\n" +
                "Number of files in server : " + str(count) + "\n" +
                "List of files in the server before this update : " + files + "\n" +
                "User id : " + user + "\nServer Port : " + port + "\n" +
                "Local time in the server : " + localtime + "\n" +
                "Available memory : " + str(mem) + " Gb \n"
                )
        f.close()

    def delete_file(self):
        try:
            fileName = input("Enter file name: ")
            print(self.ftp.delete(fileName))
        except:
            print('Please enter valid file path.')

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
                   '4': self.local_dir_and_files,
                   '5': self.put_file,
                   '6': self.create_dir,
                   '7': self.delete_file,
                   '9': self.copy_directories,
                   '10': self.delete_dir,
                   '12': self.rename_file_remote,
                   '13': self.rename_file_local,
                   '14': self.upload_multiple_files,
                   '15': self.session_details_for_update
                   }

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
                print('4: List directories and files on local machine')
                print('5: Put file onto remote server')
                print('6: Create directory on remote server')
                print('7: Delete file from remote server')
                # print('8: Change permissions on remove server')
                print('9: Copy directories on remote server')
                print('10: Delete directories on remote server')
                # print('11: Save connection information')
                print('12: Rename file on remote server')
                print('13: Rename local file')
                print('14: Upload multiple files to remote server')
                print('15: saving server details to file before update')

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
