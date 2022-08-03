import ftplib
from unittest import mock
import unittest

from ftp import FTP_Client  

class FTPTestCase(unittest.TestCase):

    @mock.patch('ftplib.FTP')
    def test_log_off_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)
        
        ftp.log_off()
        mockFtpObj.quit.assert_called()

    @mock.patch('ftplib.FTP')
    def test_get_file_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()
        
        ftp = FTP_Client(mockFtpObj)
        
        ftp._get_file("test")
        mockFtpObj.retrbinary.assert_called()

    @mock.patch('ftplib.FTP')
    def test_get_mul_file_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)

        
        ftp.get_mul_files("test test1")
        ftp.ftp.close()
        mockFtpObj.retrbinary.assert_called()

    @mock.patch('ftplib.FTP')
    @mock.patch('ftplib.open')
    def test_put_file_sucess(self, mockFtp, mOpen):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        mOpen.return_value = mock.Mock()

        ftp = FTP_Client(mockFtpObj) 
        
        ftp._put_file("test")
        mockFtpObj.storbinary.assert_called()

    @mock.patch('ftplib.FTP')
    def test_delete_file_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj) 
        
        ftp._delete_file("test")
        mockFtpObj.delete.assert_called()
    
    @mock.patch('ftplib.FTP')
    def test_list_directories_and_file_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)

        ftp.list_directories_and_files()
        mockFtpObj.dir.assert_called()

    @mock.patch('os.dir')
    def test_list_local_directories_and_file_sucess(self, mockOs):
        mockOs.return_value = mock.Mock()
        mockOsObj = mockOs()

        ftp = FTP_Client(mockOsObj)

        ftp.local_dir_and_files()
        mockOsObj.listdir.called


    @mock.patch('ftplib.FTP')
    def test_create_dir_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)
        
        ftp._create_dir("test")

        assert mockFtpObj.mkd.called


    @mock.patch('ftplib.FTP')
    def test_delete_dir_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)
        
        ftp._delete_dir("test")

        assert mockFtpObj.rmd.called

    @mock.patch('ftplib.FTP')
    def test_copy_directory_sucess(self, mockFtp):
        mockFtp.return_value = mock.Mock()
        mockFtpObj = mockFtp()

        ftp = FTP_Client(mockFtpObj)
        
        ftp._copy_directories("test test1")

        assert mockFtpObj.copy_dir.called

   





if __name__ == '__main__':
    unittest.main()