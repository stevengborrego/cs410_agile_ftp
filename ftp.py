""" CS 410/510 Summer 2022

Team Members:
Steven Borrego
Storm Crozier
Lakshmi Yalamarthi
Minh Tran
Dawson Shay

"""

from ftplib import FTP
from re import A

from numpy import append, array

import os
import socket
import psutil
import sys
import difflib


class FTP_Client:
    def __init__(self, ftp):
        self.ftp = ftp
    def passOS(self, os):
        self.os = os

    def list_directories_and_files(self):
        self.ftp.dir()

    def get_file(self):
        try:
            fileName = input("Enter file name: ")

            localFile = open(fileName, 'wb')
            self.ftp.retrbinary('RETR ' + fileName, localFile.write, 1024)

            localFile.close()
        except:
            print('Please enter valid file path.')

    def _get_file(self, fileName):

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

    def _get_mul_files(self, list):
        try:
            files = list.split(" ")

            for file in files:
                self.ftp.retrbinary("RETR "+file, open(file, 'wb').write)
            self.ftp.close
        except:
            print('Please enter valid file paths.')

    def local_dir_and_files(self):
        files = os.listdir(os.curdir)
        print (files)

    def _local_dir_and_files(self):
        files = self.os.listdir(os.curdir)
        print (files)

    def put_file(self):
        try:
            fileName = input("Enter file name: ")
            self.ftp.storbinary('STOR '+fileName, open(fileName, 'rb'))
        except:
            print('Please enter a valid file path.')

    def _put_file(self, fileName):
        try:
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

    def _create_dir(self, dir):
        try:
            self.ftp.mkd(dir)
        except:
            print('Please enter a valid directory path.')

    def delete_dir(self):
        try:
            dir = input("\nEnter directory name to delete: ")
            path = self.ftp.pwd()

            self.ftp.rmd(path + dir)
        except:
            print('Please enter a valid directory path.')

    def _delete_dir(self, dir):
        try:
            self.ftp.rmd(dir)
        except:
            print('Please enter a valid directory path.')


    def save_info(self, loginInfo): 
        saveInfo = map(lambda x: x + '\n', loginInfo) # format info as newline seperated array 
        with open("connect.txt","w") as f: # 'w' mode so it overwrites each time new info is saved
            f.writelines(saveInfo)
        f.close()

    def load_info(self):
        loginInfo = []
        with open("connect.txt") as f:
            for line in f:
                loginInfo.append(line.strip()) # remove newlines
        return loginInfo

    def copy_dir(self, dir:str):
        try:
            local_path = os.getcwd()
            remote_path = self.ftp.pwd()


            #dir = input("\nEnter directory name to copy: ")


            #dir = input("\nEnter directory name to copy: ")


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

    def _copy_directories(self, list):
        try:
            directories = list.split(" ")

            for dir in directories:
                self.ftp.copy_dir(dir)
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

    def _rename_file_remote(self, fromName, toName):
        try:
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

    def _rename_file_local(self, fromName, toName):
        try:
            self.os.rename(fromName, toName)
        except:
            print('Please enter valid file paths.')

    def upload_multiple_files(self):
        try:
            dir = input("Enter Directory path for files you want to upload : ")
            files = os.listdir(dir)
            print(files)
            for filename in files:
                opened_file = open(dir + '/' + filename, 'rb')
                self.ftp.storbinary('STOR ' + filename, opened_file)
                opened_file.close()
        except:
            print('Please enter valid file paths.')
    
    def _upload_multiple_files(self, files):
        try:
            for filename in files:
                #opened_file = open(dir + filename, 'rb')
                self.ftp.storbinary('STOR '+ filename, filename)
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

    def _session_details_for_update(self):
        file = "session.txt"
        f = open(file, "w")
        count = 0
        files = ""
        ip = socket.gethostbyname("ftp.epizy.com")
        session = ''
        user = ''
        port = ''
        localtime = ''
        mem = ''
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

    def _delete_file(self, fileName):
        try:
            print(self.ftp.delete(fileName))
        except:
            print('Please enter valid file path.')

    def change_permission(self):
        fileName = input("Enter file name: ")
        desiredPermission = input("Enter desired permission: ")
        print(self.ftp.sendcmd('SITE CHMOD ' + desiredPermission + ' ' + fileName))
    
    def _change_permission(self, fileName, desiredPermission):
        print(self.ftp.sendcmd('SITE CHMOD ' + desiredPermission + ' ' + fileName))


    def diff(self): # similar in function to GNU's diff
        file1 = input("Enter first file: ")
        file2 = input("Enter second file: ")
        with open(file1) as file_1:
            file_1_text = file_1.readlines()
            
        with open(file2) as file_2:
            file_2_text = file_2.readlines()
            
        # find and print the diff:
        for line in difflib.unified_diff(
                file_1_text, file_2_text, fromfile=file1, 
                tofile=file2, lineterm=''):
            print(line)

    def _diff(self, file1, file2): # For Unit test
        with open(file1) as file_1:
            file_1_text = file_1.readlines()
            
        with open(file2) as file_2:
            file_2_text = file_2.readlines()
            
        # find and print the diff:
        for line in difflib.unified_diff(
                file_1_text, file_2_text, fromfile=file1, 
                tofile=file2, lineterm=''):
            print(line)


    def cat(self): # display contents of file 
        try:
            fileName = input("Enter file you'd like to see contents of: ")
            fileName = open(fileName, 'r')
            content = fileName.read()
            print(content)
            fileName.close()
        except:
            print('Please enter valid file name.')

    def _cat(self, fileName): # For Unit test
        fileName = open(fileName, 'r')
        content = fileName.read()
        print(content)
        fileName.close()



    def log_off(self):
        self.ftp.quit()
        print('You are now logged off')


# # login credentials
# host: ftp.epizy.com
# username: epiz_32073599
# password: UMDmFiWWBp

        
    def menu(self):
        loadInfo = input("Load connection info from file? [Press ENTER if YES, otherwise submit ANY KEY]: ")
        
        if (loadInfo == ""):
            file_exists = os.path.exists('connect.txt')
            if (file_exists == True):
                loginInfo = self.load_info()
                host = loginInfo[0]
                user = loginInfo[1]
                password = loginInfo[2]
            else:
                print("No such file found, please enter manually")
                host = input('Enter hostname: ')
                user = input('Enter username: ')
                password = input('Enter password: ')
                loginInfo = [host, user, password]
        else:
            host = input('Enter hostname: ')
            user = input('Enter username: ')
            password = input('Enter password: ')
            loginInfo = [host, user, password]
                

        options = {'0': self.list_directories_and_files,
                   '1': self.get_file,
                   '2': self.log_off,
                   '3': self.get_mul_files,
                   '4': self.local_dir_and_files,
                   '5': self.put_file,
                   '6': self.create_dir,
                   '7': self.delete_file,
                   '8': self.change_permission,
                   '9': self.copy_directories,
                   '10': self.delete_dir,
                   '11': lambda: self.save_info(loginInfo),
                   '12': self.rename_file_remote,
                   '13': self.rename_file_local,
                   '14': self.upload_multiple_files,
                   '15': self.session_details_for_update,
                   '16': self.diff,
                   '17': self.cat,
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
                print('8: Change permissions on remove server')
                print('9: Download directories on remote server')
                print('10: Delete directories on remote server')
                print('11: Save connection information')
                print('12: Rename file on remote server')
                print('13: Rename local file')
                print('14: Upload multiple files to remote server')
                print('15: saving server details to file before update')
                print('16: Return the difference (diff) between two files')
                print('17: Print contents of file')

                selection = input('\nPlease make a selection: ')

                if selection in options.keys():
                    options[selection]()
                else:
                    print('\nPlease make a valid selection')


if __name__ == "__main__":
    print('====================================================')
    print('CS 410/510 Agile - Group  Project')
    print('====================================================')

    ftp = FTP_Client(ftp=None)
    ftp.menu()
